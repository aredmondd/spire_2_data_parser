import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

COLORS = ['#d53b27', '#2e7d32', '#f07c1e', '#bf5a85', '#3873a9']

def drawPie(values):
    fig, ax = plt.subplots()
    ax.pie(values, colors=COLORS, labels=values, wedgeprops={'linewidth': 2})
    plt.show()

