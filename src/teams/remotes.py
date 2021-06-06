from yahoo_fantasy_api.team import Team
from yahoo_fantasy_api.league import League

from core.mixins.remotes import YahooBaseRemoteObjectMixin, YahooAPITeam


class YahooTeamRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()
        self.children_map = {
            'players': 'get_players'
        }

    def get_remote_attrs(self, **kwargs):
        team = YahooAPITeam(self.get_oauth(), kwargs['id'])
        league = League(self.get_oauth(), team.league_id)
        team_atts = league.teams()[kwargs['id']]

        self.attrs = {
            'id': kwargs['id'],
            'name': team_atts.get('name'),
            'waiver_priority': team_atts.get('waiver_priority'),
            'manager_nickname': team_atts.get('managers')[0].get('manager', {}).get('nickname'),
            'manager_email': team_atts.get('managers')[0].get('manager', {}).get('email')
        }
        team_stat = team.stats()
        from stats.models import YahooStats
        stat_map = {
            i['yahoo_id']: i for i in YahooStats.league_stats
        }
        for stat in team_stat:
            stat_name = stat_map.get(int(stat['stat_id']))
            if not stat_name:
                continue
            try:
                self.attrs[stat_name['stat']] = float(stat['value'])
            except (ValueError, TypeError):
                continue

        return super().get_remote_attrs(**kwargs)

    def get_players(self, **kwargs):
        team = Team(self.get_oauth(), kwargs['id'])
        rosters = team.roster()
        players = [player['player_id'] for player in rosters]
        return players