from os import listdir, scandir, stat
from os.path import isfile, join
from datetime import datetime

# CONSTANTS #
savePath = "/home/aetos/.local/share/SlayTheSpire2/steam/76561198854416655/profile1/saves/history/"
backupFlag = ".backup"


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

for r in runs:
    print(getCreatedDate(r))
