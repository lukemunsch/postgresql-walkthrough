import psycopg2


# connects to "chinook" database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()


# query1 - select all records from artist table
cursor.execute('SELECT * FROM "Artist"')

# produce results for the file
results = cursor.fetchall()
# results = cursor.fetchone()


# remember to close connection once finished
connection.close()


# print results
for result in results:
    print(result)
