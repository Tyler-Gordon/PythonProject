import sqlite3

conn = sqlite3.connect('characters.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE character
          (id INTEGER PRIMARY KEY ASC, 
           username VARCHAR(250) NOT NULL,
           health INTEGER NOT NULL,
           attack INTEGER NOT NULL,
           defence INTEGER NOT NULL,
           attack_speed INTEGER NOT NULL,
           type VARCHAR(10) NOT NULL,
           sword_crit_chance INTEGER,
           sword_crit_modifier INTEGER,
           shield_defence_modifier INTEGER,
           spell_power INTEGER,
           spell_chance INTEGER
           )
          ''')

conn.commit()
conn.close()