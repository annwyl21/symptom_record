import matplotlib.pyplot as plt
import numpy as np

def scatterplot():
    price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
    sales_per_day = [34, 62, 49, 22, 13, 19]

    plt.scatter(price, sales_per_day)
    plt.savefig('application/static/images/scatterplot.png')
    #plt.show()



