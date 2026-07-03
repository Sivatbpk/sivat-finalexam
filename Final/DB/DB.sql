CREATE TABLE users (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    wallet_balance NUMERIC(10, 2) DEFAULT 0.00
);

CREATE TABLE orders (
    queue_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    menu VARCHAR(100) NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);


INSERT INTO users (name, wallet_balance) VALUES 
('Somchai Deeja', 500.00),
('Somsri Rakdee', 150.00),
('Anan Wongsa', 20.00);

INSERT INTO orders (menu, total_price, status) VALUES 
('Kao Man Gai (Chicken Rice)', 50.00, 'Pending'),
('Pad Thai', 60.00, 'Pending'),
('Som Tum (Papaya Salad)', 45.00, 'Ready'),
('Kao Pad Kung (Shrimp Fried Rice)', 65.00, 'Pending');

UPDATE orders 
SET status = 'Ready' 
WHERE queue_id = 1;


SELECT queue_id, menu, total_price, status 
FROM orders 
WHERE status = 'Pending';