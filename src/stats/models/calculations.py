import logging
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)


class StatsCalculatorMixin(models.Model):
    positions = [
        {'name': 'C', 'count': 1, 'type': 'B'},
        {'name': 'SS', 'count': 1, 'type': 'B'},
        {'name': '2B', 'count': 1, 'type': 'B'},
        {'name': '3B', 'count': 1, 'type': 'B'},
        {'name': '1B', 'count': 1, 'type': 'B'},
        {'name': 'OF', 'count': 3, 'type': 'B'},
        {'name': 'Util', 'count': 2, 'type': 'B'},
        {'name': 'SP', 'count': 10, 'type': 'P'},
        {'name': 'RP', 'count': 10, 'type': 'P'},
    ]

    class Meta:
        abstract=True

    regular_player = JSONField(_('Regular Players'), default=dict, null=True, blank=True)
    is_regular_player_auto = models.BooleanField(_('Is auto'), default=True)
    bat_stat_order = models.CharField(_('Bat Stat Order'), max_length=512, null=True, blank=True)
    pit_stat_order = models.CharField(_('Pit Stat Order'), max_length=512, null=True, blank=True)

    def get_regular_player(self):
        sort_stat = '-player__auctionbaseballplayer__PTS'
        player_to_exclude = []
        player_list_position = {}
        position_rank = []
        for position in self.positions:
            count_player = len(self.yahoo_team.players.filter(
                player__eligible_positions__contains=[{"position": position['name']}])
            )
            position_rank.append(
                {
                    'name': position['name'],
                    'count_player': count_player/position['count'],
                    'count': position['count'],
                    'type': position['type']
                }
            )
        position_rank = sorted(position_rank, key=lambda pos: pos['count_player'])

        ip = 0
        pit_pct = 1
        for position in position_rank:
            position_pct = position['count']
            players = self.yahoo_team.players.filter(
                player__eligible_positions__contains=[{"position": position['name']}]
            ).exclude(id__in=player_to_exclude).order_by(sort_stat)

            if self.bat_stat_order and position['name'] not in ['RP', 'SP']:
                bat_stat_order = str(self.bat_stat_order).split(',')
                players_dict = {
                    player.player.calculate_value(*bat_stat_order): player
                    for player in players
                }
                players_dict = sorted(players_dict.items(), reverse=True)
                players = [player[1] for player in players_dict]

            for player in players:
                if position['name'] in ['RP', 'SP']:
                    if not hasattr(player.player, 'baseballavestats') or not player.player.baseballavestats.ip:
                        continue
                    player_pct = pit_pct
                    ip += player.player.baseballavestats.ip * 6 / 162
                    if ip >= 60:
                        pit_pct = 0
                else:
                    if player in player_list_position:
                        player_ave_pct = 1 - sum(
                            [pos['pct'] for pos in player_list_position[player]]
                        )
                    else:
                        player_ave_pct = 1
                    if not player.player.baseballavestats.g:
                        continue
                    player_time_pct = player_ave_pct * player.player.baseballavestats.g / 162
                    if (position_pct - player_time_pct) > 0:
                        player_pct = player_ave_pct
                        position_pct -= player_time_pct
                    else:
                        player_pct = position_pct
                        position_pct -= player_pct

                att = {
                    'position': position['name'],
                    'pct': player_pct,
                    'type': position['type']
                }
                if player in player_list_position:
                    player_list_position[player] += [att]
                else:
                    player_list_position[player] = [att]

                if position_pct == 0:
                    break
                else:
                    player_to_exclude.append(player.id)
        return player_list_position

    def get_general_stat(self, *args, **kwargs):
        total_stat = 0
        for player, atts in kwargs['players'].items():
            try:
                stat_value = getattr(
                    player.player.baseballavestats, kwargs['stat_name'], None
                )
            except:
                pass
            if not stat_value:
                continue
            player_pct = sum([att['pct'] for att in atts])
            total_stat += stat_value * player_pct

        if not total_stat or total_stat == 0:
            return None
        return round(total_stat, kwargs.get('round_value', 0)) if total_stat else total_stat

    def get_auction_stat(self, *args, **kwargs):
        total_stat = 0
        for player, atts in kwargs['players'].items():
            stat_value = None
            try:
                stat_value = getattr(
                    player.player.auctionbaseballplayer, kwargs['stat_name'], None
                )
            except:
                pass
            if not stat_value:
                continue
            player_pct = sum([att['pct'] for att in atts])
            total_stat += stat_value * player_pct

        if not total_stat or total_stat == 0:
            return None
        return round(total_stat, kwargs.get('round_value', 0)) if total_stat else total_stat

    def get_stat_ab(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)
    
    def get_stat_r(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_h(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_hr(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_rbi(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_bb(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_k(self, *args, **kwargs):
        kwargs['stat_name'] = 'so'
        return self.get_general_stat(*args, **kwargs)

    def get_stat_sv(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_hld(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_qs(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_avg(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ab = kwargs['ab']
        h = kwargs['h']
        if all((h, ab)):
            stat_value = round(h / ab, 3)
        return stat_value
    
    def get_stat_obp(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        bb = kwargs['bb']
        h = kwargs['h']
        hbp = self.get_general_stat(**kwargs, stat_name='hbp')
        pa = self.get_general_stat(**kwargs, stat_name='pa')
        if all((h, bb, hbp, pa)):
            stat_value = round((h + bb + hbp)/pa, 3)
        return stat_value

    def get_stat_slg(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ab = kwargs['ab']
        h = kwargs['h']
        hr = kwargs['hr']
        double = self.get_general_stat(**kwargs, stat_name='double')
        triple = self.get_general_stat(**kwargs, stat_name='triple')
        if all((ab, h, double, triple, hr)):
            stat_value = round((h + 2*double + 3*triple + 4*hr)/ab, 3)
        return stat_value

    def get_stat_ops(self, *args, **kwargs):
        stat_value = None
        if all((kwargs['obp'], kwargs['slg'])):
            stat_value = round(kwargs['obp'] + kwargs['slg'], 3)
        return stat_value

    def get_stat_nsb(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        sb = self.get_general_stat(**kwargs, stat_name='sb')
        cs = self.get_general_stat(**kwargs, stat_name='cs')
        if all((sb, cs)):
            stat_value = round(sb - cs, 0)
        return stat_value

    def get_stat_ip(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)

    def get_stat_era(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ip = kwargs['ip']
        er = self.get_general_stat(**kwargs, stat_name='er')
        if all((ip, er)):
            stat_value = round(er*9/ip, 2)
        return stat_value

    def get_stat_whip(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ip = kwargs['ip']
        ha = self.get_general_stat(**kwargs, stat_name='ha')
        bba = self.get_general_stat(**kwargs, stat_name='bba')
        if all((ip, ha, bba)):
            stat_value = round((bba + ha)/ip, 2)
        return stat_value

    def get_stat_kbb(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        soa = self.get_general_stat(**kwargs, stat_name='soa')
        bba = self.get_general_stat(**kwargs, stat_name='bba')
        if all((soa, bba)):
            stat_value = round(soa/bba, 2)
        return stat_value

    def get_stat_k9(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ip = kwargs['ip']
        soa = self.get_general_stat(**kwargs, stat_name='soa')
        if all((soa, ip)):
            stat_value = round(soa*9/ip, 2)
        return stat_value

    def get_stat_rapp(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        gap = self.get_general_stat(**kwargs, stat_name='gap')
        gs = self.get_general_stat(**kwargs, stat_name='gs')
        if all((gap, gs)):
            stat_value = round(gap - gs, 0)
        return stat_value

    def get_stat_h9(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ip = kwargs['ip']
        ha = self.get_general_stat(**kwargs, stat_name='ha')
        if all((ip, ha)):
            stat_value = round(ha*9/ip, 3)
        return stat_value

    def get_stat_bb9(self, *args, **kwargs):
        stat_value = None
        kwargs.pop('stat_name')
        ip = kwargs['ip']
        bba = self.get_general_stat(**kwargs, stat_name='bba')
        if all((ip, bba)):
            stat_value = round(bba*9/ip, 3)
        return stat_value

    def save(self, *args, **kwargs):
        stats = [
            'ab', 'r', 'h', 'hr', 'rbi', 'bb', 'k', 'avg', 'obp', 'slg', 'ops',
            'nsb', 'ip', 'era', 'whip', 'kbb', 'k9', 'rapp', 'h9', 'bb9', 'sv',
            'hld', 'qs'
        ]
        auction_stats = [
            'mR', 'mH', 'mHR', 'mRBI', 'mBB', 'mSO', 'mAVG', 'mOBP', 'mSLG',
            'mOPS', 'mSBCS',
            'mIP', 'mERA', 'mWHIP', 'mKBB', 'mK9', 'mBB9', 'mHLD', 'mQS',
            'mSVHLD', 'mSV', 'PTS'
        ]
        if self.is_regular_player_auto:
            players = self.get_regular_player()
            self.regular_player = {}
            for key, value in players.items():
                value = [str(key.id)] + value
                self.regular_player[str(key)] = value
        else:
            from players.models import BaseballPlayer, YahooPlayerLeague
            players = {}
            for key, value in self.regular_player.items():
                instance = YahooPlayerLeague.objects.get(id=value[0])
                players [instance] = value[1:]
        _kwargs = {
            'players': players
        }
        # print("{}".format(self.yahoo_team.name))
        for key, value in _kwargs['players'].items():
            for v in value:
                if v['type'] != 'B':
                    continue
                # print(
                #     "{} {} {}".format(
                #         str(key), v['position'], round(v['pct'] * 100, 0)
                #     )
                # )
        # print("-------------------------------")
        for stat in stats:
            if callable(getattr(self, 'get_stat_{}'.format(stat), None)):
                _kwargs['stat_name'] = stat
                ret = getattr(self, 'get_stat_{}'.format(stat))(**_kwargs)
                _kwargs[stat] = ret
                setattr(self, stat, ret)

        for stat in auction_stats:
            _kwargs['stat_name'] = stat
            ret = self.get_auction_stat(**_kwargs)
            _kwargs[stat] = ret
            setattr(self, stat, ret)

        return super().save(*args, **kwargs)
