import psycopg2

# One-time use script to create an example user

print('Connecting to the PostgreSQL database...TESTING')
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

# Add example user to database
cur.execute("insert into symptom_log.user_data (username, password, firstname, lastname, email) values (%s, %s, %s, %s, %s);", ('example_user', 'password', 'Example', 'User', 'example@email.com'))
conn.commit()

# Retrieve user_id from database
cur.execute("select * from symptom_log.user_data where username = %s and password = %s;", ('example_user', 'password'))
rows = cur.fetchall()
user_id = rows[0][0]

# Add 10 example symptoms to database
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-01', '08:01', 'woke up with headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-04', '07:30', 'really annoying headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-07', '07:25', 'tension headache round my eyes'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-10', '07:15', 'headache with vision blurring'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-12', '07:00', 'woke up with headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-14', '06:45', 'woke up with headache again'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-15', '06:30', 'woke up with a splitting headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-16', '06:01', 'really bad headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-17', '04:01', 'woke up with headache'))
cur.execute("insert into symptom_log.symptom_collection (user_id, date, time, symptom_details) values (%s, %s, %s, %s);", (user_id, '2022-06-17', '11:45', 'headache still there and I can\'t sleep'))
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
