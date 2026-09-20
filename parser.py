from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime
import json
import pprint

# CONSTANTS #
savePath = "/home/aetos/.local/share/SlayTheSpire2/steam/76561198854416655/profile1/saves/history/"
backupFlag = ".backup"
jsonData = ['acts', 'build_id', 'game_mode', 'killed_by_encounter', 'killed_by_event', 'map_point_history', 'modifiers', 'platform_type', 'players', 'run_time', 'schema_version', 'seed', 'start_time', 'was_abandoned', 'win']

# HELPER FUNCTIONS #
def isBackupRun(name: string, backupFlag: string) -> bool:
    if (name.find(backupFlag) == -1):
        return False
    return True

def formatDate(ms: int) -> str:
    return datetime.fromtimestamp(ms);

def getModifiedDate(file: os.DirEntry) -> int:
    return stat(file).st_mtime

# the name of the file is the `startTimeInSeconds.run`.
# we can chop off run and get the created date. 
def getCreatedDate(file: os.DirEntry) -> str:
    return formatDate(int(r.name[:-4]))

# MAIN FUNCTION # 
runs = []

for f in scandir(savePath):
    if (not isBackupRun(f.name, backupFlag)):
        runs.append(f)

runs.sort(key=getModifiedDate)

killedByDict = {}

for r in runs:
    file = open(r.path)
    d = json.load(file)
    killedBy = d['killed_by_encounter']
    if killedBy in killedByDict:
        killedByDict[killedBy] = killedByDict[killedBy] + 1
    else:
        killedByDict[killedBy] = 1
    pprint.pprint(d)
    break

temp = 0
tempKey = ""
for key in killedByDict:
    if killedByDict[key] > temp and key != "NONE.NONE":
        temp = killedByDict[key]
        tempKey = key

print(temp, tempKey)
