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
    try:
        amount = float(input("Ange belopp:"))
    except ValueError:
        print("Ogiltigt belopp. Försök igen.")
        return

    if amount <= 0:
        print("Beloppet måste vara större än noll. Försök igen.")
        return
    
    description = input("Ange beskrivning:")

    cursor.execute("SELECT category_id, name FROM categories")
    categories = cursor.fetchall()

    print("\nTillgängliga kategorier:")
    for category_id, name in categories:
        print(f"{category_id}. {name}")

    try:
        category_id = int(input("Ange kategori-id:"))
    except ValueError:
        print("Ogiltigt kategori-id. Försök igen.")
        return

    valid_ids = [id for id, name in categories]

    if category_id not in valid_ids:
        print("Ogiltigt kategori-id. Försök igen.")
        return

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

def show_category_totals():
    cursor.execute("""
        SELECT categories.name,
               SUM(expenses.amount) AS total_amount
        FROM expenses
        INNER JOIN categories
            ON expenses.category_id = categories.category_id
        GROUP BY categories.name
        ORDER BY total_amount DESC
    """)
    category_totals = cursor.fetchall()

    for category, total in category_totals:
        print(f"{category}: {total:.2f} kr")

while True:
    print("\nVälj ett alternativ:")
    print("1. Lägg till utgift")
    print("2. Visa alla utgifter")
    print("3. Visa totaler per kategori")
    print("4. Avsluta")

    choice = input("Ange ditt val (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_category_totals()
    elif choice == "4":
        break
    else:
        print("Ogiltigt val. Försök igen.")

conn.close()