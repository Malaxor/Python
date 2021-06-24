import sqlite3

conn = sqlite3.connect('my_friends.db')
# create cursor object
c = conn.cursor()
# execute some SQL
# c.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INTEGER)")
# insert_query = """
#    INSERT INTO friends
#    VALUES('Charlie', 'Lewis', 7)
# """
data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
# commit changes
conn.commit()

conn.close()
