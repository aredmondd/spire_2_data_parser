from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime
import json
import pprint
import datetime as dt
import total_pie_chart as pie
import total_runs as bar
from enum import Enum

# 76561198854416655 is my ID

# CONSTANTS #
savePath = "/home/aetos/.local/share/SlayTheSpire2/steam/76561198854416655/profile1/saves/history/"
# macSavePath = "/Users/aidenredmond/Library/Application Support/SlayTheSpire2/steam/76561198854416655/profile1/saves/history"
backupFlag = ".backup"
jsonData = ['acts', 'ascension', 'build_id', 'game_mode', 'killed_by_encounter', 'killed_by_event', 'map_point_history', 'modifiers', 'platform_type', 'players', 'run_time', 'schema_version', 'seed', 'start_time', 'was_abandoned', 'win']

class Character(Enum):
    IRONCLAD = "CHARACTER.IRONCLAD"
    SILENT = "CHARACTER.SILENT"
    REGENT = "CHARACTER.REGENT"
    NECROBINDER = "CHARACTER.NECROBINDER"
    DEFECT = "CHARACTER.DEFECT"

# HELPER FUNCTIONS #
def isBackupRun(name: string, backupFlag: string) -> bool:
    if (name.find(backupFlag) == -1):
        return False
    return True

def formatDate(ms: int) -> float:
    return datetime.fromtimestamp(ms);

def getModifiedDate(file: os.DirEntry) -> int:
    return stat(file).st_mtime

# the name of the file is the `startTimeInSeconds.run`.
# we can chop off run and get the created date. 
def getCreatedDate(file: os.DirEntry) -> float:
    return formatDate(int(file.name[:-4]))

def getPlaysPerDay(runs):
    days = {}
    startDate = datetime.fromisoformat('2026-04-13').date()
    endDate = datetime.today().date()

    diff = abs((startDate - endDate).days)

    for day in range(diff + 1):
        loopDate = startDate + dt.timedelta(days=day)
        days[loopDate] = [0,0,0,0,0]

    for r in runs:
        file = open(r.path)
        d = json.load(file)
        players = d['players']

        runDate = formatDate(d['start_time']).date()

        if (len(players) == 1):
            runChar = players[0]['character']
            dayArray = days[runDate]

            match runChar:
                case Character.IRONCLAD.value:
                    dayArray[0] = dayArray[0] + 1
                case Character.SILENT.value:
                    dayArray[1] = dayArray[1] + 1
                case Character.REGENT.value:
                    dayArray[2] = dayArray[2] + 1
                case Character.NECROBINDER.value:
                    dayArray[3] = dayArray[3] + 1
                case Character.DEFECT.value:
                    dayArray[4] = dayArray[4] + 1
                case _:
                    raise ValueError(runChar, "is not valid")

            days[runDate] = dayArray

    return dict(sorted(days.items()))

def getWinsPerDay(runs):
    wins = {}
    startDate = datetime.fromisoformat('2026-04-13').date()
    endDate = datetime.today().date()

    num = 1
    for r in runs:
        file = open(r.path)
        d = json.load(file)
        players = d['players']

        if (len(players) == 1 and d['win'] == True):
            runDate = formatDate(d['start_time']).date()
            print('win on', runDate, 'as ', players[0]['character'], 'on A', d['ascension'])
            if(wins.get(runDate) != None):
                wins[runDate] += 1
            else:
                wins[runDate] = 1
        num += 1

    return dict(sorted(wins.items()))



# MAIN FUNCTION # 
runs = []
runsPerCharacter = {'CHARACTER.IRONCLAD': 0, 'CHARACTER.SILENT': 0, 'CHARACTER.REGENT': 0, 'CHARACTER.NECROBINDER': 0, 'CHARACTER.DEFECT': 0}

# sort runs
for f in scandir(savePath):
    if (not isBackupRun(f.name, backupFlag)):
        runs.append(f)

runs.sort(key=getModifiedDate)

# get data about runs

singlePlayerRunCount = 0
multiPlayerRunCount = 0;

days = getPlaysPerDay(runs)
# wins = getWinsPerDay(runs)

pprint.pprint(days)
# pprint.pprint(json.load(open(runs[0].path)))
bar.drawBarChart(days.values(), days.keys())


# for r in runs:
    # file = open(r.path)
    # d = json.load(file)
    # players = d['players']

    # if (len(players) == 1):
        # print(getCreatedDate(file))
        # character = players[0]['character']
        # runsPerCharacter[character] += 1
        # singlePlayerRunCount += 1
    # else:
        # multiPlayerRunCount += 1


# results
# print(singlePlayerRunCount)
# print(multiPlayerRunCount)
# print(runsPerCharacter)
# pie.drawPie(list(runsPerCharacter.values()))

