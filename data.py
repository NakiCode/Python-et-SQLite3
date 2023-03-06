# 1.  IMPORTATION DU MODULE
import sqlite3
# 2. CREATION DE LA BASE DES DONNEES

conn = sqlite3.connect('data.db')
query = conn.cursor()
# 3. CREATION DES TABLES
query.execute("""
    CREATE TABLE IF NOT EXISTS 'Todo' (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'title' TEXT (50) NOT NULL,
        'desc' TEXT (100)
    )
""")

# 4. INSERTION DES DONNEES (INSERT)

# donnees = [('Apprendre', 'React Js'), ('Apprendre', 'Flutter'), ('Decouvrir', 'Django')]
# query.executemany("""
#     INSERT INTO Todo (title, desc) VALUES (?, ?)
# """, donnees)

# 5. SELECTION DES DONNEES (SELECT)

# query.execute("""
#     SELECT * FROM Todo
# """)
# response = query.fetchall()
# print(response[2][2])
# print(response[0], response[1], response[2])

# 6. MISE A JOUR DES DONNEES (UPDATE)

# donnees = ('Decouvrir', 1)
# query.execute("""
#     UPDATE Todo SET title=? WHERE id=?
# """, donnees)

# 7. SUPPRESSION DES DONNEES (DELETE)
donnees = (3,)
query.execute("""
    DELETE FROM Todo WHERE id = ?
""", donnees)


conn.commit()
conn.close()