import sqlite3  
conn = sqlite3.connect('student.db')

c = conn.cursor()
sql = """
  INSERT INTO students (name, intro, avatar)
  VALUES (?, ?, ?)
"""
c.execute(sql, ('Allison', 'Hi!', 'https://i.redd.it/j8fknvi9eg141.jpg'))
c.execute(sql, ('Tom', 'HA!', 'https://i.redd.it/j8fknvi9eg141.jpg'))
c.execute(sql, ('Davids', 'Um...', 'https://i.redd.it/j8fknvi9eg141.jpg'))

conn.commit()
conn.close()