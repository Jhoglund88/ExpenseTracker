CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS expenses (
        expense_id INTEGER PRIMARY KEY,
        amount REAL,
        description TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
);