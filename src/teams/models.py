from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.models import BaseModel, RemoteObjectModelMixin, BaseStats
from leagues.models import YahooLeague
from teams.remotes import YahooTeamRemote


class YahooTeam(RemoteObjectModelMixin, BaseModel, BaseStats):
    """
    """
    def __str__(self):
        return "{}".format(self.name)

    children = ['players']

    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = YahooTeamRemote()

    name = models.CharField(
        _("Team Name"), max_length=1024, blank=True, null=True)

    league = models.ForeignKey(
        YahooLeague, verbose_name=_('Yahoo League'), on_delete=models.CASCADE,
        related_name='teams')

    waiver_priority = models.CharField(
        _('Waiver Priority'), max_length=1024, blank=True, null=True)

    manager_nickname = models.CharField(
        _("Manager Nickname"), max_length=1024, blank=True, null=True)

    manager_email = models.CharField(
        _("Manager Email"), max_length=1024, blank=True, null=True)

    def update_model_from_remote(self, **kwargs):
        if not 'id' in kwargs:
            kwargs['id'] = self.remote_id
        super().update_model_from_remote(**kwargs)
        self.update_children_model_from_remote(**kwargs)

    def update_children_model_from_remote(self, **kwargs):
        kwargs['remote_id'] = self.remote_id
        super().update_children_model_from_remote(**kwargs)

    nsb = models.FloatField(_("Net Stolen Base"), blank=True, null=True)
    kbb = models.FloatField(_("K/BB"), blank=True, null=True)
    rapp = models.FloatField(_("RAPP"), blank=True, null=True)
    h9 = models.FloatField(_("H/9"), blank=True, null=True)

    def save(self, *args, **kwargs):
        player_hits = []
        player_hrs = []
        player_rs = []
        player_rbis = []
        player_bbs = []
        player_ks = []
        player_avgs = []
        player_obps = []
        player_slgs = []
        player_opss = []
        player_nsbs = []
        player_ips = []
        player_eras = []
        player_whips = []
        player_k9s = []
        player_kbbs = []
        player_rapps = []
        player_bb9s = []
        player_h9s = []
        player_qss = []
        player_nsvs = []
        player_nsvhs = []

        for player in self.players.all():
            if isinstance(getattr(player.baseball_player, 'zipsstats'), object):
                if player.baseball_player.zipsstats.h:
                    player_hits.append(player.baseball_player.zipsstats.h)
                if player.baseball_player.zipsstats.hr:
                    player_hrs.append(player.baseball_player.zipsstats.hr)
                if player.baseball_player.zipsstats.r:
                    player_rs.append(player.baseball_player.zipsstats.r)
                if player.baseball_player.zipsstats.rbi:
                    player_rbis.append(player.baseball_player.zipsstats.rbi)
                if player.baseball_player.zipsstats.bb:
                    player_bbs.append(player.baseball_player.zipsstats.bb)
                if player.baseball_player.zipsstats.so:
                    player_ks.append(player.baseball_player.zipsstats.so)
                if player.baseball_player.zipsstats.avg:
                    player_avgs.append(player.baseball_player.zipsstats.avg)
                if player.baseball_player.zipsstats.obp:
                    player_obps.append(player.baseball_player.zipsstats.obp)
                if player.baseball_player.zipsstats.slg:
                    player_slgs.append(player.baseball_player.zipsstats.slg)
                if player.baseball_player.zipsstats.ops:
                    player_opss.append(player.baseball_player.zipsstats.ops)
                if player.baseball_player.zipsstats.sb and player.baseball_player.zipsstats.cs:
                    player_nsbs.append(player.baseball_player.zipsstats.sb-player.baseball_player.zipsstats.cs)
                if player.baseball_player.zipsstats.ip:
                    player_ips.append(player.baseball_player.zipsstats.ip)
                if player.baseball_player.zipsstats.era:
                    player_eras.append(player.baseball_player.zipsstats.era)
                if player.baseball_player.zipsstats.whip:
                    player_whips.append(player.baseball_player.zipsstats.whip)
                if player.baseball_player.zipsstats.k9:
                    player_k9s.append(player.baseball_player.zipsstats.k9)
                if player.baseball_player.zipsstats.soa and player.baseball_player.zipsstats.bba:
                    player_kbbs.append(player.baseball_player.zipsstats.soa/player.baseball_player.zipsstats.bba)
                if player.baseball_player.zipsstats.g and player.baseball_player.zipsstats.gs:
                    player_rapps.append(
                        player.baseball_player.zipsstats.g - player.baseball_player.zipsstats.gs)
                if player.baseball_player.zipsstats.bb9:
                    player_bb9s.append(player.baseball_player.zipsstats.bb9)
                if player.baseball_player.zipsstats.ha and player.baseball_player.zipsstats.ip:
                    player_h9s.append(
                        player.baseball_player.zipsstats.ha * 9 / player.baseball_player.zipsstats.ip)

        self.h = round(sum(player_hits)/len(player_hits)) if len(player_hits)>0 else None
        self.hr = round(sum(player_hrs) / len(player_hrs)) if len(player_hrs) > 0 else None
        self.r = round(sum(player_rs) / len(player_rs)) if len(player_rs) > 0 else None
        self.rbi = round(sum(player_rbis) / len(player_rbis)) if len(player_hrs) > 0 else None
        self.bb = round(sum(player_bbs) / len(player_bbs)) if len(player_bbs) > 0 else None
        self.so = round(sum(player_ks) / len(player_ks)) if len(player_ks) > 0 else None
        self.avg = round(sum(player_avgs) / len(player_avgs), 3) if len(player_avgs) > 0 else None
        self.obp = round(sum(player_obps) / len(player_obps), 3) if len(player_obps) > 0 else None
        self.slg = round(sum(player_slgs) / len(player_slgs), 3) if len(player_slgs) > 0 else None
        self.ops = round(sum(player_opss) / len(player_opss), 3) if len(player_opss) > 0 else None
        self.nsb = round(sum(player_nsbs) / len(player_nsbs)) if len(player_nsbs) > 0 else None
        self.ip = round(sum(player_ips) / len(player_ips)) if len(player_ips) > 0 else None
        self.era = round(sum(player_eras) / len(player_eras), 2) if len(player_eras) > 0 else None
        self.whip = round(sum(player_whips) / len(player_whips), 2) if len(player_whips) > 0 else None
        self.k9 = round(sum(player_k9s) / len(player_k9s), 2) if len(player_k9s) > 0 else None
        self.kbb = round(sum(player_kbbs) / len(player_kbbs), 2) if len(player_kbbs) > 0 else None
        self.rapp = round(sum(player_rapps) / len(player_rapps)) if len(player_rapps) > 0 else None
        self.bb9 = round(sum(player_bb9s) / len(player_bb9s), 2) if len(player_bb9s) > 0 else None
        self.h9 = round(sum(player_h9s) / len(player_h9s), 2) if len(player_h9s) > 0 else None
        super().save(*args, **kwargs)


