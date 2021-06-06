from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.game import Game
from yahoo_fantasy_api.team import Team, objectpath
from yahoo_fantasy_api.yhandler import YHandler

from core.mixins.remotes import YahooBaseRemoteObjectMixin, YahooAPILeague


class YahooLeagueRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {
            'weeks': 'get_weeks',
            'teams': 'get_teams',
            'matchups': 'get_matchups'
        }

    def get_remote_attrs(self, **kwargs):
        league = YahooAPILeague(self.get_oauth(), kwargs['id'])
        # stats = league.player_stats(['10027'], req_type='season')
        settings = league.settings()
        stats = [
            {
                'id': value['stat']['stat_id'],
                'name': value['stat']['display_name'],
            }
            for value in settings['stat_categories']['stats']
            if value['stat'].get('is_only_display_stat') != '1'
        ]
        self.attrs = {
            'id': kwargs['id'],
            'name': settings.get('name'),
            'current_week': settings.get('current_week'),
            'draft_status': settings.get('draft_status'),
            'num_teams': settings.get('num_teams'),
            'league_type': settings.get('league_type'),
            'playoff_start_week': settings.get('playoff_start_week'),
            'stats': stats
        }
        return super().get_remote_attrs(**kwargs)
    
    def get_teams(self, **kwargs):
        league = League(self.get_oauth(), kwargs['id'])
        return league.teams()

    def get_players(self, **kwargs):
        league = League(self.get_oauth(), kwargs['id'])
        json = league.yhandler.get_players_raw(
            kwargs['id'], start=kwargs['start'], status=kwargs['status'])

        return json['fantasy_content']['league'][1]['players']

    def get_weeks(self, **kwargs):
        league = League(self.get_oauth(), kwargs['id'])
        start_week = league.settings()['start_week']
        end_week = league.end_week()
        return [
            '%s_%s' % (kwargs['id'], i)
            for i in range(int(start_week), int(end_week) + 1)
        ]

    def get_matchups(self, **kwargs):
        league = League(self.get_oauth(), kwargs['id'])
        start_week = league.settings()['start_week']
        end_week = league.end_week()
        return list(range(int(start_week), int(end_week)))

    def get_leagues_repr(self, **kwargs):
        game = Game(self.get_oauth(), kwargs['code'])
        league_ids = game.league_ids(kwargs['year'])
        leagues = []
        for id in league_ids:
            league = League(self.get_oauth(), id)
            league = league.settings()
            leagues.append(
                {
                    'id': league['league_key'],
                    'name': league['name']
                }
            )
        return leagues




class YahooWeeksRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {}


    def get_remote_attrs(self, **kwargs):
        league = League(self.get_oauth(), kwargs['parent_id'])
        week_number = int(str(kwargs['id']).split('_')[1])
        current_week = int(league.current_week())
        try:
            date_range = league.week_date_range(week_number)
        except:
            date_range = None
        self.attrs = {
            'id': kwargs['id'],
            'week_number': week_number,
            'start_date': date_range[0] if isinstance(date_range, tuple) else None,
            'end_date': date_range[1] if isinstance(date_range, tuple) else None,
            'is_current_week': week_number == current_week
        }
        return super().get_remote_attrs(**kwargs)


