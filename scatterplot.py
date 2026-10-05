import matplotlib.pyplot as plt
import numpy as np

def drawPlot(runs):
    fig, ax = plt.subplots()

    dayOfWeeks= []
    times = []

    for r in runs:
        dayOfWeeks.append(r.weekday())
        times.append(r.hour * 60 + r.minute)

    x = dayOfWeeks
    y = times

    ax.scatter(x,y, alpha=0.25, edgecolors='none')
    ax.grid(True)

    plt.show()
