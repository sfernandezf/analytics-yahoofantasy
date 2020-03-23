from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.game import Game

from core.mixins.remotes import YahooBaseRemoteObjectMixin
from core.utils import get_oauth


class YahooGameRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.attrs = {}
        self.children_map = {
            'leagues': 'get_leagues'
        }

    def get_remote_attrs(self, **kwargs):
        game = Game(get_oauth(), kwargs['code'])
        return super().get_remote_attrs(**kwargs)

    def get_leagues(self, **kwargs):
        game = Game(get_oauth(), kwargs['code'])
        return game.league_ids(kwargs['year'])



class YahooLeagueRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {
            'weeks': 'get_weeks',
            # 'teams': 'get_teams'

        }

    def get_remote_attrs(self, **kwargs):
        league = League(get_oauth(), kwargs['id'])
        settings = league.settings()
        self.attrs = {
            'id': kwargs['id'],
            'name': settings.get('name'),
            'current_week': settings.get('current_week'),
            'draft_status': settings.get('draft_status'),
            'num_teams': settings.get('num_teams'),
            'league_type': settings.get('league_type'),
            'playoff_start_week': settings.get('playoff_start_week')
        }
        return super().get_remote_attrs(**kwargs)
    
    def get_teams(self, **kwargs):
        league = League(get_oauth(), kwargs['id'])
        return league.teams()

    def get_weeks(self, **kwargs):
        league = League(get_oauth(), kwargs['id'])
        start_week = league.settings()['start_week']
        end_week = league.end_week()
        return ['%s_%s' % (kwargs['id'], i)
                for i in range(int(start_week), int(end_week))]


class YahooWeeksRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {}


    def get_remote_attrs(self, **kwargs):
        league = League(get_oauth(), kwargs['parent_id'])
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

