import sqlite3
import os

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "products.db")


# creates the SQlite database schema and fill with example data until we decide on products
SCHEMA_AND_SEED = """
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  category TEXT,
  image TEXT,
  description TEXT,
  stock INTEGER DEFAULT 0
);

INSERT INTO products (name, price, category, image, description, stock) VALUES
('Black Tee', 19.99, 'mens', 'assets/extras/yessir.png', 'Comfortable cotton tee', 20),
('Denim Jacket', 59.99, 'mens', 'assets/extras/yessir.png', 'Classic denim jacket', 8),
('breBlack Tee', 19.99, 'mens', 'assets/extras/yessir.png', 'Comfortable cotton tee', 20),
('erbdtDenim Jacket', 59.99, 'mens', 'assets/extras/yessir.png', 'Classic denim jacket', 8),
('rtdtdrtBlack Tee', 19.99, 'mens', 'assets/extras/yessir.png', 'Comfortable cotton tee', 20),
('Dedrtdrnim Jacket', 59.99, 'mens', 'assets/extras/yessir.png', 'Classic denim jacket', 8),
('Blrtack Tee', 19.99, 'mens', 'assets/extras/yessir.png', 'Comfortable cotton tee', 20),
('Dendrtim Jacket', 59.99, 'mens', 'assets/extras/yessir.png', 'Classic denim jacket', 8),
('Bladck Tee', 19.99, 'mens', 'assets/extras/yessir.png', 'Comfortable cotton tee', 20),
('Dedrtnim Jacket', 59.99, 'mens', 'assets/extras/yessir.png', 'Classic denim jacket', 8),
('White Sneakers', 79.99, 'womens', 'assets/extras/yessir.png', 'Lightweight running sneakers', 12);
"""


def create_db():
    os.makedirs(DB_DIR, exist_ok=True)
    first_time = not os.path.exists(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    try:
        if first_time:
            conn.executescript(SCHEMA_AND_SEED)
        else:
            print(f"DB already exists — no changes made.")
    finally:
        conn.close()

if __name__ == "__main__":
    create_db()
