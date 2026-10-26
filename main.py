import sqlite3

conn = sqlite3.connect("expenses.db")

conn.execute("PRAGMA foreign_keys = ON")


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

def show_expenses():
    cursor.execute("""
    SELECT expenses.amount, expenses.description, categories.name
    FROM expenses
    JOIN categories
    ON expenses.category_id = categories.category_id
""")
    expenses = cursor.fetchall()

    for expense in expenses:
        print(f"{expense[0]} kr - {expense[1]} - {expense[2]}")

add_expense()
show_expenses()
conn.close()