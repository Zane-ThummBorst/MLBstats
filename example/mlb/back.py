import statsapi as sa
import django
# sets of all possible stats for leader functions (hitting and pitching)
# May be useful if combining data
# hitting_stats = {"era", "homeRuns", "atBats", "runs", "hits", "doubles", "triples", "rbi", "walks", "strikeouts", "stolenBases",
#                  "caughtStealing", "gamesPlayed", "avg", "ops", "obp", "slg", "hitByPitch", "plateAppearances", "sacrificeBunts",
#                  "sacFlies", "gidp", "extraBaseHits", "totalBases", "intentionalWalks", }
# pitching_stats = {"era", "wins", "losses", "games", "gamesStarted", "completeGames", "shutouts", "saves", "saveOpportunities",
#                   "inningsPitched", "hits", "runs", "earnedRuns", "homeRuns","hitBatsman", "walks", "strikeouts", "whip", "avg",
#                   "totalBattersFaced", "numberOfPitches", "pitchesPerInning", "gamesFinished","holds", "intentionalWalks",
#                   "wildPitches", "balks", "groundIntoDoublePlay", "StolenBases", "caughtStealing", "pickoffs"}
abbreviations ={
    "gamesPlayed": "GP",
    "groundOuts": "GO",
    "airOuts": "AO",
    "runs": "r",
    "doubles": "2B",
    "triples": "3B",
    "homeRuns": "HR",
    "strikeOuts": "SO",
    "baseOnBalls": "BB",
    "intentionalWalks": "IW",
    "hits": "H",
    "hitByPitch": "HBP",
    "avg": "avg",
    "atBats": "AB",
    "obp": "OBP",
    "slg": "SLG",
    "ops": "OPS",
    "caughtStealing": "CS",
    "stolenBases": "SB",
    "stolenBasePercentage": "SBP",
    "groundIntoDoublePlay": "GIDP",
    "numberOfPitches": "NUP",
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

def playerInfo(name):
    # Think about an edge case where there are two players with the same name????
    for player in sa.lookup_player(name):
        #print('Full name: {}, Position: {}'.format(player['fullName'], player['primaryPosition']['abbreviation']))
        d = sa.player_stat_data(player.get('id'), 'hitting', 'season')
        d = d.get('stats')
        stats = d[0].get('stats')
        # for key in stats:

        print(stats)
        return [stats, abbreviations]

def lookup(name):
    player_data = sa.lookup_player(name)
    return player_data[0]

def team(id):
    team = sa.lookup_team(id)
    print(team)
    return team[0].get('name')

# x = 0
# for player in sa.lookup_player("Aaron Judge"):
#     print(player)
#
# # print(sa.get('player',)



