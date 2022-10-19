import sqlite3
import sys

level = 1
p = 1171
connect = sqlite3.connect("dictionary.db")
cur = connect.cursor()
num = 0
count = 117125
print("Status.")
for i in range(100):
     print("_", end="")
print("")
diction = cur.execute(f"SELECT * FROM words")
for row in (diction):
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     word = row[0]
     types = row[1]
     if types == 'adj':
          types = 'adjective'
     if types == 'prep':
          types = 'preposition'
     if types == 'adv':
          types = 'adverb'
     length = row[3]
     definition = row[4]

     try:
          cursor.execute(f"INSERT INTO words('id', 'word', 'type', 'length', 'definition') VALUES ({num}, '{word}', '{types}', {length}, '{definition}')")
          conn.commit()
          num+=1
          level+=1
     except:
          pass
     
     if level == p:
          print("_", end="")
          p = p + 1171
     elif p == count:
          print(".")

   