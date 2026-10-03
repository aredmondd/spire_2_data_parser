from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime
import json
import pprint
import datetime as dt
import total_pie_chart as pie
import total_runs as bar
import CONSTANTS
import drawLineChart as lineChart

# HELPER FUNCTIONS #
def getRunJson(run):
    return json.load(open(run.path))

def isSinglePlayerRun(run):
    return len(run['players']) == 1

def isWin(run):
    return run['win'] == True

def isBackupRun(name: string, backupFlag: string) -> bool:
    if (name.find(backupFlag) == -1):
        return False
    return True

def formatDate(ms: int) -> float:
    return datetime.fromtimestamp(ms);

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
                case CONSTANTS.Character.IRONCLAD.value:
                    dayArray[0] = dayArray[0] + 1
                case CONSTANTS.Character.SILENT.value:
                    dayArray[1] = dayArray[1] + 1
                case CONSTANTS.Character.REGENT.value:
                    dayArray[2] = dayArray[2] + 1
                case CONSTANTS.Character.NECROBINDER.value:
                    dayArray[3] = dayArray[3] + 1
                case CONSTANTS.Character.DEFECT.value:
                    dayArray[4] = dayArray[4] + 1
                case _:
                    raise ValueError(runChar, "is not valid")

            days[runDate] = dayArray

    return dict(sorted(days.items()))

def getWinLossOverTime(runs):
    ratioPerDay = {}
    wins = 0
    losses = 0

    for r in runs:
        file = open(r.path)
        d = json.load(file)
        players = d['players']

        runDate = formatDate(d['start_time']).date()

        if (len(players) == 1):
            if d['win'] == True:
                wins += 1
            else:
                losses += 1

            ratioPerDay[runDate] = wins / losses * 100

    return ratioPerDay

def getMinMaxDeckSize(runs):
    data = getRunJson(runs[0])

    firstRunDeckLength = len(data['players'][0]['deck'])

    largest = firstRunDeckLength
    largestRun = data
    smallest = firstRunDeckLength
    smallestRun = data

    for r in runs:
        data = getRunJson(r)

        if (isSinglePlayerRun(data) and isWin(data)):
            deckLength = len(data['players'][0]['deck'])
            if (deckLength > largest):
                largest = deckLength
                largestRun = data
            if (deckLength < smallest):
                smallest = deckLength
                smallestRun = data

    print(largest)
    pprint.pprint(largestRun)
    print(smallest)
    pprint.pprint(smallestRun)

def getShortestAndLongestRun(runs):
    data = getRunJson(runs[0])

    firstRunLength = data['run_time']

    shortestRun = firstRunLength
    shortRunData = data
    longestRun = firstRunLength
    longestRunData = data

    for r in runs:
        data = getRunJson(r)

        if (isSinglePlayerRun(data) and isWin(data)):
            runLength = data['run_time']
            if runLength > longestRun:
                longestRun = runLength
                longestRunData = data
            if runLength < shortestRun:
                shortestRun = runLength
                shortestRunData = data

    print(shortestRun / 60)
    print(formatDate(shortRunData['start_time']), shortRunData['players'][0]['character'])
    print(longestRun / 60)
    print(formatDate(longestRunData['start_time']), longestRunData['players'][0]['character'])

# def getLongestLossStreak():

# def getLongestWinStreak():

# def mapDeckSize():

def mapRunTime(runs):
    runTimes = []

    for r in runs:
        data = getRunJson(r)
        runTimes.append(formatDate(data['start_time']).time())

    runTimes.sort()

    return runTimes

# MAIN FUNCTION # 
runs = []

# sort runs
for f in scandir(CONSTANTS.SAVE_PATH):
    if (not isBackupRun(f.name, CONSTANTS.BACKUP_FLAG)):
        runs.append(f)

runs.sort(key=getCreatedDate)

# days = getPlaysPerDay(runs)
# ratios = getWinLossOverTime(runs)

# getMinMaxDeckSize(runs)
# getShortestAndLongestRun(runs)

# bar.drawBarChart(days)
# lineChart.drawPlot(ratios)

times = mapRunTime(runs)
pprint.pprint(times)
