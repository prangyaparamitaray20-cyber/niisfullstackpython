import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("INSERT INTO student VALUSE(2,'raja',95)")
conn.commit()
conn.close()
print("Data inserted succesfully")