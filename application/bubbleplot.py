import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def bubbleplot():
    #plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

    # date and time are hard-coded for example because I do not yet have a database set-up that I can query using sql, from which I can create a pandas dataframe with results
    # pain is hard-coded because I have not yet created the pain scale assessment
    date = ['Jun 6', 'Jun 7', 'Jun 8', 'Jun 9', 'Jun 10', 'Jun 11', 'Jun 14', 'Jun 14', 'Jun 15', 'Jun 16']
    time = [10, 21, 9, 8, 12, 11, 10, 7, 6, 10]
    pain = [10, 15, 20, 25, 30, 30, 45, 45, 50, 55]

    plt.figure(figsize=(4, 3))
    ax=plt.subplot()
    plt.subplots_adjust(bottom = 0.2, left = 0.2)
    plt.scatter(date, time, s=pain, alpha=0.5)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
    ax.yaxis.set_major_locator(ticker.MultipleLocator(4))

    plt.xticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Time of Day', fontsize=8, )
    plt.title('My Symptom Record')
    plt.savefig('application/static/images/bubbleplot.png')
    plt.show()

if __name__ == '__main__':
    bubbleplot()

# need to add code to handle missing values
# need to add code to handle too many dates along y-axis

# can I get the ai to generate the bubbleplot?