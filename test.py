import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_querry = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_querry, user)

users = [
    (2, 'bob', 'asdf'),
    (3, 'rolf', 'xyz')
]
cursor.executemany(insert_querry, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()