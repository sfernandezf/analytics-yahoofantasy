
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseStats(models.Model):
    class Meta:
        abstract = True

    g = models.FloatField(_("Games"), blank=True, null=True)
    pa = models.FloatField(_("Plate Appareances"), blank=True, null=True)
    ab = models.FloatField(_("At Bat"), blank=True, null=True)
    h = models.FloatField(_("Hits"), blank=True, null=True)
    double = models.FloatField(_("Doubles"), blank=True, null=True)
    triple = models.FloatField(_("Triples"), blank=True, null=True)
    hr = models.FloatField(_("Home Run"), blank=True, null=True)
    r = models.FloatField(_("Runs"), blank=True, null=True)
    rbi = models.FloatField(_("Runs Bat in"), blank=True, null=True)
    bb = models.FloatField(_("Base Balls"), blank=True, null=True)
    so = models.FloatField(_("Strike Out"), blank=True, null=True)
    hbp = models.FloatField(_("Hit By Pitch"), blank=True, null=True)
    sb = models.FloatField(_("Stolen Base"), blank=True, null=True)
    cs = models.FloatField(_("Caught Stolen"), blank=True, null=True)
    avg = models.FloatField(_("Average"), blank=True, null=True)
    obp = models.FloatField(_("Obp"), blank=True, null=True)
    slg = models.FloatField(_("Slugging"), blank=True, null=True)
    ops = models.FloatField(_("OPS"), blank=True, null=True)
    woba = models.FloatField(_("wOBA"), blank=True, null=True)
    wrcplus = models.FloatField(_("wRC+"), blank=True, null=True)
    bsr = models.FloatField(_("BsR"), blank=True, null=True)
    fld = models.FloatField(_("Fld"), blank=True, null=True)
    off = models.FloatField(_("Off"), blank=True, null=True)
    _def = models.FloatField(_("Def"), blank=True, null=True)
    war = models.FloatField(_("WAR"), blank=True, null=True)
    gap = models.FloatField(_("Games as Pitcher"), blank=True, null=True)
    w = models.FloatField(_("Win"), blank=True, null=True)
    l = models.FloatField(_("Loses"), blank=True, null=True)
    era = models.FloatField(_("Earned Run Average"), blank=True, null=True)
    gs = models.FloatField(_("Game Started"), blank=True, null=True)
    ip = models.FloatField(_("Innings Pitched"), blank=True, null=True)
    ha = models.FloatField(_("Hits Allowed"), blank=True, null=True)
    er = models.FloatField(_("Earned Run"), blank=True, null=True)
    hra = models.FloatField(_("Home Run Allowed"), blank=True, null=True)
    soa = models.FloatField(_("Strike Out Allowed"), blank=True, null=True)
    bba = models.FloatField(_("Base Balls Allowed"), blank=True, null=True)
    whip = models.FloatField(_("WHIP"), blank=True, null=True)
    k9 = models.FloatField(_("Strike Out in 9 Inns"), blank=True, null=True)
    bb9 = models.FloatField(_("Base Balls in ( Inns"), blank=True, null=True)
    fip = models.FloatField(_("FIP"), blank=True, null=True)
    adp = models.FloatField(_("WAR"), blank=True, null=True)
    sv = models.FloatField(_("SV"), blank=True, null=True)
    hld = models.FloatField(_("SV"), blank=True, null=True)
    winp = models.FloatField(_("Winning Percentage"), blank=True, null=True)

    @property
    def stat_list(self):
        return ['g', 'pa', 'ab', 'h', 'double', 'triple', 'hr', 'r', 'rbi',
                'bb', 'so',  'hbp', 'sb', 'cs', 'avg', 'obp', 'slg', 'ops',
                'woba', 'wrcplus', 'bsr', 'fld', 'off', '_def', 'war', 'gap',
                'w', 'l', 'era', 'gs', 'ip', 'ha', 'er', 'hra', 'soa', 'bba',
                'whip', 'k9', 'bb9', 'fip', 'adp', 'sv', 'hld', 'winp']


class YahooStats(models.Model):
    class Meta:
        abstract = True

    # Batting
    gp = models.FloatField(_("Games Played"), blank=True, null=True)
    gs = models.FloatField(_("Games Started"), blank=True, null=True)
    avg = models.FloatField(_("Batting Average"), blank=True, null=True)
    obp = models.FloatField(_("On-base Percentage"), blank=True, null=True)
    slg = models.FloatField(_("Slugging Percentage"), blank=True, null=True)
    ab = models.FloatField(_("At Bats"), blank=True, null=True)
    r = models.FloatField(_("Runs"), blank=True, null=True)
    h = models.FloatField(_("Hits"), blank=True, null=True)
    single = models.FloatField(_("Singles"), blank=True, null=True)
    double = models.FloatField(_("Doubles"), blank=True, null=True)
    triple = models.FloatField(_("Triples"), blank=True, null=True)
    hr = models.FloatField(_("Home Runs"), blank=True, null=True)
    rbi = models.FloatField(_("Runs Batted In"), blank=True, null=True)
    sh = models.FloatField(_("Sacrifice Hits"), blank=True, null=True)
    sf = models.FloatField(_("Sacrifice Flys"), blank=True, null=True)
    sb = models.FloatField(_("Stolen Bases"), blank=True, null=True)
    cs = models.FloatField(_("Caught Stealing"), blank=True, null=True)
    so = models.FloatField(_("Strike Out"), blank=True, null=True)
    bb = models.FloatField(_("Walks"), blank=True, null=True)
    ibb = models.FloatField(_("Intentional Walks"), blank=True, null=True)
    hbp = models.FloatField(_("Hit By Pitch"), blank=True, null=True)
    k = models.FloatField(_("Strikeouts"), blank=True, null=True)
    gidp = models.FloatField(_("Ground Into Double Play"), blank=True, null=True)
    ops = models.FloatField(_("On-base + Slugging Percentage"), blank=True, null=True)
    tb = models.FloatField(_("Total Bases"), blank=True, null=True)
    po = models.FloatField(_("Put Outs"), blank=True, null=True)
    a = models.FloatField(_("Assists"), blank=True, null=True)
    e = models.FloatField(_("Errors"), blank=True, null=True)
    fpct = models.FloatField(_("Fielding Percentage"), blank=True, null=True)
    xbh = models.FloatField(_("Extra Base Hits"), blank=True, null=True)
    nsb = models.FloatField(_("Net Stolen Bases"), blank=True, null=True)
    sbp = models.FloatField(_("Stolen Base Percentage"), blank=True, null=True)
    cyc = models.FloatField(_("Hitting for the Cycle"), blank=True, null=True)
    pa = models.FloatField(_("Plate Appearances"), blank=True, null=True)
    slam = models.FloatField(_("Grand Slam Home Runs"), blank=True, null=True)
    ofa = models.FloatField(_("Outfield Assists"), blank=True, null=True)
    dpt = models.FloatField(_("Double Plays Turned"), blank=True, null=True)
    ci = models.FloatField(_("Catcher Interference"), blank=True, null=True)

    # Pitching
    app = models.FloatField(_("Appearances"), blank=True, null=True)
    era = models.FloatField(_("Earned Run Average"), blank=True, null=True)
    whip = models.FloatField(_("(Walks + Hits) / Innings Pitched"), blank=True, null=True)
    w = models.FloatField(_("Wins"), blank=True, null=True)
    l = models.FloatField(_("Losses"), blank=True, null=True)
    cg = models.FloatField(_("Completed Games"), blank=True, null=True)
    sho = models.FloatField(_("Shutouts"), blank=True, null=True)
    sv = models.FloatField(_("Saves"), blank=True, null=True)
    out = models.FloatField(_("Outs"), blank=True, null=True)
    ha = models.FloatField(_("Hits Allowed"), blank=True, null=True)
    tbf = models.FloatField(_("Total Batters Faced"), blank=True, null=True)
    ra = models.FloatField(_("Runs Allowed"), blank=True, null=True)
    er = models.FloatField(_("Earned Runs"), blank=True, null=True)
    hra = models.FloatField(_("Home Runs Allowed"), blank=True, null=True)
    bba = models.FloatField(_("Walks Allowed"), blank=True, null=True)
    ibba = models.FloatField(_("Intentional Walks Allowed"), blank=True, null=True)
    hbpa = models.FloatField(_("Hit Batters"), blank=True, null=True)
    ka = models.FloatField(_("Strikeouts Allowed"), blank=True, null=True)
    wp = models.FloatField(_("Wild Pitches"), blank=True, null=True)
    blk = models.FloatField(_("Balks"), blank=True, null=True)
    sba = models.FloatField(_("Stolen Bases Allowed"), blank=True, null=True)
    gidpa = models.FloatField(_("Batters Grounded Into Double Plays"), blank=True, null=True)
    svop = models.FloatField(_("Save Chances"), blank=True, null=True)
    hld = models.FloatField(_("Holds"), blank=True, null=True)
    k9 = models.FloatField(_("Strikeouts per Nine Innings"), blank=True,null=True)
    kbb = models.FloatField(_("Strikeout to Walk Ratio"), blank=True, null=True)
    tba = models.FloatField(_("Total Bases Allowed"), blank=True, null=True)
    ip = models.FloatField(_("Innings Pitched"), blank=True, null=True)
    pc = models.FloatField(_("Pitch Count"), blank=True, null=True)
    doublea = models.FloatField(_("Doubles Allowed"), blank=True, null=True)
    triplea = models.FloatField(_("Triples Allowed"), blank=True, null=True)
    rw = models.FloatField(_("Relief Wins"), blank=True, null=True)
    rl = models.FloatField(_("Relief Losses"), blank=True, null=True)
    pick = models.FloatField(_("Pickoffs"), blank=True,null=True)
    rapp = models.FloatField(_("Relief Appearances"), blank=True, null=True)
    obpa = models.FloatField(_("On-base Percentage Against"), blank=True, null=True)
    winp = models.FloatField(_("Winning Percentage"), blank=True, null=True)
    singlea = models.FloatField(_("Singles Allowed"), blank=True, null=True)
    h9 = models.FloatField(_("Hits Per Nine Innings"), blank=True, null=True)
    bb9 = models.FloatField(_("Walks Per Nine Innings"), blank=True, null=True)
    nh = models.FloatField(_("No Hitters"), blank=True, null=True)
    pg = models.FloatField(_("Perfect Games"), blank=True, null=True)
    svp = models.FloatField(_("Save Percentage"), blank=True,null=True)
    ira = models.FloatField(_("Inherited Runners Scored"), blank=True, null=True)
    qs = models.FloatField(_("Quality Starts"), blank=True, null=True)
    bsv = models.FloatField(_("Blown Saves"), blank=True, null=True)
    nsv = models.FloatField(_("Net Saves"), blank=True, null=True)
    nsvh = models.FloatField(_("Net Saves or Holds"), blank=True, null=True)

    @property
    def stat_list(self):
        return ['gp', 'gs', 'avg', 'obp', 'lg', 'ab', 'r', 'h', 'single', 'double',
                'triple', 'hr', 'rbi', 'sh', 'sf', 'sb', 'cs', 'bb', 'ibb', 'hbp',
                'k', 'gidp', 'ops', 'tb', 'po', 'a', 'e', 'fpct', 'xbh', 'nsb',
                'sbp', 'cyc', 'pa', 'slam', 'ofa', 'dpt', 'ci', 'app', 'era',
                'whip', 'w', 'l', 'cg', 'sho', 'sv', 'out', 'ha', 'tbf', 'ra',
                'er', 'hra', 'bba', 'ibba', 'hbpa', 'ka', 'wp', 'blk', 'sba',
                'gidpa', 'svop', 'hld', 'k9', 'kbb', 'tba', 'ip', 'pc', 'doublea',
                'triplea', 'rw', 'rl', 'pick', 'rapp', 'obpa', 'winp', 'singlea',
                'h9', 'bb9', 'nh', 'pg', 'svp', 'ira', 'qs', 'bsv', 'nsv', 'so']

    league_stats = [
        {
            'stat': 'r',
            'names': ['R'],
            'yahoo_id': 7,
            'comparator': '>'
        },
        {
            'stat': 'h',
            'names': ['H'],
            'yahoo_id': 8,
            'comparator': '>'
        },
        {
            'stat': 'hr',
            'names': ['HR'],
            'yahoo_id': 12,
            'comparator': '>'
        },
        {
            'stat': 'rbi',
            'names': ['RBI'],
            'yahoo_id': 13,
            'comparator': '>'
        },
        {
            'stat': 'bb',
            'names': ['BB'],
            'yahoo_id': 18,
            'comparator': '>'
        },
        {
            'stat': 'so',
            'names': ['K'],
            'yahoo_id': 21,
            'comparator': '<'
        },
        {
            'stat': 'avg',
            'names': ['AVG'],
            'yahoo_id': 3,
            'comparator': '>'
        },
        {
            'stat': 'obp',
            'names': ['OBP'],
            'yahoo_id': 4,
            'comparator': '>'
        },
        {
            'stat': 'slg',
            'names': ['SLG'],
            'yahoo_id': 5,
            'comparator': '>'
        },
        {
            'stat': 'ops',
            'names': ['OPS'],
            'yahoo_id': 55,
            'comparator': '>'
        },
        {
            'stat': 'nsb',
            'names': ['NSB'],
            'yahoo_id': 62,
            'comparator': '>'
        },
        {
            'stat': 'ip',
            'names': ['IP'],
            'yahoo_id': 50,
            'comparator': '>'
        },
        {
            'stat': 'era',
            'names': ['ERA'],
            'yahoo_id': 26,
            'comparator': '<'
        },
        {
            'stat': 'whip',
            'names': ['WHIP'],
            'yahoo_id': 27,
            'comparator': '<'
        },
        {
            'stat': 'kbb',
            'names': ['K/BB'],
            'yahoo_id': 56,
            'comparator': '>'
        },
        {
            'stat': 'k9',
            'names': ['K/9'],
            'yahoo_id': 57,
            'comparator': '>'
        },
        {
            'stat': 'rapp',
            'names': ['RAPP'],
            'yahoo_id': 73,
            'comparator': '>'
        },
        {
            'stat': 'h9',
            'names': ['H/9'],
            'yahoo_id': 77,
            'comparator': '<'
        },
        {
            'stat': 'bb9',
            'names': ['BB/9'],
            'yahoo_id': 78,
            'comparator': '<'
        },
        {
            'stat': 'qs',
            'names': ['QS'],
            'yahoo_id': 83,
            'comparator': '>'
        },
        {
            'stat': 'nsv',
            'names': ['NSV'],
            'yahoo_id': 85,
            'comparator': '>'
        },
        {
            'stat': 'nsvh',
            'names': ['NSVH'],
            'yahoo_id': 90,
            'comparator': '>'
        },
        {
            'stat': 'pa',
            'names': ['PA'],
            'yahoo_id': 65,
            'comparator': '>'
        },
        {
            'stat': 'winp',
            'names': ['WIN%'],
            'yahoo_id': 75,
            'comparator': '>'
        }
    ]


class AuctionStats(models.Model):
    class Meta:
        abstract = True

    mAVG = models.FloatField(_("mAVG"), blank=True, null=True)
    mRBI = models.FloatField(_("mRBI"), blank=True, null=True)
    mR = models.FloatField(_("mR"), blank=True, null=True)
    mHR = models.FloatField(_("mHR"), blank=True, null=True)
    mOBP = models.FloatField(_("mOBP"), blank=True, null=True)
    mSLG = models.FloatField(_("mSLG"), blank=True, null=True)
    mOPS = models.FloatField(_("mOPS"), blank=True, null=True)
    mH = models.FloatField(_("mH"), blank=True, null=True)
    mSO = models.FloatField(_("mSO"), blank=True, null=True)
    mBB = models.FloatField(_("mBB"), blank=True, null=True)
    mSBCS = models.FloatField(_("mSBCS"), blank=True, null=True)
    mSV = models.FloatField(_("mSV"), blank=True, null=True)
    mERA = models.FloatField(_("mERA"), blank=True, null=True)
    mWHIP = models.FloatField(_("mWHIP"), blank=True, null=True)
    mK9 = models.FloatField(_("mK9"), blank=True, null=True)
    mBB9 = models.FloatField(_("mBB9"), blank=True, null=True)
    mKBB = models.FloatField(_("mKBB"), blank=True, null=True)
    mIP = models.FloatField(_("mIP"), blank=True, null=True)
    mHLD = models.FloatField(_("mHLD"), blank=True, null=True)
    mQS = models.FloatField(_("mQS"), blank=True, null=True)
    mSVHLD = models.FloatField(_("mSVHLD"), blank=True, null=True)

    PTS = models.FloatField(_("PTS"), blank=True, null=True)
    aPOS = models.FloatField(_("aPOS"), blank=True, null=True)
    Dollars = models.FloatField(_("Dollars"), blank=True, null=True)