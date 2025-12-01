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

('Black Hat', 19.99, 'mens', 'assets/images/mens/blackhat.jpeg', 'Comfortable cotton tee', 200),
('Black Long-Sleeve Shirt', 19.99, 'mens', 'assets/images/mens/blackshirt.webp', 'Comfortable cotton tee', 200),
('Black Socks', 19.99, 'mens', 'assets/images/mens/blacksocks.webp', 'Comfortable cotton tee', 200),
('Blue Jacket', 19.99, 'mens', 'assets/images/mens/bluejacket.webp', 'Comfortable cotton tee', 200),
('Blue Jeans', 19.99, 'mens', 'assets/images/mens/bluejeans.webp', 'Comfortable cotton tee', 200),
('Blue T-Shirt', 19.99, 'mens', 'assets/images/mens/bluetee.jpeg', 'Comfortable cotton tee', 200),
('Brown Pants', 19.99, 'mens', 'assets/images/mens/brownpants.jpg', 'Comfortable cotton tee', 200),
('Dark Blue Jeans', 19.99, 'mens', 'assets/images/mens/darkbluejeans.webp', 'Comfortable cotton tee', 200),
('Dark Gray Jeans', 19.99, 'mens', 'assets/images/mens/darkgrayjeans.jpg', 'Comfortable cotton tee', 200),
('Gray Beanie', 19.99, 'mens', 'assets/images/mens/graybeanie.webp', 'Comfortable cotton tee', 200),
('Gray Long-Sleeve Shirt', 19.99, 'mens', 'assets/images/mens/grayshirt.webp', 'Comfortable cotton tee', 200),
('Gray Socks', 19.99, 'mens', 'assets/images/mens/graysocks.webp', 'Comfortable cotton tee', 200),
('Gray Sweat Pants', 19.99, 'mens', 'assets/images/mens/graysweatpants.jpg', 'Comfortable cotton tee', 200),
('Gray Beanie with Dark Gray Stripes', 19.99, 'mens', 'assets/images/mens/lightanddarkgraybeanie.jpg', 'Comfortable cotton tee', 200),
('Light Blue Jeans', 19.99, 'mens', 'assets/images/mens/lightbluejeans.webp', 'Comfortable cotton tee', 200),
('Light Gray Hoodie', 19.99, 'mens', 'assets/images/mens/lightgrayhoodie.webp', 'Comfortable cotton tee', 200),
('Light Green Shirt', 19.99, 'mens', 'assets/images/mens/lightgreenshirt.webp', 'Comfortable cotton tee', 200),
('Brown Suede Leather Jacket', 19.99, 'mens', 'assets/images/mens/rickgrimesjacket.jpg', 'Comfortable cotton tee', 200),
('White Hoodie', 19.99, 'mens', 'assets/images/mens/whitehoodie.jpg', 'Comfortable cotton tee', 200),
('White Socks', 19.99, 'mens', 'assets/images/mens/whitesocks.webp', 'Comfortable cotton tee', 200),
('Beige Long-Sleeve Shirt', 19.99, 'womens', 'assets/images/womens/beigelongsleeveshirt.jpeg', 'Comfortable cotton tee', 200),
('Black Scarf', 19.99, 'womens', 'assets/images/womens/blackscarf.webp', 'Comfortable cotton tee', 200),
('Black Socks', 19.99, 'womens', 'assets/images/womens/blacksocks.webp', 'Comfortable cotton tee', 200),
('Black Sweat Pants', 19.99, 'womens', 'assets/images/womens/blacksweatpants.jpeg', 'Comfortable cotton tee', 200),
('Gray Long-Sleeve Shirt', 19.99, 'womens', 'assets/images/womens/bluegraylongsleeveshirt.jpeg', 'Comfortable cotton tee', 200),
('Blue Jeans', 19.99, 'womens', 'assets/images/womens/bluejeans.jpeg', 'Comfortable cotton tee', 200),
('Blue Sweat Shirt', 19.99, 'womens', 'assets/images/womens/bluesweatshirt.webp', 'Comfortable cotton tee', 200),
('Brown and Black Scarf', 19.99, 'womens', 'assets/images/womens/brownandblackscarf.webp', 'Comfortable cotton tee', 200),
('Brown Leather Jacket', 19.99, 'womens', 'assets/images/womens/brownleatherjacket.webp', 'Comfortable cotton tee', 200),
('Brown Pants', 19.99, 'womens', 'assets/images/womens/brownpants.jpeg', 'Comfortable cotton tee', 200),
('Brown T-Shirt', 19.99, 'womens', 'assets/images/womens/browntshirt.jpg', 'Comfortable cotton tee', 200),
('Gray Jacket', 19.99, 'womens', 'assets/images/womens/grayjacket.jpeg', 'Comfortable cotton tee', 200),
('Gray Sweat Pants', 19.99, 'womens', 'assets/images/womens/graysweatpants.jpeg', 'Comfortable cotton tee', 200),
('Light Blue Jeans', 19.99, 'womens', 'assets/images/womens/lightbluejeans.webp', 'Comfortable cotton tee', 200),
('Light Blue Pants', 19.99, 'womens', 'assets/images/womens/lightbluepants.jpeg', 'Comfortable cotton tee', 200),
('Light Brown Shirt', 19.99, 'womens', 'assets/images/womens/lightbrownshirt.webp', 'Comfortable cotton tee', 200),
('Purple Blue', 19.99, 'womens', 'assets/images/womens/purpleblue.jpeg', 'Comfortable cotton tee', 200),
('Teel Long Sleeve Shirt', 19.99, 'womens', 'assets/images/womens/teellongsleeveshirt.jpeg', 'Comfortable cotton tee', 200),
('White Socks', 19.99, 'womens', 'assets/images/womens/whitesocks.webp', 'Comfortable cotton tee', 200),
('White Turtle Neck Shirt', 19.99, 'womens', 'assets/images/womens/whiteturtleneck.jpeg', 'Comfortable cotton tee', 200)
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
