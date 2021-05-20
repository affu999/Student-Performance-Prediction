import sqlite3

def createTable():
    con = sqlite3.connect("COLLEGE.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ADMIN(ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
    cur.execute("INSERT INTO ADMIN VALUES(?, ?, ?)",(1, "Affan", "12345"))
    con.commit()
    cur.close()
    con.close()

if __name__ == "__main__":
    createTable()
