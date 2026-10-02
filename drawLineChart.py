import matplotlib.pyplot as plt
import numpy as np

def drawPlot(runs):
    fig, ax = plt.subplots()

    ax.stackplot(runs.keys(), runs.values(), color='r')

    plt.show()
