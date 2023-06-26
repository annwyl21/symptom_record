import psycopg2
from datetime import datetime

print('Connecting to the PostgreSQL database...')
# symptom_log is the name of both my database and the schema within it

# Establish a connection to the database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='symptom_log',
    user='postgres',
    password='mysecretpassword'
)

# Create a cursor object
cur = conn.cursor()
print('Connected to the PostgreSQL database')

class Symptom_log:

    def check_username_password_exist(username, password):
        cur.execute("select * from symptom_log.user_data where username = %s and password = %s;", (username, password))
        rows = cur.fetchall()
        if len(rows) == 0:
            return False
        else:
            user_id = rows[0][0]
            return user_id
    
    def add_a_symptom(user_id, symptom_details):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M")
        cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, date, time, symptom_details))
        conn.commit()
        return True
    
    def get_symptoms(user_id):
        cur.execute("select symptom_details from symptom_log.symptom_collection where user_id = %s;", (user_id,)) 
        # note the comma after user_id, this is because the execute() function expects a tuple of parameters, even if there is only one parameter
        # The execute() function in psycopg2, which is a PostgreSQL adapter for Python, expects a SQL query string and then a tuple (or dictionary in some cases) of parameters to substitute into the SQL query.
        rows = cur.fetchall()
        symptoms = rows
        return symptoms
    
    def add_a_symptom_summary(user_id, symptoms_summary, symptoms_start_date, symptoms_end_date):
        # insert the returned summary
        cur.execute("insert into symptom_log.summary_collection (user_id, symptoms_summary, symptoms_start_date, symptoms_end_date) values (%s, %s, %s, %s);", (user_id, symptoms_summary, symptoms_start_date, symptoms_end_date))
        conn.commit()

        # get the summary_id
        cur.execute("select summary_id from symptom_log.summary_collection where user_id = %s and symptoms_summary = %s;", (user_id, symptoms_summary))
        summary_id = cur.fetchall()[0][0]

        # insert the summary_id into the record for each symptom
        cur.execute("update symptom_log.symptom_collection set summary_id = %s where user_id = %s and date >= %s and date <= %s;", (summary_id, user_id, symptoms_start_date, symptoms_end_date))
        conn.commit()
        return True

if __name__ == "__main__":
    # CAN NOT BE RUN WITH THIS DATA AGAIN BECAUSE THIS NOW EXISTS IN THE DATABASE - CHECKED AND CONFIRMED AS WORKING
    #print(Symptom_log.check_username_password_exist('mrs_tester', 'test_password'))
    #print(Symptom_log.add_a_symptom(1, 'headache'))
    #print(Symptom_log.get_symptoms(1))
    #print(Symptom_log.add_a_symptom_summary(1, 'headache', '2023-07-01', '2023-01-31'))
    print(Symptom_log.get_symptoms(1))


# Close the cursor and connection
cur.close()
conn.close()