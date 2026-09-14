import sqlite3
con = sqlite3.connect("tutorial.db") # соединение с базой данных, если бд нет, то файл создастся
cur = con.cursor()
cur.execute("CREATE TABLE status (status_name TEXT," \
            " status_id INTEGER PRIMARY KEY )")

cur.execute("CREATE TABLE projects (project_id INTEGER PRIMARY KEY," \
            "user_id INTEGER,project_name TEXT NOT NULL," \
            "description TEXT,url TEXT,status_id INTEGER," \
            "FOREIGN KEY(status_id) REFERENCES status(status_id))")

cur.execute("CREATE TABLE skills (skill_name TEXT," \
            "skill_id INTEGER PRIMARY KEY )")  

cur.execute("CREATE TABLE project_skills (project_id INTEGER ," \
            "skill_id INTEGER FOREIGN KEY, id INTEGER )")
con.commit()


con.close()