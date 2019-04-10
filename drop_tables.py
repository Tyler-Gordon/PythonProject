import sqlite3

conn = sqlite3.connect('characters.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE character
          ''')

conn.commit()
conn.close()
