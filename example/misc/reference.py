import statsapi as sa


hitting_stats = {"era", "homeRuns", "atBats", "runs", "hits", "doubles", "triples", "rbi", "walks", "strikeouts", "stolenBases",
                 "caughtStealing", "gamesPlayed", "avg", "ops", "obp", "slg", "hitByPitch", "plateAppearances", "sacrificeBunts",
                 "sacFlies", "gidp", "extraBaseHits", "totalBases", "intentionalWalks", }
pitching_stats = {"era", "wins", "losses", "games", "gamesStarted", "completeGames", "shutouts", "saves", "saveOpportunities",
                  "inningsPitched", "hits", "runs", "earnedRuns", "homeRuns","hitBatsman", "walks", "strikeouts", "whip", "avg",
                  "totalBattersFaced", "numberOfPitches", "pitchesPerInning", "gamesFinished","holds", "intentionalWalks",
                  "wildPitches", "balks", "groundIntoDoublePlay", "StolenBases", "caughtStealing", "pickoffs"}


# prints out all hitting stat options

def printHittingStats():
    i = 1
    for stat in hitting_stats:
        print(i, ". ", stat)
        i += 1

# prints out all hitting stat options
def printPitchingStats():
    i = 1
    for stat in pitching_stats:
        print(i, ". ", stat)
        i += 1


# prints out hitting stat Leaders based on user input
def hittingStatLeaders():
    stat = input("please enter in a stat to check out!: ")
    while not (stat in hitting_stats):
        print("Unsupported stat")
        stat = input("please enter in a stat to check out!: ")

    season = int(input("What season do you want to look at?: "))
    while 1876 > season > 2023:
        print("please select a season from 1876 to now!")
        season = int(input("What season do you want to look at?: "))

    print(sa.league_leaders(leaderCategories=stat, season=season, limit=50))

# prints out pitching stat Leaders based on user input
def PitchingStatLeaders():
    stat = input("please enter in a stat to check out!: ")
    while not (stat in pitching_stats):
        print("Unsupported stat")
        stat = input("please enter in a stat to check out!: ")

    season = int(input("What season do you want to look at?: "))
    while 1876 > season > 2023:
        print("please select a season from 1876 to now!")
        season = int(input("What season do you want to look at?: "))

    print(sa.league_leaders(leaderCategories=stat, season=season, limit=50))