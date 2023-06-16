import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def scatterplot():
    #plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

    # date and time are hard-coded for example because I do not yet have a database set-up that I can query using sql, from which I can create a pandas dataframe with results
    date = ['Jun 6', 'Jun 7', 'Jun 8', 'Jun 9', 'Jun 10', 'Jun 11', 'Jun 14', 'Jun 14', 'Jun 15', 'Jun 16']
    time = [10, 21, 9, 8, 12, 11, 10, 7, 6, 10]

    plt.figure(figsize=(4, 3))
    ax=plt.subplot()
    plt.subplots_adjust(bottom = 0.2, left = 0.2)


    plt.scatter(date, time, marker='x', color='red', s=40)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) #this sets the x-axis to show every 1 day  
    ax.yaxis.set_major_locator(ticker.MultipleLocator(4)) #this sets the y-axis to show every 1 hour
    
    plt.xticks(fontsize=6)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Time of Day', fontsize=8, )
    plt.title('My Symptom Record')
    
    plt.savefig('application/static/images/scatterplot.png')
    #plt.show()


if __name__ == '__main__':
    scatterplot()

# add code to handle dates properly
# need to add code to handle missing values
# need to add code to handle too many dates along y-axis