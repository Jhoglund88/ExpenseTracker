import sqlite3

conn = sqlite3.connect("expenses.db")


cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        category_id  INTEGER PRIMARY KEY,
        name  TEXT
    );
""")

def add_expense():
    amount = float(input("Ange belopp:"))
    description = input("Ange beskrivning:")
    category_id = int(input("Ange kategori-id:"))

    cursor.execute("""
        INSERT INTO expenses (amount, description, category_id)
        VALUES (?, ?, ?)
    """, (amount, description, category_id))

    conn.commit()

    print("Utgiften har sparats!")

add_expense()

conn.close()