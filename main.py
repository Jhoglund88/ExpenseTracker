import sqlite3

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        category_id  INTEGER PRIMARY KEY,
        name  TEXT
    );
""")

# cursor.execute("""
#     INSERT INTO categories (name)
#     VALUES ('mat');
# """)

# cursor.execute("""
#     INSERT INTO categories (name)
#     VALUES ('Transport');
# """) 

cursor.execute("""
    DELETE FROM categories
    WHERE category_id > 2;
""")

cursor.execute("""
    SELECT * FROM categories;
""")

rows = cursor.fetchall()
print(rows)

conn.commit()
conn.close()