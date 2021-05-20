import sqlite3

def createTable(query):
    con = sqlite3.connect("COLLEGE.db")
    cur = con.cursor()
    cur.execute(query)
    cur.execute("INSERT INTO STUDENT('ROLLNO', 'NAME') VALUES(?, ?)",(1, "Sana"))
    con.commit()
    cur.close()
    con.close()

if __name__ == "__main__":
    query = "CREATE TABLE IF NOT EXISTS \
        STUDENT(ROLLNO INTEGER PRIMARY KEY, NAME TEXT NOT NULL, sex TEXT, age INTEGER, \
        address TEXT, famsize TEXT,\
        Medu INTEGER, Fedu INTEGER, Mjob TEXT, Fjob TEXT, guardian TEXT, \
        traveltime INTEGER, studytime INTEGER, \
        failures INTEGER, schoolsup TEXT, famsup TEXT, paid TEXT, activities TEXT, \
        higher TEXT, internet TEXT, \
        romantic TEXT, freetime, goout INTEGER, Walc INTEGER, health INTEGER, \
        absences INTEGER, G1 INTEGER)"
    createTable(query)
