import matplotlib.pyplot as plt
import numpy as np
import pprint
import CONSTANTS

def drawBarChart(runs):
    # totalRunz = totalRuns(runs)
    # pprint.pprint(totalRunz)

    # fig, ax = plt.subplots()

    # ax.bar(totalRunz.keys(), totalRunz.values())
    # ax.set_title('Number of runs per day')

    # plt.show()

    # with each character broken out with color

    pprint.pprint(runs)
    runsWithCharacters = parseData(runs)

    x = runs.keys()
    ironcladRuns = np.array(runsWithCharacters["IRONCLAD"])
    silentRuns = np.array(runsWithCharacters["SILENT"])
    regentRuns = np.array(runsWithCharacters["REGENT"])
    necrobinderRuns = np.array(runsWithCharacters["NECROBINDER"])
    defectRuns = np.array(runsWithCharacters["DEFECT"])

    plt.bar(x, ironcladRuns, color=CONSTANTS.COLORS[0], edgecolor = "none")
    plt.bar(x, silentRuns, bottom=ironcladRuns, color=CONSTANTS.COLORS[1], edgecolor = "none")
    plt.bar(x, regentRuns, bottom=ironcladRuns + silentRuns, color=CONSTANTS.COLORS[2], edgecolor = "none")
    plt.bar(x, necrobinderRuns, bottom=ironcladRuns + silentRuns + regentRuns, color=CONSTANTS.COLORS[3], edgecolor = "none")
    plt.bar(x, defectRuns, bottom=ironcladRuns + silentRuns + regentRuns + necrobinderRuns, color=CONSTANTS.COLORS[4], edgecolor = "none")
    plt.show()

# {
#   2026-04-18: [0,4,2,1,1],
#   2026-04-19: [1,2,0,0,1]
#   2026-04-20: [6,0,0,0,1]
# }
# to 
# {
#   IRONCLAD: [0,1,6]
#   SILENT:   [4,2,0]
#   ...
# }
def parseData(runs):
    characters = {"IRONCLAD": [], "SILENT": [], "REGENT": [], "NECROBINDER": [], "DEFECT": []}
    for date, plays in runs.items():
        print(date,plays)
        characters["IRONCLAD"].append(plays[0])
        characters["SILENT"].append(plays[1])
        characters["REGENT"].append(plays[2])
        characters["NECROBINDER"].append(plays[3])
        characters["DEFECT"].append(plays[4])
    return characters


def totalRuns(runs):
    for date, plays in runs.items():
        runs[date] = sum(plays)
    return runs
