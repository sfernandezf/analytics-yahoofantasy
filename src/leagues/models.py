from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin
from leagues.remotes import YahooLeagueRemote, YahooWeeksRemote


class YahooOauthCredentials(BaseModel):
    def __str__(self):
        return self.name

    name = models.CharField(_('Name'), max_length=64)
    consumer_key = models.CharField(_('Consumer Key'), max_length=1024)
    consumer_secret = models.CharField(_('Consumer Secret'), max_length=1024)
    access_token = models.CharField(_('Access Token'), max_length=8192)
    refresh_token = models.CharField(_('Refresh Token'), max_length=1024)
    token_time = models.FloatField(_('Token Time'))
    token_type = models.CharField(
        _('Token Type'), max_length=1024, default='bearer')

    @property
    def oauth_dict(self):
        return {
            "access_token": self.access_token,
            "consumer_key": self.consumer_key,
            "consumer_secret": self.consumer_secret,
            "refresh_token": self.refresh_token,
            "token_time": self.token_time,
            "token_type": self.token_type,
        }


class Year(BaseModel):
    def __str__(self):
        return "{}".format(self.name)

    name = models.CharField(_('Year Number'), max_length=4)


class YahooGame(BaseModel):
    """
    """
    def __str__(self):
        return "{} {}".format(self.code, str(self.year))

    code = models.CharField(
        _("Game Code"), max_length=128, default='mlb')

    year = models.ForeignKey(
        'leagues.Year', on_delete=models.CASCADE, verbose_name=_('Year'), null=True, blank=True)


class YahooLeague(RemoteObjectModelMixin, BaseModel):
    """
    """
    def __str__(self):
        return "{} {}".format(self.name, getattr(self.game.year, 'name', ''))

    children = [
        'weeks',
        'teams',
        'matchups'
    ]

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooLeagueRemote()

    game = models.ForeignKey(
        YahooGame, verbose_name=_('Yahoo Game'), on_delete=models.CASCADE,
        related_name='leagues', null=True)

    yahoo_credentials = models.ForeignKey(
        YahooOauthCredentials,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Oauth Credentials'),
        related_name='leagues', )

    is_active = models.BooleanField(_('Is Active'), default=False)
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    domain = models.CharField(
        _('Domain'), max_length=512, null=True, blank=True
    )

    name = models.CharField(
        _("League Name"), max_length=1024, blank=True, null=True)

    current_week = models.IntegerField(
        _('Current Week'), blank=True, null=True)

    draft_status = models.CharField(
        _("Draft Status"), max_length=1024, blank=True, null=True)

    num_teams = models.IntegerField(
        _('Number of Teams'), blank=True, null=True)

    league_type = models.CharField(
        _("League Type"), max_length=1024, blank=True, null=True)

    playoff_start_week = models.IntegerField(
        _('Playoff Start Week'), blank=True, null=True)

    stats = JSONField(_('Stats'), default=dict, null=True, blank=True)
    meta = JSONField(_('Meta'), default=dict, null=True, blank=True)

    def update_model_from_remote(self, **kwargs):
        if not 'id' in kwargs:
            kwargs['id'] = self.remote_id
        kwargs['league'] = self
        super().update_model_from_remote(**kwargs)
        self.update_children_model_from_remote(**kwargs)

    def update_children_model_from_remote(self, **kwargs):
        kwargs['remote_id'] = self.remote_id
        super().update_children_model_from_remote(**kwargs)

    def get_leagues(self):
        return self.remote_manager.get_leagues_repr(
            code=self.game.code, year=self.game.year.name)

    def update_players_from_remote(self, **kwargs):
        """
        model1.model2.model3.name = x
        geattr(model1, 'model2', object), 'name', x)
        :return: remote object
        """
        if not 'id' in kwargs:
            kwargs['id'] = self.remote_id
        kwargs['league'] = self
        self.remote_manager.set_credentials(
            kwargs['league'].get_yahoo_credentials()
        )

        from players.models import BaseballPlayer, YahooPlayerLeague
        limit = 25
        for status in ['T', 'A']:
            i = 0
            while True:
                players = self.remote_manager.get_players(
                    start=i, status=status, **kwargs)

                for player in players.values():
                    if not isinstance(player, dict):
                        continue
                    player_dict = {}
                    [player_dict.update(i) for i in  player['player'][0]]
                    if player_dict['name']['first']=='Omar':
                        print(player_dict)
                    bplayer, _ = BaseballPlayer.objects.update_or_create(
                        defaults=dict(
                            first_name=player_dict['name']['first'],
                            last_name=player_dict['name']['last'],
                            team=player_dict['editorial_team_full_name'],
                            eligible_positions=player_dict['eligible_positions'],
                        ),
                        remote_player_id=player_dict['player_id']
                    )
                i += limit
                print(i)
                if len(players)<limit:
                    break

    def get_yahoo_credentials(self):
        return self.yahoo_credentials

    @property
    def teams_order(self):
        teams = self.teams.order_by('-w_pct')
        return teams

    @property
    def matchups_order(self):
        matchups = self.matchups.filter(week__is_current_week=True)
        return matchups


class YahooMultiYearLeague(BaseModel):
    def __str__(self):
        return "{}".format(self.name)

    name = models.CharField(_('Name'), null=True, blank=True, max_length=64)
    leagues = models.ManyToManyField(
        'leagues.YahooLeague', verbose_name=_('Leagues')
    )
    is_active = models.BooleanField(_('Is Active'), default=True)
    domain = models.CharField(
        _('Domain'), max_length=512, null=True, blank=True)

    @property
    def teams_order(self):
        teams = self.teams.order_by('-w_pct')
        return teams

    @property
    def matchups_order(self):
        from results.models import YahooMatchup
        matchups = YahooMatchup.objects.filter(
            week__is_current_week=True, league__in=self.leagues.all()
        )
        return matchups


class YahooLeagueWeeks(RemoteObjectModelMixin, BaseModel):
    def __str__(self):
        return "{}".format(self.week_number)

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooWeeksRemote()

    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo Game'), on_delete=models.CASCADE,
        related_name='weeks')

    week_number = models.IntegerField(_('Week Number'), blank=True, null=True)

    start_date = models.DateField(_('Start Date'), blank=True, null=True)

    end_date = models.DateField(_('End Date'), blank=True, null=True)

    is_current_week = models.BooleanField(_('Is Current Week'), default=False)


class RotoMultiLeagues(BaseModel):
    name = models.CharField(
        max_length=1024, null=True, blank=True, verbose_name=_('Name')
    )
    leagues = models.ManyToManyField('leagues.YahooLeague')
    is_active = models.BooleanField(_('Is Active'), default=True)
    domain = models.CharField(
        _('Domain'), max_length=512, null=True, blank=True
    )

