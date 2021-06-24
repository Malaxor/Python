import sqlite3

conn = sqlite3.connect('my_friends.db')
# create cursor object
c = conn.cursor()
# execute some SQL
c.execute("SELECT * FROM friends")

# iterate over cursor 
# for result in c:
#    print(result)

# fetchg one result
# print(c.fetchone())

# fetch all results as a list
# print(c.fetchall())

# commit changes
conn.commit()

conn.close()
