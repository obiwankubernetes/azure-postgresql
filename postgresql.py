# Step 1 
# Create postgres db on azure (tutorial by Will Brock @ https://www.youtube.com/watch?v=DJd-Mr6nalc)

# Step 2
# Connect to db through python (tutorial by MSFT @ https://docs.microsoft.com/en-us/azure/postgresql/connect-python

# install packages
# pip install psycopg2

# import packages
import psycopg2
import config

# Update connection string information from portal below
host = config.server_name
dbname = config.database_name
user = config.admin_username
password = config.admin_password
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string) 
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed)")

# Create an example tabble
cursor.execute("CREATE TABLE Blogpost (id serial PRIMARY KEY, title VARCHAR(50), subtitle VARCHAR(50), author VARCHAR(50), date_posted DATE, content TEXT);")
print("Finished creating table")

# Insert some sample data into the table
cursor.execute("INSERT INTO Blogpost (title, subtitle, author, date_posted, content) VALUES (%s, %s, %s, %s, %s);", ("test1", "test1", "test1", "2020-06-06", "testing"))
cursor.execute("INSERT INTO Blogpost (title, subtitle, author, date_posted, content) VALUES (%s, %s, %s, %s, %s);", ("test2", "test2", "test2", "2020-06-06", "testing"))
cursor.execute("INSERT INTO Blogpost (title, subtitle, author, date_posted, content) VALUES (%s, %s, %s, %s, %s);", ("test3", "test3", "test3", "2020-06-06", "testing"))
print("Inserted 3 rows of data")

# # Clean up
# conn.commit()
# cursor.close()
# conn.close()