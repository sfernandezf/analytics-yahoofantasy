from django.db import models


class StatsCalculatorMixin(models.Model):
    positions = [
        {'name': 'C', 'count': 1, 'type': 'B'},
        {'name': 'SS', 'count': 1, 'type': 'B'},
        {'name': '2B', 'count': 1, 'type': 'B'},
        {'name': '3B', 'count': 1, 'type': 'B'},
        {'name': '1B', 'count': 1, 'type': 'B'},
        {'name': 'OF', 'count': 3, 'type': 'B'},
        {'name': 'Util', 'count': 2, 'type': 'B'},
        {'name': 'RP', 'count': 10, 'type': 'P'},
        {'name': 'SP', 'count': 10, 'type': 'P'}
    ]

    class Meta:
        abstract=True

    def get_regular_player(self):
        player_to_exclude = []
        player_list_position = {}

        position_rank = []
        for position in self.positions:
            count_player = len(self.players\
                .filter(
                eligible_positions__contains=[{"position": position['name']}]))
            position_rank.append(
                {
                    'name': position['name'],
                    'count_player': count_player/position['count'],
                    'count': position['count'],
                    'type': position['type']
                }
            )
        position_rank = sorted(position_rank, key=lambda pos: pos['count_player'])

        for position in position_rank:
            position_pct = position['count']
            players = self.players \
                .filter(
                eligible_positions__contains=[{"position": position['name']}]) \
                .exclude(id__in=player_to_exclude) \
                .order_by('baseball_player__baseballavestats__adp')
            for player in players:
                if position['name'] in ['RP', 'SP']:
                    player_pct = 1
                else:
                    if player in player_list_position:
                        player_ave_pct = 1 - sum([pos['pct'] for pos in
                                                  player_list_position[player]])
                    else:
                        player_ave_pct = 1
                    player_time_pct = player_ave_pct * player.baseball_player.baseballavestats.g / 180
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
                stat_value = getattr(player.baseball_player.baseballavestats, kwargs['stat_name'], None)
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

    def get_stat_so(self, *args, **kwargs):
        return self.get_general_stat(*args, **kwargs)
    
    def get_stat_avg(self, *args, **kwargs):
        stat_value = None
        if kwargs['h'] and kwargs['ab']:
            stat_value = round(kwargs['h']/kwargs['ab'], 3)
        return stat_value

    def save(self, *args, **kwargs):
        stats = ['ab', 'r', 'h', 'hr', 'rbi', 'bb', 'so', 'nsb', 'avg']
        _kwargs = {
            'players': self.get_regular_player()
        }
        for stat in stats:
            if callable(getattr(self, 'get_stat_{}'.format(stat), None)):
                _kwargs['stat_name'] = stat
                ret = getattr(self, 'get_stat_{}'.format(stat))(**_kwargs)
                _kwargs[stat] = ret
                setattr(self, stat, ret)
        return super().save(*args, **kwargs)
