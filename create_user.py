import sqlite3
conn=sqlite3.connect("Kaveesh.db")
conn.execute("CREATE TABLE user(id INTEGER PRIMARY KEY,username TEXT,password TEXT)")
print("Table created")
conn.close