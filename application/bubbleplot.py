import matplotlib.pyplot as plt
import numpy as np

def bubbleplot():
    #plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

    # x = np.random.rand(40)
    # y = np.random.rand(40)
    # z = np.random.rand(40)

    # date and time are hard-coded for example because I do not yet have a database set-up that I can query using sql, from which I can create a pandas dataframe with results
    # pain is hard-coded because I have not yet created the pain scale assessment
    date = ['Jun 6', 'Jun 7', 'Jun 8', 'Jun 9', 'Jun 10', 'Jun 11', 'Jun 14', 'Jun 14', 'Jun 15', 'Jun 16']
    time = [10, 21, 9, 8, 12, 11, 10, 7, 6, 10]
    pain = [10, 15, 20, 25, 30, 30, 45, 45, 50, 55]

    # use the scatter function
    #plt.scatter(x, y, s=z*1000, alpha=0.5) where alpha is the transparency of the bubbles, to handle overlapping bubbles
    plt.scatter(date, time, s=pain, alpha=0.5)

    plt.xlabel('Date')
    plt.ylabel('Time of Day')
    plt.title('My Symptom Record')
    plt.savefig('application/static/images/bubbleplot.png')
    #plt.show()

if __name__ == '__main__':
    bubbleplot()