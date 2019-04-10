import sqlite3

conn = sqlite3.connect('characters.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE character
          (id INTEGER PRIMARY KEY ASC, 
           username VARCHAR(250) NOT NULL,
           health VARCHAR(250) NOT NULL,
           attack VARCHAR(250) NOT NULL,
           defence VARCHAR(250) NOT NULL,
           attack_speed VARCHAR(10) NOT NULL,
           sword_crit_chance VARCHAR(100),
           sword_crit_modifier VARCHAR(10),
           shield_defence_modifier VARCHAR(10),
           spell_power VARCHAR(100),
           spell_chance VARCHAR(10)
           )
          ''')

conn.commit()
conn.close()