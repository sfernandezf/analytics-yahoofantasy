from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.game import Game

from core.mixins.remotes import YahooBaseRemoteObjectMixin
from core.utils import get_oauth
from leagues.remotes import YahooAPILeague


class YahooMatchupsRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {}

    def get_remote_attrs(self, **kwargs):
        league = YahooAPILeague(get_oauth(), kwargs['parent_id'])
        matchups = league.matchups(kwargs['id'])
        self.attrs = []
        matchups = matchups['fantasy_content']['league'][1]['scoreboard']['0'].get('matchups')
        for key, data in matchups.items():
            if not isinstance(data, dict):
                continue
            self.attrs.append( {
                'home_team': data['matchup']['0']['teams']['0']['team'][0][0]['team_key'],
                'visitor_team': data['matchup']['0']['teams']['1']['team'][0][0]['team_key'],
                'week': int(data['matchup']['week'])
            })
        return super().get_remote_attrs(**kwargs)
