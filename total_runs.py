import matplotlib.pyplot as plt
import numpy as np
import pprint

def drawBarChart(days):
    totalRunz = totalRuns(days)
    pprint.pprint(totalRunz)

    #parseData(days)

    # labels = list(labels)
    # values = list(values)

    # for label in range(len(labels)): labels[label] = labels[label].isoformat()

    fig, ax = plt.subplots()
    # bottom = np.zeros(3)

    ax.bar(totalRunz.keys(), totalRunz.values())
    # ax.tick_params("x", rotation=45, rotation_mode="xtick", width=2)
    ax.set_title('Number of runs per day')


    plt.show()

# turn data from parser.py
# {
#   2026-04-18: [0,4,2,1,1],
#   2026-04-19: [1,2,0,0,1]
#   2026-04-20: [6,0,0,0,1]
# }
#
# into
#
# {
#   IRONCLAD: [0,1,6]
#   SILENT:   [4,2,0]
#   ...
# }
def parseData(runs):
    characters = {"IRONCLAD": [], "SILENT": [], "REGENT": [], "NECROBINDER": [], "DEFECT": []}
    for date, plays in runs.items():
        characters["IRONCLAD"].append(plays[0])
        characters["SILENT"].append(plays[1])
        characters["REGENT"].append(plays[2])
        characters["NECROBINDER"].append(plays[3])
        characters["DEFECT"].append(plays[4])


def totalRuns(runs):
    for date, plays in runs.items():
        runs[date] = sum(plays)
    return runs
