import logging
from django.conf import settings

from yahoo_oauth import OAuth2
from yahoo_fantasy_api.yhandler import YHandler
from yahoo_fantasy_api.league import League
from yahoo_fantasy_api.team import Team, objectpath


logger = logging.getLogger(__name__)


class CustomOauth(OAuth2):
    pass


class BaseRemoteObjectMixin:
    credentials_cache = {}

    def __init__(self, **kwargs):
        self.fields = []
        self.attrs = {}
        self.children_map = {}
        self.credentials = kwargs.get('credentials')

    def get_remote_attrs(self, **kwargs):
        return self.attrs

    def update(self, **kwargs):
        raise NotImplementedError

    def get_children(self, child, **kwargs):
        if not child in self.children_map:
            return []
        
        return getattr(self, self.children_map[child])(**kwargs)

    def set_credentials(self, value):
        self.credentials = value
        

class YahooBaseRemoteObjectMixin(BaseRemoteObjectMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields = ['id', 'name']

    def get_oauth(self):
        if not self.credentials:
            return None

        oauth = self.credentials_cache.get(str(self.credentials.id))

        if oauth and oauth.token_is_valid():
            return oauth

        if not oauth:
            oauth = CustomOauth(**self.credentials.oauth_dict)

        if not oauth.token_is_valid():
            oauth.refresh_access_token()

        self.credentials_cache[str(self.credentials.id)] = oauth
        return oauth


class CustomYhandler(YHandler):
    def get_team_stats_raw(self, team_id):
        """Return the raw JSON when requesting standings for a league.

        :param league_id: League ID to get the standings for
        :type league_id: str
        :return: JSON document of the request.
        """
        return self.get("team/{}/stats;type=season".format(team_id))


class YahooAPITeam(Team):
    def __init__(self, sc, team_key):
        super().__init__(sc, team_key)
        self.yhandler = CustomYhandler(sc)

    def stats(self):
        """Return the team roster for a given week or date
        """
        t = objectpath.Tree(self.yhandler.get_team_stats_raw(self.team_key))
        it = t.execute('''$..(stat_id,value)''')

        stats = []
        try:
            while True:
                stat_dict = next(it)
                if not 'stat_id' in stat_dict:
                    continue
                stats.append(
                    {
                        "stat_id": stat_dict["stat_id"],
                        "value": stat_dict["value"]
                    }
                )
        except StopIteration:
            pass
        return stats


class YahooAPILeague(League):
    def matchups(self, week=None):
        """Retrieve matchups data for current week

        :return: Matchup details as key/value pairs
        :rtype: dict
        """
        json = self.yhandler.get_scoreboard_raw(self.league_id, week)
        return json

    def settings(self):
        """Return the league settings

        :return: League settings as key/value pairs
        :rtype: Dict
        """""
        if self.settings_cache is None:
            json = self.yhandler.get_settings_raw(self.league_id)
            data = {}
            if "fantasy_content" in json:
                content = json["fantasy_content"]
                if "league" in content:
                    self._merge_dicts(data, content["league"][0], [])
                    # Filtering out 'roster_positions' and 'stat_categories'
                    # because they can be found in other APIs.
                    self._merge_dicts(data,
                                      content["league"][1]["settings"][0],
                                      ["roster_positions"])
            self.settings_cache = data
        return self.settings_cache
