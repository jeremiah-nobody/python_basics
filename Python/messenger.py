import sqlite3
import sys

conn = sqlite3.connect("messenger.db")
db = conn.cursor()

username = input("Username: ")
password = input("Password: ")

if not username:
    print("You must input username.")
    sys.exit()
    
if not password:
    print("You must enter password.")
    sys.exit()

check = db.execute(f"SELECT * from users WHERE password == '{password}' AND username = '{username}'")

if not check:
    print("Invalid Username or Password")
    sys.exit()

db.execute("SELECT * FROM messages")

message = db.fetchall()

for row in message:
    for column in row:
        print(column)
    print("")

action = input("Action: ")

if action.lower().strip() == "new":
    message = input("Message: ")

    db.execute(f"INSERT INTO messages(message, sender) VALUES('{message}', '{username}')")
    conn.commit()