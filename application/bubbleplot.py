import matplotlib.pyplot as plt
import numpy as np

def bubbleplot():
    x = np.random.rand(40)
    y = np.random.rand(40)
    z = np.random.rand(40)

    # use the scatter function
    plt.scatter(x, y, s=z*1000, alpha=0.5)

    # show the graph
    plt.savefig('application/static/images/bubbleplot.png')
    #plt.show()