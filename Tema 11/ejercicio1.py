import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

alu = input('Ingrese nombre del alumno: ')

query = f'SELECT * FROM Alumnos where nombre = "{alu}"'
rows=cursor.execute(query)

for row in rows:
    print(row)

cursor.close()
conn.close()