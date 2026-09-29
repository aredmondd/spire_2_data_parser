from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime
import json
import pprint
import datetime as dt

# 76561198854416655 is my ID

# CONSTANTS #
savePath = "/home/aetos/.local/share/SlayTheSpire2/steam/76561198854416655/profile1/saves/history/"
macSavePath = "/Users/aidenredmond/Library/Application Support/SlayTheSpire2/steam/76561198854416655/profile1/saves/history"
backupFlag = ".backup"
jsonData = ['acts', 'build_id', 'game_mode', 'killed_by_encounter', 'killed_by_event', 'map_point_history', 'modifiers', 'platform_type', 'players', 'run_time', 'schema_version', 'seed', 'start_time', 'was_abandoned', 'win']
characters = ['IRONCLAD', 'SILENT', 'REGENT', 'NECROBINDER', 'DEFECT']

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
    return formatDate(int(r.name[:-4]))

# MAIN FUNCTION # 
runs = []
runsPerCharacter = {'CHARACTER.IRONCLAD': 0, 'CHARACTER.SILENT': 0, 'CHARACTER.REGENT': 0, 'CHARACTER.NECROBINDER': 0, 'CHARACTER.DEFECT': 0}

for f in scandir(macSavePath):
    if (not isBackupRun(f.name, backupFlag)):
        runs.append(f)

runs.sort(key=getModifiedDate)

singlePlayerRunCount = 0
multiPlayerRunCount = 0;

for r in runs:
    file = open(r.path)
    d = json.load(file)
    players = d['players']


    if (len(players) == 1):
        print(getCreatedDate(file))
        character = players[0]['character']
        runsPerCharacter[character] += 1
        singlePlayerRunCount += 1
    else:
        multiPlayerRunCount += 1


print(singlePlayerRunCount)
print(multiPlayerRunCount)
print(runsPerCharacter)
