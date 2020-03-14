from yahoo_fantasy_api.team import Team
from yahoo_fantasy_api.league import League

from core.mixins.remotes import YahooBaseRemoteObjectMixin
from core.utils import get_oauth


class YahooPlayerRemote(YahooBaseRemoteObjectMixin):
    def __init__(self):
        super().__init__()

    def get_remote_attrs(self, **kwargs):
        team_id = getattr(kwargs.get('team', object), 'remote_id', None)
        team = Team(get_oauth(), team_id)
        league = League(get_oauth(), team.league_id)
        player_atts = league.player_details(kwargs['id'])[0]
        self.attrs = {
            'id': kwargs['id'],
            'first_name': player_atts.get('name', {}).get('first'),
            'last_name': player_atts.get('name', {}).get('last'),
            'editorial_team_full_name': player_atts.get('editorial_team_full_name'),
            'eligible_positions': player_atts.get('eligible_positions'),
        }
        return super().get_remote_attrs(**kwargs)

