SELECT * FROM categories;

CREATE TABLE IF NOT EXISTS expenses (
        expense_id INTEGER PRIMARY KEY,
        amount REAL,
        description TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

INSERT INTO expenses (amount, description, category_id)
VALUES (149.90, 'Lunch', 1);

SELECT expenses.description, expenses.amount, categories.name
FROM expenses
JOIN categories
ON expenses.category_id = categories.category_id;

SELECT expenses.description, expenses.amount, categories.name
FROM expenses
JOIN categories
ON expenses.category_id = categories.category_id
WHERE expenses.amount > 100;

SELECT expenses.description, expenses.amount, categories.name
FROM expenses
JOIN categories
ON expenses.category_id = categories.category_id
WHERE categories.name = 'mat'
ORDER BY amount ASC;

SELECT * FROM expenses;