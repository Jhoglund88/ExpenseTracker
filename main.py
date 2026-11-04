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
    SELECT expenses.expense_id, expenses.amount, expenses.description, categories.name
    FROM expenses
    JOIN categories
    ON expenses.category_id = categories.category_id
""")
    expenses = cursor.fetchall()

    for expense in expenses:
        print(f"ID: {expense[0]} - {expense[1]}kr - {expense[2]} - {expense[3]}")

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

def delete_expense():
    while True:
        try:
            delete_choice = int(input("Ange ID för utgiften du vill ta bort:"))
            break
        except ValueError:
            print("\nOgiltigt ID. Försök igen.")
            

    cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (delete_choice,))
    conn.commit()

    if cursor.rowcount == 0:
        print("Inget ID matchar det numret")
    else:
        print("Valt ID har tagits bort")

def update_expenses():
    show_expenses()
    while True:
        try:
            update_choice = int(input("Ange ID för utgiften du vill uppdatera:"))
            break
        except ValueError:
            print("\nOgiltigt ID. Försök igen.")

    cursor.execute("SELECT * FROM expenses WHERE expense_id = ?", (update_choice,))
    expense = cursor.fetchone()

    if expense is None:
        print("Inget ID matchar det numret")
        return

    try:
        new_amount = float(input("Ange nytt belopp:"))
    except ValueError:
        print("Ogiltigt belopp. Försök igen.")
        return

    if new_amount <= 0:
        print("Beloppet måste vara större än noll. Försök igen.")
        return

    new_description = input("Ange ny beskrivning:")

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, description = ?
        WHERE expense_id = ?
    """, (new_amount, new_description, update_choice))

    conn.commit()

    print("Utgiften har uppdaterats!")

def show_recent_expenses():
    cursor.execute("""
       SELECT * FROM expenses
    ORDER BY expense_id DESC
    LIMIT 10; """)

    for expense in cursor.fetchall():
        print(f"ID: {expense[0]} - {expense[1]}kr - {expense[2]} - Kategori ID: {expense[3]}")

   
       

while True:
    print("\nVälj ett alternativ:")
    print("1. Lägg till utgift")
    print("2. Visa alla utgifter")
    print("3. Visa totaler per kategori")
    print("4. Ta bort utgift")
    print("5. Uppdatera utgift")
    print("6. Avsluta")

    choice = input("Ange ditt val (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_category_totals()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        update_expenses()
    elif choice == "6":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val. Försök igen.")

conn.close()