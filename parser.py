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


# MAIN FUNCTION # 
count = 0
for f in scandir(savePath):
    if (not isBackupRun(f.name, backupFlag)):
        print(formatDate(stat(f).st_mtime))
        print(stat(f))
        print(f.name)
        print()
        count += 1
print("Done!", count)

