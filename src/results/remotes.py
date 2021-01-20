from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.game import Game

from core.mixins.remotes import YahooBaseRemoteObjectMixin
from leagues.remotes import YahooAPILeague


class YahooMatchupsRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {}

    def get_remote_attrs(self, **kwargs):
        league = YahooAPILeague(self.get_oauth(), kwargs['parent_id'])
        matchups = league.matchups(kwargs['id'])
        self.attrs = []
        matchups = matchups['fantasy_content']['league'][1]['scoreboard']['0'].get('matchups')
        for key, data in matchups.items():
            if not isinstance(data, dict):
                continue

            home_team = data['matchup']['0']['teams']['0']['team'][0][0]['team_key']
            visitor_team = data['matchup']['0']['teams']['1']['team'][0][0]['team_key']
            home_win, home_loss, visitor_win, visitor_loss, draws = 0, 0, 0, 0, 0
            for stat in data['matchup'].get('stat_winners', []):
                if not 'stat_winner' in stat:
                    continue
                if stat['stat_winner'].get('is_tied') == 1:
                    draws +=1
                elif stat['stat_winner'].get('winner_team_key') == home_team:
                    home_win += 1
                    visitor_loss += 1
                elif stat['stat_winner'].get('winner_team_key') == visitor_team:
                    visitor_win += 1
                    home_loss += 1

            self.attrs.append({
                'remote_id': kwargs['id'],
                'home_team': home_team,
                'visitor_team': visitor_team,
                'home_team_stats': {
                   stat['stat']['stat_id']: stat['stat']['value']
                    for stat in data['matchup']['0']['teams']['0']['team'][1]['team_stats']['stats']
                },
                'visitor_team_stats': {
                    stat['stat']['stat_id']: stat['stat']['value']
                    for stat in data['matchup']['0']['teams']['1']['team'][1]['team_stats']['stats']
                },
                'week': int(data['matchup']['week']),
                'home_win': home_win,
                'home_loss': home_loss,
                'home_draw': draws,
                'visitor_win': visitor_win,
                'visitor_loss': visitor_loss,
                'visitor_draw': draws,
            })

        return super().get_remote_attrs(**kwargs)
