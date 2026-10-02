import matplotlib.pyplot as plt
import numpy as np

def drawBarChart(values, labels):
    labels = list(labels)
    # values = list(values)

    # for label in range(len(labels)): labels[label] = labels[label].isoformat()

    fig, ax = plt.subplots()
    bottom = np.zeros(3)

    ax.bar(labels, values)
    # ax.tick_params("x", rotation=45, rotation_mode="xtick", width=2)
    ax.set_title('Number of runs per day')

    # plt.show()
