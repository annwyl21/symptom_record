import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from application.data_format import Data_format

def scatterplot(symptom_list):
    date_time_list = Data_format.reformat_for_scatterplot(symptom_list)
    date_list = []
    time_list = []
    for symptom_data in date_time_list:
        date_list.append(symptom_data[0])
        time_list.append(symptom_data[1])

    plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

    plt.figure(figsize=(4, 3))
    ax=plt.subplot()
    plt.subplots_adjust(bottom = 0.2, left = 0.2)

    plt.scatter(date_list, time_list, marker='x', color='red', s=40)

    #ax.set_ylim([0, 24])  # This sets the limits of y-axis from 0 to 24
    ax.set_yticks([0, 4, 8, 12, 16, 20, 24]) # This sets the y-axis to show every 4 hours
    #ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) #this sets the x-axis to show every 1 day  
    #ax.yaxis.set_major_locator(ticker.MultipleLocator(4)) #this sets the y-axis to show every 1 hour
    
    plt.xticks(fontsize=6, rotation=45)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Time of Day', fontsize=8)
    plt.title('My Symptom Record')
    
    plt.savefig('application/static/images/scatterplot.png')
    #plt.show()


if __name__ == '__main__':
    scatterplot()

# add code to handle dates properly
# need to add code to handle missing values
# need to add code to handle too many dates along y-axis