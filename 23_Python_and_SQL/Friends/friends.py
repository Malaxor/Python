import sqlite3

conn = sqlite3.connect('my_friends.db')
# create cursor object
c = conn.cursor()
# execute some SQL
people = [
   ("Roald", "Amundsen", 5),
   ("Rosa", "Parks", 8),
   ("Henry", "Hudson", 7),
   ("Neil", "Armstrong", 6),
   ("Daniel", "Boone", 3)
]
query = "INSERT INTO friends VALUES (?,?,?)"
c.executemany(query, people)
# commit changes
conn.commit()

conn.close()
