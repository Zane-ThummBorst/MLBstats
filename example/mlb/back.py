import statsapi as sa
import json

alphabet = 'abcdefghijklmnopqrstuvwxyz'
abbreviations = {
    "gamesPlayed": "GP",
    "groundOuts": "GO",
    "airOuts": "AO",
    "runs": "R",
    "doubles": "2B",
    "triples": "3B",
    "homeRuns": "HR",
    "strikeOuts": "SO",
    "baseOnBalls": "BB",
    "intentionalWalks": "IW",
    "hits": "H",
    "hitByPitch": "HBP",
    "avg": "AVG",
    "atBats": "AB",
    "obp": "OBP",
    "slg": "SLG",
    "ops": "OPS",
    "caughtStealing": "CS",
    "stolenBases": "SB",
    "stolenBasePercentage": "SBP",
    "groundIntoDoublePlay": "GIDP",
    "numberOfPitches": "NOP",
    "plateAppearances": "PA",
    "totalBases": "TB",
    "rbi": "RBI",
    "leftOnBases": "LOB",
    "sacBunts": "SAC",
    "sacFlies": "SF",
    "babip": "BABIP",
    "groundOutsToAirOuts": "GO/AO",
    "catchersInterference": "CI",
    "atBatsPerHomeRun": "AB/HR"
}
abbreviationsP = dict(gamesPlayed='GP', gamesStarted='GS', groundOuts='GO', airOuts='AO', runs='R', doubles='2B',
                      triples='3B', homeRuns='HR', strikeOuts='SO', baseOnBalls='BB', intentionalWalks='IW', hits='H',
                      hitByPitch='HBP', avg='AVG', atBats='AB', obp='OBP', slg='SLG', ops='OPS', caughtStealing='CS',
                      stolenBases='SB', stolenBasePercentage='SBP', groundIntoDoublePlay='GIDP', numberOfPitches='NOP',
                      era='ERA', inningsPitched='IP', wins='W', losses='L', saves='S', saveOpportunities='SO',
                      holds='H', blownSaves='BS', earnedRuns='ER', whip='WHIP', battersFaced='BF', outs='O',
                      gamesPitched='GP', completeGames='CG', shutouts='ShO', strikes='TS', strikePercentage='SP',
                      hitBatsmen='HB', balks='BK', wildPitches='WP', pickoffs='P', totalBases='TB',
                      groundOutsToAirouts='GOTA', winPercentage='WP', pitchesPerInning='PPI', gamesFinished='GF',
                      strikeoutWalkRatio='SWR', strikeoutsPer9Inn='K/9', walksPer9Inn='W/9', hitsPer9Inn='H/9',
                      runsScoredPer9='R/9', homeRunsPer9='HR/9', inheritedRunners='IR', inheritedRunnersScored='IRS',
                      catchersInterference='CI', sacBunts='SB', sacFlies='SF')



# Hitting stats
def playerInfo(name):
    # Think about an edge case where there are two players with the same name????
    for player in sa.lookup_player(name):
        d = sa.player_stat_data(player.get('id'), 'hitting', 'season')
        d = d.get('stats')
        stats = d[0].get('stats')
        return [stats, abbreviations]


# Pitching stats
def playerInfoP(name):
    # Think about an edge case where there are two players with the same name????
    for player in sa.lookup_player(name):
        d = sa.player_stat_data(player.get('id'), 'pitching', 'season')
        d = d.get('stats')
        stats = d[0].get('stats')
        return [stats, abbreviations]


def lookup(name):
    player_data = sa.lookup_player(name)
    return player_data[0]


def team(id):
    team = sa.lookup_team(id)
    print(team)
    return team[0].get('name')


'''
Functions to add:
    (NOTE: not all api calls return nicely; some return just as one big string which requires some parsing. Save these for last).
    get pitchers and pitching stats (done)
    linescores (hits runs for game on specific data)
    gamepace stats for a given year back to 1999
    get is an advanced use of the api, try to figure out how to use
    last_game gets data from most recent game
    stat leader function
    roster function
    schedule function
    standing function
'''

# get boxscore given a date and a team (can be either 1 or 2 teams)
'''
how to tackle:
info is coming back in an ok but length format
work on each part one at a time(each piece of info should be treated as its own container
work first on: teamInfo, totals
'''


def getBoxScore(date, team_id):
    # edge_cases (double header) OR no games
    gid = sa.schedule(date=date, team=143)[0]['game_id']
    box = sa.boxscore_data(gamePk=gid)
    return box

def categories():
    arr = []
    leaderCategories = sa.get(endpoint='meta', params={'type': 'leagueLeaderTypes'})
    for e in leaderCategories:
        arr.append(e['displayName'])
    return arr

def statLeaders(category, group, season):
    leaders = sa.league_leader_data(leaderCategories=category, limit=10, statGroup=group, season=season)
    return leaders

def season_timeline():
    data = sa.latest_season()
    print(data)

def standings():
    stand = sa.standings_data(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None)
    return stand

def teamRecord(id):
    stand = standings()
    for league in stand:
        for elem in stand[league]['teams']:
            if elem['team_id'] == id:
                return elem


def roster(teamId):
    r = sa.roster(teamId)
    result =[]
    arr = r.split('\n')
    for e in arr:
        if e == '':
            continue
        e = (" ".join(e.split())).split(' ')
        name = ""
        for i in range(2, len(e)):
            name += e[i] + ' '
        result.append(
            {
                'number': e[0],
                'position': e[1],
                'name': name.rstrip()
            }
        )
    return result

def nameToTeamId(name):
    teams = sa.lookup_team('')
    for team in teams:
        if team['teamName'] == name:
            return team['id']
    return -1

def allTeams():
    teams = sa.lookup_team('')
    arr = []
    for team in teams:
        arr.append(team['teamName'])

    return arr

def playerInfo2(name,year,stat):
    # Think about an edge case where there are two players with the same name????
    for player in sa.lookup_player(name):
        d = sa.player_stat_data(player.get('id'), stat, 'yearByYear')
        d = d.get('stats')
        for season in d:
            if season['season'] == str(year):

                return [season['stats'], abbreviations if stat == 'hitting' else abbreviationsP]
        return -1

def playerInfoP2(name,year):
    # Think about an edge case where there are two players with the same name????
    for player in sa.lookup_player(name):
        d = sa.player_stat_data(player.get('id'), 'pitching', 'yearByYear')
        d = d.get('stats')
        for season in d:
            if season['season'] == str(year):
                return [season['stats'], abbreviations]
        return -1

def retrieve_players():
    players = set()
    for c in alphabet:
        for player in sa.lookup_player(c):
            players.add(player['fullName'])
    return players

