import mysql.connector

my_db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'python7am'
)

my_cursor = my_db.cursor()

def select(table):
    global my_cursor
    # query = "SELECT * FROM table;"
    return my_cursor.execute("SELECT * FROM table;")

select('users')
# ____________________________
# def insert(*tablename, **data):
#     query = "INSERT INTO tablename VALUES data"
#     my_cursor.execute(query)

# # data = ['ram','sita','gita']

# insert('users', name='ram')
# ________________________________________

# query = "CREATE DATABASE IF NOT EXISTS python7am"

# my_cursor.execute(query)

# create_query = "create table if not exists users(id int auto_increment primary key, name varchar(100))"

# my_cursor.execute(create_query)

# insert_query="INSERT INTO users(name) VALUES('admin')"
# my_cursor.execute(insert_query)

# select_query = "SELECT * from users"
# my_cursor.execute(select_query)
# result = my_cursor.fetchall()
# result = my_cursor.fetchone()
# result = my_cursor.fetchmany(4)
# for user in result:
#     print(user)

# delete_query = "DELETE FROM users WHERE id='2'"
# my_cursor.execute(delete_query)
# my_db.commit()  #always required in case of inserting/updating the database