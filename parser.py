from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime
import json
import pprint
import datetime as dt
import total_pie_chart as pie
import total_runs as bar
import CONSTANTS

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


# MAIN FUNCTION # 
runs = []

# sort runs
for f in scandir(CONSTANTS.SAVE_PATH):
    if (not isBackupRun(f.name, CONSTANTS.BACKUP_FLAG)):
        runs.append(f)

runs.sort(key=getModifiedDate)

days = getPlaysPerDay(runs)

bar.drawBarChart(days)

