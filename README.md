# GIODRIPPS - Fashion Killa Web Project

A modern, full-stack fashion e-commerce web application built with Flask, SQLite, and vanilla JavaScript. Browse curated style collections across men's, women's, and youth categories with a sleek shopping cart and checkout experience.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-blue)

---

## Tech Stack

### Backend
- **Flask** - Lightweight Python web framework
- **SQLite3** - Embedded relational database

### Frontend
- **HTML** - Semantic markup
- **CSS** - Modern styling with animations
- **JavaScript** - Interactive components and client-side logic
- **Font Awesome 7** - Icon library for UI elements

### Database
- SQLite with 90+ pre-populated products across all categories
- Product schema includes: id, name, price, category, image, description, stock

---

## Project Structure

```
FASHION-KILLA-WEB-PROJECT/
├── app.py                      # Main Flask application
├── create_db.py                # Database initialization script
├── index.html                  # Homepage
├── data/
│   └── products.db            # SQLite database
├── assets/
│   ├── images/
│   │   ├── homepage/          # Homepage banners
│   │   ├── mens/              # Men's product images
│   │   ├── womens/            # Women's product images
│   │   ├── youth/             # Youth product images
│   │   └── fits/              # Style collection images
│   └── extras/                # Fallback images
├── src/
│   ├── pages/                 # HTML page templates
│   │   ├── men.html           # Men's collection page
│   │   ├── women.html         # Women's collection page
│   │   ├── youth.html         # Youth collection page
│   │   ├── checkout.html      # Checkout & cart page
│   │   ├── collection.html    # Curated fits/collections
│   │   ├── search.html        # Search results page
│   │   ├── deals.html         # Promotions & deals
│   │   ├── aboutus.html       # About us page
│   │   └── help.html          # Help & support page
│   ├── scripts/               # JavaScript functionality
│   │   ├── header.js          # Header, menu, and cart dropdowns
│   │   ├── homepage.js        # Homepage interactions
│   │   ├── popup.js           # Product detail popups
│   │   └── deals.js           # Deals page functionality
│   └── styles/                # CSS stylesheets
│       ├── styles.css         # Global styles
│       ├── homepage.css       # Homepage styling
│       ├── bigmans.css        # Category page styling
│       ├── checkout.css       # Checkout page styling
│       ├── collection.css     # Collection page styling
│       ├── popup.css          # Popup styling
│       ├── deals.css          # Deals page styling
│       ├── help.css           # Help page styling
│       ├── aboutus.css        # About page styling
│       ├── youth.css          # Youth section styling
│       └── respectwhamen.css  # Women's section styling
└── LICENSE                    # MIT License
```

---

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
	```bash
	git clone https://github.com/SYKOMCHN/FASHION-KILLA-WEB-PROJECT.git
	cd FASHION-KILLA-WEB-PROJECT
	```

2. **Install dependencies**
	```bash
	pip install flask
	```

3. **Initialize the database**
	```bash
	python create_db.py
	```
	This will create `data/products.db` with 90+ pre-populated fashion items.

4. **Run the Flask application**
	```bash
	python app.py
	```

5. **Open in your browser**
	```
	http://127.0.0.1:5000
	```

---

## Usage

### Browsing Products
- **Homepage** (`/`) - View featured collections and category shortcuts
- **Men's Collection** (`/men`) - Browse 20+ men's streetwear items
- **Women's Collection** (`/women`) - Explore 30+ women's fashion pieces
- **Youth Collection** (`/youth`) - Shop 15+ youth-sized clothing
- **Collections** (`/collection`) - View curated style fits
- **Deals** (`/deals`) - Check out promotional items
- **Search** (`/search?q=keyword`) - Search across all products

### Shopping
1. **Add to Cart** - Click "Add to cart" on any product card
2. **View Cart** - Click the cart icon to see cart contents
3. **Checkout** - Navigate to checkout page to review order
4. **Purchase** - Complete transaction (payment simulation)
5. **Help** - Access FAQs and support information

---

## API Routes

### Product Routes
- `GET /` - Homepage
- `GET /men` - Men's collection
- `GET /women` - Women's collection  
- `GET /youth` - Youth collection
- `GET /collection` - Curated collections
- `GET /search?q=<query>` - Search products
- `GET /deals` - Promotions page

### Cart Routes
- `POST /add_to_cart/<product_id>` - Add item to cart
- `POST /remove_from_cart/<product_id>` - Remove item from cart
- `GET /cart_contents` - Get cart HTML fragment
- `GET /src/pages/checkout.html` - View checkout page
- `POST /purchase` - Complete purchase

### Collection Routes
- `GET /fit_contents/<fit_id>` - Get products in a specific style fit

---

## Database Schema

### Products Table
```sql
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  category TEXT,
  image TEXT,
  description TEXT,
  stock INTEGER DEFAULT 0
);
```

**Categories:**
- `mens` - Men's fashion (21 items)
- `womens` - Women's fashion (32 items)
- `youth` - Youth fashion (15 items)

---

## Key Features Explained

### Shopping Cart
- **Session-Based** - Cart persists for 30 days per session
- **Real-time Updates** - Add/remove items without page refresh
- **Dropdown Preview** - Quick view of cart contents
- **Quantity Tracking** - See item quantities and totals

### Search Functionality
- Searches across product name, description, and category
- Case-insensitive matching
- Real-time result display

### Style Collections
- Pre-curated fits with 4-9 items per collection
- Visual showcase of complete outfits
- Mix-and-match inspiration for customers

### Responsive Navigation
- Hamburger menu for mobile
- Search bar integrated into header
- Cart and help icons always accessible
- Smooth dropdown transitions

---

## Configuration

### Session Management
- Default session lifetime: 30 days
- Secret key: Configurable via `SECRET_KEY` environment variable
- Session storage: Server-side via Flask sessions

### Database Path
- Default location: `data/products.db`
- Automatically created on first run
- Configurable in `app.py` via `DB_PATH` variable

### Fallback Image
- Missing product images default to `assets/extras/yessir.png`
- Image URL prefix handling for relative paths

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 Oscar Huang**


---

**Built with ❤️ by the GIODRIPPS Team**
