import sqlite3  
conn = sqlite3.connect('student.db')

c = conn.cursor()
sql = """
    SELECT id, name, intro, avatar 
     FROM students
"""
c.execute(sql)

#print(c.fetchall())

stus = c.fetchall()
ps = [f"{id:<5}{name:<10}{intro:<20}{avatar}"
      for id, name, intro, avatar in stus]
print('\n'.join(ps))
