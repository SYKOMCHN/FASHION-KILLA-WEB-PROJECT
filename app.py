import os
import sqlite3
from flask import Flask, g, render_template, jsonify, request, abort, url_for

app = Flask(__name__, static_folder='.', static_url_path='', template_folder='.')

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "products.db")



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


@app.route("/src/pages/men.html")
def men_page():
    products = query_products(category="mens")
    return render_template("src/pages/men.html", products=products)


# convenience route
@app.route("/men")
def men_short():
    products = query_products(category="mens")
    return render_template("src/pages/men.html", products=products)

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


if __name__ == "__main__":
    
    app.run(debug=True, host="127.0.0.1", port=5000)