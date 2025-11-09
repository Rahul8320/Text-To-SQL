import sqlite3
import random
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect("mySql.db")
cursor = conn.cursor()

# Drop tables if exist (for clean start)
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS addresses")
cursor.execute("DROP TABLE IF EXISTS order_items")

# Create tables
cursor.execute("""CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT
)""")

cursor.execute("""CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    street TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)""")

cursor.execute("""CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)""")

cursor.execute("""CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATE,
    ship_address_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(ship_address_id) REFERENCES addresses(address_id)
)""")

cursor.execute("""CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)""")

# Insert dummy customers
customer_names = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Ethan",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Jane",
]
emails = [f"user{i}@example.com" for i in range(1, 11)]
phones = [
    "123-456-7890",
    "234-567-8901",
    "345-678-9012",
    "456-789-0123",
    "567-890-1234",
    "678-901-2345",
    "789-012-3456",
    "890-123-4567",
    "901-234-5678",
    "012-345-6789",
]

for i in range(10):
    cursor.execute(
        "INSERT INTO customers(name, email, phone) VALUES (?, ?, ?)",
        (customer_names[i], emails[i], phones[i]),
    )

# Insert dummy addresses
streets = [
    "123 Elm St",
    "456 Oak St",
    "789 Pine St",
    "101 Maple Ave",
    "202 Birch Ave",
    "303 Cedar Blvd",
    "404 Ash Blvd",
    "505 Walnut Rd",
    "606 Chestnut Rd",
    "707 Spruce Ln",
]
cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose",
]
states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
zips = [
    "10001",
    "90001",
    "60601",
    "77001",
    "85001",
    "19101",
    "78201",
    "92101",
    "75201",
    "95101",
]

for i in range(10):
    cursor.execute(
        "INSERT INTO addresses(customer_id, street, city, state, zip_code) VALUES (?, ?, ?, ?, ?)",
        (i + 1, streets[i], cities[i], states[i], zips[i]),
    )

# Insert dummy products
product_names = [f"Product-{i}" for i in range(1, 31)]
descriptions = [f"Description for product {i}" for i in range(1, 31)]
prices = [round(random.uniform(10.0, 100.0), 2) for _ in range(30)]
for i in range(30):
    cursor.execute(
        "INSERT INTO products(name, description, price) VALUES (?, ?, ?)",
        (product_names[i], descriptions[i], prices[i]),
    )

# Insert dummy orders
base_date = datetime.today()
for i in range(50):
    customer_id = random.randint(1, 10)
    order_date = base_date - timedelta(days=random.randint(1, 365))
    ship_address_id = customer_id  # For simplicity, address_id is same as customer_id
    cursor.execute(
        "INSERT INTO orders(customer_id, order_date, ship_address_id) VALUES (?, ?, ?)",
        (customer_id, order_date.strftime("%Y-%m-%d"), ship_address_id),
    )

# Insert dummy order items, each order having 1-5 products randomly
order_ids = [row[0] for row in cursor.execute("SELECT order_id FROM orders").fetchall()]
product_ids = [
    row[0] for row in cursor.execute("SELECT product_id FROM products").fetchall()
]

for order_id in order_ids:
    num_items = random.randint(1, 5)
    for _ in range(num_items):
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 3)
        cursor.execute(
            "INSERT INTO order_items(order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, product_id, quantity),
        )

conn.commit()
conn.close()

print("Database created and populated with dummy data.")
