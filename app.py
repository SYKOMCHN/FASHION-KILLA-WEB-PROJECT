from flask import Flask, g, render_template, jsonify, request, abort, url_for, session, redirect, render_template_string
import sqlite3, os

from datetime import timedelta

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='.')

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "products.db")


# keep session for 30 days
app.permanent_session_lifetime = timedelta(days=30)


# key for sessions
app.secret_key = os.environ.get("SECRET_KEY", "boopyboopboope")

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def query_products(category=None):
    db = get_db()
    cur = db.cursor() # object to execute queries
    if category:
        cur.execute("SELECT * FROM products WHERE LOWER(category)=LOWER(?)", (category,))
    else:
        cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    products = []
    for r in rows:
        p = dict(r) # convert the rows to regular dicts
        img = p.get("image") or ""
        # need to prefix '../../'
        if img and not (img.startswith("/") or img.startswith("..")):
            p["img_url"] = "../../" + img
        else:
            p["img_url"] = img or "../../assets/extras/yessir.png"
        products.append(p)
    return products


@app.route("/")
def index():
    return render_template("index.html")


# mens page
@app.route("/src/pages/men.html")
def men_page():
    products = query_products(category="mens")
    return render_template("src/pages/men.html", products=products)


# convenience route
@app.route("/men")
def men_short():
    products = query_products(category="mens")
    return render_template("src/pages/men.html", products=products)


# women page
@app.route("/src/pages/women.html")
def women_page():
    products = query_products(category="womens")
    return render_template("src/pages/women.html", products=products)

@app.route("/women")
def women_short():
    products = query_products(category="womens")
    return render_template("src/pages/women.html", products=products)


# youth page
@app.route("/src/pages/youth.html")
def youth_page():
    products = query_products(category="youth")
    return render_template("src/pages/youth.html", products=products)

@app.route("/youth")
def youth_short():
    products = query_products(category="youth")
    return render_template("src/pages/youth.html", products=products)




# search route
@app.route("/search")
def search():
    q = (request.args.get("q") or "").strip() # get the search query
    products = []
    if q:
        db = get_db()
        cur = db.cursor()
        like = f"%{q}%"
        cur.execute(
            """
            SELECT * FROM products
            WHERE LOWER(name) LIKE LOWER(?)
               OR LOWER(description) LIKE LOWER(?)
               OR LOWER(category) LIKE LOWER(?)
            """,
            (like, like, like),
        )
        rows = cur.fetchall()
        for r in rows:
            p = dict(r)
            img = p.get("image") or ""
            if img and not (img.startswith("/") or img.startswith("..")):
                p["img_url"] = "../../" + img
            else:
                p["img_url"] = img or "../../assets/extras/yessir.png"
            products.append(p)

    # render the search.html page with the results
    return render_template("src/pages/search.html", products=products, query=q)





# add item to cart
@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart = dict(cart)
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    session.permanent = True
    return ("", 204)

# remove item from cart (POST)
@app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    key = str(product_id)
    if key in cart:
        del cart[key]
        session["cart"] = cart
    return ("", 204)

# return HTML fragment for cart dropdown
@app.route("/cart_contents")
def cart_contents():
    cart = session.get("cart", {})
    if not cart:
        return '<div style="padding:12px;">Your cart is empty.</div>'

    db = get_db()
    cur = db.cursor()
    ids = [int(k) for k in cart.keys()]
    placeholders = ",".join("?" * len(ids))
    cur.execute(f"SELECT id, name, price, image FROM products WHERE id IN ({placeholders})", ids)
    rows = cur.fetchall()

    total = 0.0
    items_html = ""
    for r in rows:
        p = dict(r)
        qty = cart.get(str(p["id"]), 1)
        total += p["price"] * qty
        img = p.get("image") or ""
        img_url = ("../../" + img) if (img and not (img.startswith("/") or img.startswith(".."))) else (img or "../../assets/extras/yessir.png")

        items_html += f'''
        <div class="cart-item" data-id="{p["id"]}" style="display:flex;gap:8px;padding:8px;border-bottom:1px solid rgba(0,0,0,0.06);align-items:center;">
          <img src="{img_url}" alt="{p["name"]}" style="width:50px;height:50px;object-fit:cover;border-radius:6px;">
          <div style="flex:1;">
            <div style="font-weight:bold;font-size:0.9rem;">{p["name"]}</div>
            <div style="font-size:0.85rem;">${p["price"]:.2f} x {qty}</div>
          </div>
          <button class="cart-remove" data-id="{p['id']}" style="border:none;background:#c22;color:#fff;padding:6px 8px;border-radius:6px;cursor:pointer;">Remove</button>
        </div>
        '''

    items_html += f'''
      <div style="padding:8px 8px 0 8px;"><strong>Total: ${total:.2f}</strong></div>
      <div style="padding:10px;">
        <button id="checkout_btn" style="width:100%;padding:8px;border-radius:8px;border:none;cursor:pointer;background:rgb(28,28,28);color:#fff;">Go to checkout</button>
      </div>
    '''
    return items_html





if __name__ == "__main__":
    
    app.run(debug=True, host="127.0.0.1", port=5000)