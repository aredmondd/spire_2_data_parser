import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')


def drawPie(values):
    fig, ax = plt.subplots()
    ax.pie(values, colors=COLORS, labels=values, wedgeprops={'linewidth': 2})
    plt.show()

