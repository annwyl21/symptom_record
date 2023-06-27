from datetime import datetime

class Data_format():

	def reformat_for_scatterplot(retrieved_symptoms):
		date_time_list = []
		for date_time in retrieved_symptoms:
			symptom_time = []
			# change the date format of date returned in row[0] to be a uk format
			date = Data_format.us_to_uk_date_format(date_time[0])
			symptom_time.append(date)
			# remove seconds from time returned in row[1]
			time = Data_format.remove_minutes_notation(date_time[1])
			symptom_time.append(time)
			date_time_list.append(symptom_time)
		return date_time_list
    
	def us_to_uk_date_format(date):
		date_time_format = datetime.strptime(str(date), '%Y-%m-%d')
		#uk_date = date_time_format.strftime('%d %B %Y') # returns uk date format
		uk_date = date_time_format.strftime('%d-%b') # returns nice day/ month format
		return uk_date

	def remove_seconds_notation(time):
		time = str(time)
		time = time[:-3]
		return time
	
	def remove_minutes_notation(time):
		time = str(time)
		time = time[:-6]
		return time
	
