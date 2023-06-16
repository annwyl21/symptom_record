import matplotlib.pyplot as plt

def scatterplot():
    #plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

    # date and time are hard-coded for example because I do not yet have a database set-up that I can query using sql, from which I can create a pandas dataframe with results
    date = ['Jun 6', 'Jun 7', 'Jun 8', 'Jun 9', 'Jun 10', 'Jun 11', 'Jun 14', 'Jun 14', 'Jun 15', 'Jun 16']
    time = [10, 21, 9, 8, 12, 11, 10, 7, 6, 10]

    plt.scatter(date, time, marker='x', color='red', s=40)
    plt.xlabel('Date')
    plt.ylabel('Time of Day')
    plt.title('My Symptom Record')
    plt.savefig('application/static/images/scatterplot.png')
    #plt.show()


if __name__ == '__main__':
    scatterplot()
