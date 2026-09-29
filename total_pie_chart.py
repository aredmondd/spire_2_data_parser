import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

def drawPie(values):
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))
    fig, ax = plt.subplots()
    ax.pie(values, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    plt.show()

