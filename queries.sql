SELECT * FROM categories;

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

SELECT * FROM categories;

