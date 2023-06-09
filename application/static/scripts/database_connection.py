import psycopg2

def test_connection():

    print('Connecting to the PostgreSQL database...TESTING')
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

    # Execute a query:
    # To display the PostgreSQL 
    # database server version
    cur.execute('SELECT version()')
    print(cur.fetchone())



    cur.execute("SELECT schema_name FROM information_schema.schemata;")
    print("List of schemas in your database:")
    schemas = cur.fetchall()
    for schema in schemas:
        print(schema)


    cur.execute("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'symptom_log'""")
    print("List of tables in schema symptom_log:")
    tables = cur.fetchall()
    for table in tables:
        print(table)

    # Execute a query
    #cur.execute("select * from user-info;")

    # Fetch the results
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == '__main__':
    test_connection()