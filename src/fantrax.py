from os import system, name
import time

import requests


MY_TEAM = 'yj4j8xe3kldz0qpd'

TEAMS = {
    'j8dozvzmkle5c103': {'name': 'Benito_Camela', 'id': 'j8dozvzmkle5c103','shortName': 'Benito_C', 'commissioner': False, 'capacity': 6},
    '3ahnujz7kle057fd': {'name': 'Citizen Cain','id': '3ahnujz7kle057fd','shortName': 'daguero', 'commissioner': False, 'capacity': 3},
    'isicls7fklbjgx8o': {'name': 'Cool Hand Lucas',  'id': 'isicls7fklbjgx8o', 'shortName': 'CHS', 'commissioner': True, 'capacity': 3},
    'yj4j8xe3kldz0qpd': {'name': 'Delray Beach Rays', 'id': 'yj4j8xe3kldz0qpd','shortName': 'sfernand', 'commissioner': True, 'capacity': 5},
    '16z1i4rbkle6q8pr': {'name': 'dsabas01','id': '16z1i4rbkle6q8pr','shortName': 'dsabas01', 'commissioner': False, 'capacity': 6},
    'h43ohgrgkldzvzgh': {'name': 'Han Soto: A Fantasy Wars Story', 'id': 'h43ohgrgkldzvzgh', 'shortName': ':3', 'commissioner': False, 'capacity': 3},
    'yhsntslukle0o41w': {'name': 'Havana Blues', 'id': 'yhsntslukle0o41w', 'shortName': 'BLU', 'commissioner': False, 'capacity': 3},
    'zs2oh3bqkle09a1q': {'name': 'Team davemarrod90','id': 'zs2oh3bqkle09a1q','shortName': 'davemarr', 'commissioner': False, 'capacity': 3},
    'dx4a807okle3km1l': {'name': 'Team mandymvp', 'id': 'dx4a807okle3km1l', 'shortName': 'mandymvp', 'commissioner': False, 'capacity': 3},
    'ekios2q5kldzuuyj': {'name': 'Team Manu_91', 'id': 'ekios2q5kldzuuyj', 'shortName': 'Manu_91', 'commissioner': False, 'capacity': 3},
    'f5y61lqbkldzuqqc': {'name': 'Team NicoGC', 'id': 'f5y61lqbkldzuqqc','shortName': 'NicoGC', 'commissioner': False, 'capacity': 3},
    '7rxfeeglkle06iwm': {'name': 'Team tomy85','id': '7rxfeeglkle06iwm', 'shortName': 'tomy85', 'commissioner': False, 'capacity': 3}
}

def get_pending_transaction():
    cookies = {
        '_ga': 'GA1.2.1665217220.1611180830',
        'uig': '11ilir1mkk5zgv4g',
        'uac': 'i0tuuf7tkk8l0dm0',
        'wl': '1',
        'FX_REM': 'c2Zlcm5hbmRlemY5MDoxOTI2Njk3OTgyOTkwOjc5MDBkYjNlMzk4NTdmNjU5ZTM4MmU4OWU0Nzg1MmUz',
        'usprivacy': '1---',
        '__gads': 'ID=098134eb174a39b5:T=1611338147:S=ALNI_MbHlnuf3xV6XHT-Qqm7ngz8BHImFw',
        '_fw_crm_v': 'c9c5db6d-7591-467f-832f-001dd77e5541',
        '__utmz': '221131663.1611369056.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '_gid': 'GA1.2.1954326896.1613526600',
        '__qca': 'P0-2134267959-1613533373544',
        'BAYEUX_BROWSER': '60k4no1xj8fg1afb',
        '__utmc': '221131663',
        'playwirePageViews': '56',
        'pwUID': '103089612579423',
        '__utma': '221131663.1665217220.1611180830.1613874837.1613936807.14',
        '_gat': '1',
        'GED_PLAYLIST_ACTIVITY': 'W3sidSI6IjRSTjMiLCJ0c2wiOjE2MTM5NDU3MDIsIm52IjowLCJ1cHQiOjE2MTM5MjA2NzUsImx0IjoxNjEzOTMzNjIwfSx7InUiOiJRN0YzIiwidHNsIjoxNjEzOTQ1Njk4LCJudiI6MCwidXB0IjoxNjEzODU2MDk3LCJsdCI6MTYxMzkzMzI5NH0seyJ1IjoiNjZQMiIsInRzbCI6MTYxMzk0NTY5NiwibnYiOjAsInVwdCI6MTYxMzg3Mzg4NCwibHQiOjE2MTM5MjA3NzZ9XQ..',
        'JSESSIONID': 'node0fpxx3ixmqgnt1qe8su874kibx515648.node0',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Content-Type': 'text/plain',
        'Origin': 'https://www.fantrax.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.fantrax.com/fantasy/league/nu9kee62klbjgwak/transactions/pending',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('leagueId', 'nu9kee62klbjgwak'),
    )

    data = '{"msgs":[{"method":"getPendingTransactions","data":{}},{"method":"getFantasyTeams","data":{}},{"method":"getFantasyLeagueInfo","data":{}},{"method":"getRefObject","data":{"type":"FantasyItemStatus"}}],"ng2":true,"href":"https://www.fantrax.com/fantasy/league/nu9kee62klbjgwak/transactions/pending","dt":1,"at":0,"av":null,"tz":"America/New_York","v":"19.3.1"}'

    response = requests.post('https://www.fantrax.com/fxpa/req', headers=headers, params=params, cookies=cookies, data=data)
    response = response.json()
    teams = {
        team['id']: dict(name=team['name'], shortname=['shortName'])
        for team in response['responses'][1]['data']['fantasyTeams']
    }
    bids = [
        dict(
            player=bid['scorer']['name'],
            teams=[
                teams[t]['name']
                for t in bid['cells'][0]['teamList']
            ],
            value=int(bid['cells'][0]['content'])
        )
        for bid in response['responses'][0]['data']['highBidTables'][0]['rows']
    ]

    bids = sorted(bids, key=lambda x: x['value'], reverse=True)
    _ = system('clear')
    # for bid in bids:
    #     print(bid['player'], bid['value'], bid['teams'])


def get_pending_transactions_all_teams():
    cookies = {
        '_ga': 'GA1.2.1665217220.1611180830',
        'uig': '11ilir1mkk5zgv4g',
        'uac': 'i0tuuf7tkk8l0dm0',
        'wl': '1',
        'FX_REM': 'c2Zlcm5hbmRlemY5MDoxOTI2Njk3OTgyOTkwOjc5MDBkYjNlMzk4NTdmNjU5ZTM4MmU4OWU0Nzg1MmUz',
        'usprivacy': '1---',
        '__gads': 'ID=098134eb174a39b5:T=1611338147:S=ALNI_MbHlnuf3xV6XHT-Qqm7ngz8BHImFw',
        '_fw_crm_v': 'c9c5db6d-7591-467f-832f-001dd77e5541',
        '__utmz': '221131663.1611369056.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '_gid': 'GA1.2.1954326896.1613526600',
        '__qca': 'P0-2134267959-1613533373544',
        'BAYEUX_BROWSER': '60k4no1xj8fg1afb',
        '__utmc': '221131663',
        'playwirePageViews': '63',
        '__utma': '221131663.1665217220.1611180830.1613956152.1614020300.18',
        'GED_PLAYLIST_ACTIVITY': 'W3sidSI6IjdHMjIiLCJ0c2wiOjE2MTQwMjYxMzksIm52IjoxLCJ1cHQiOjE2MTQwMjE1MjAsImx0IjoxNjE0MDI2MTM5fV0.',
        '_gat': '1',
        'JSESSIONID': 'node01tco3x64aqu06e0a1c2s39y41850425.node0',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Content-Type': 'text/plain',
        'Origin': 'https://www.fantrax.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.fantrax.com/fantasy/league/nu9kee62klbjgwak/transactions/pending/claim-drop?teamId=ALL_TEAMS',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('leagueId', 'nu9kee62klbjgwak'),
    )

    data = '{"msgs":[{"method":"getPendingTransactions","data":{"teamId":"ALL_TEAMS","txType":"CLAIM"}},{"method":"getFantasyTeams","data":{}},{"method":"getFantasyLeagueInfo","data":{}},{"method":"getRefObject","data":{"type":"FantasyItemStatus"}}],"ng2":true,"href":"https://www.fantrax.com/fantasy/league/nu9kee62klbjgwak/transactions/pending/claim-drop?teamId=ALL_TEAMS","dt":0,"at":0,"av":null,"tz":"America/New_York","v":"19.3.1"}'

    response = requests.post('https://www.fantrax.com/fxpa/req',
                             headers=headers, params=params, cookies=cookies,
                             data=data)
    response = response.json()

    players = {}
    teams = {}
    for team in response['responses'][0]['data']['tablesPerTeam']:
        teams[team['key']] = dict(
            team=TEAMS[team['key']], bids={}
        )
        for player in team['value'][0]['txSets']:
            id = player['claimScorer']['scorerId']
            if id in players:
                players[id]['bids'].append(
                    dict(bid=player['bid'], team=TEAMS[team['key']]),
                )
            else:
                players[id] = dict(
                    player=player['claimScorer'],
                    bids=[dict(bid=player['bid'], team=TEAMS[team['key']])]
                )

            teams[team['key']]['bids'][id] = dict(bid=player['bid'], team=TEAMS[team['key']])

    for _, player in players.items():
        if len(player['bids']) == 0:
            continue
        player['sorted_bids'] = sorted(
            player['bids'], key=lambda x: x['bid'], reverse=True
        )
        player['winning_bid'] = player['sorted_bids'][0]

    other_players = [
        'Anderson', 'Luzardo', 'Ketel',  'Conforto', 'Salvador', 'Olson',
        'Verdugo', 'Sano', 'Hosmer', 'Soroka', 'Sixto', 'Hayes', 'Riley',
        'Cesar',
    ]
    my_players = {}
    for k, v in players.items():
        # if k in teams[MY_TEAM]['bids'].keys():
        #     my_players[k] = v
        for n in other_players:
            if n in v['player']['name']:
                my_players[k] = v
                break

    _ = system('clear')
    for player in my_players.values():
        offer = [
            "{} {}".format(bid['bid'], bid['team']['name'])
            for bid in player['sorted_bids']
        ]
        status = (
            "Winnig"
            if player['winning_bid']['team']['name'] == TEAMS[MY_TEAM]['name']
            else "Losing"
        )
        print(
            player['player']['name'].strip(), status, "\n", "\n".join(offer), "\n"
        )


if __name__ == "__main__":
    _ = system('clear')
    while True:
        get_pending_transactions_all_teams()
        time.sleep(1)
