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

('Black Hat', 19.99, 'mens', 'assets/images/mens/blackhat.jpeg', 'Classic cotton baseball cap with adjustable strap — everyday wear.', 200),
('Black Long-Sleeve Shirt', 29.99, 'mens', 'assets/images/mens/blackshirt.webp', 'Soft long-sleeve tee in breathable cotton — great for layering.', 200),
('Black Socks', 7.99, 'mens', 'assets/images/mens/blacksocks.webp', 'Pack-style midweight crew socks with reinforced heel and toe.', 200),
('Blue Jacket', 89.99, 'mens', 'assets/images/mens/bluejacket.webp', 'Lightweight water-resistant jacket with zip pockets — ideal for transitional weather.', 200),
('Blue Jeans', 59.99, 'mens', 'assets/images/mens/bluejeans.webp', 'Classic straight-fit denim with slight stretch for comfort and durability.', 200),
('Blue T-Shirt', 19.99, 'mens', 'assets/images/mens/bluetee.jpeg', 'Everyday cotton tee with a relaxed fit and soft handfeel.', 200),
('Brown Pants', 44.99, 'mens', 'assets/images/mens/brownpants.jpg', 'Versatile chino-style pants with a tailored cut — smart-casual staple.', 200),
('Dark Blue Jeans', 64.99, 'mens', 'assets/images/mens/darkbluejeans.webp', 'Dark rinse denim with a modern slim cut and comfortable stretch.', 200),
('Dark Gray Jeans', 64.99, 'mens', 'assets/images/mens/darkgrayjeans.jpg', 'Stylish dark-gray denim offering a dressier look with everyday comfort.', 200),
('Gray Beanie', 14.99, 'mens', 'assets/images/mens/graybeanie.webp', 'Soft knit beanie that keeps you warm without being bulky.', 200),
('Gray Long-Sleeve Shirt', 29.99, 'mens', 'assets/images/mens/grayshirt.webp', 'Lightweight long-sleeve shirt in a neutral gray — great under jackets.', 200),
('Gray Socks', 7.99, 'mens', 'assets/images/mens/graysocks.webp', 'Comfort-fit crew socks with cushioned sole for daily wear.', 200),
('Gray Sweat Pants', 39.99, 'mens', 'assets/images/mens/graysweatpants.jpg', 'Soft fleece sweatpants with elastic waist and tapered ankle.', 200),
('Gray Beanie with Dark Gray Stripes', 16.99, 'mens', 'assets/images/mens/lightanddarkgraybeanie.jpg', 'Striped knit beanie with added stretch for a snug fit.', 200),
('Light Blue Jeans', 54.99, 'mens', 'assets/images/mens/lightbluejeans.webp', 'Light wash denim with vintage-inspired fading and comfortable fit.', 200),
('Light Gray Hoodie', 49.99, 'mens', 'assets/images/mens/lightgrayhoodie.webp', 'Classic pullover hoodie with kangaroo pocket and soft brushed interior.', 200),
('Light Green Shirt', 24.99, 'mens', 'assets/images/mens/lightgreenshirt.webp', 'Casual short-sleeve shirt in a fresh light-green hue.', 200),
('Brown Suede Leather Jacket', 249.99, 'mens', 'assets/images/mens/rickgrimesjacket.jpg', 'Premium suede leather jacket with classic cut — luxurious finish and build. (The Classic Rick Grimes Jacket)', 200),
('White Hoodie', 49.99, 'mens', 'assets/images/mens/whitehoodie.jpg', 'Clean, versatile pullover hoodie with moderate weight and comfy lining.', 200),
('White Socks', 6.99, 'mens', 'assets/images/mens/whitesocks.webp', 'Classic white crew socks with breathable cotton blend.', 200),
('Beige Long-Sleeve Shirt', 29.99, 'womens', 'assets/images/womens/beigelongsleeveshirt.jpeg', 'Soft beige long-sleeve top with a flattering relaxed fit.', 200),
('Black Scarf', 19.99, 'womens', 'assets/images/womens/blackscarf.webp', 'Lightweight woven scarf perfect for layering and adding polish to outfits.', 200),
('Black Socks', 7.99, 'womens', 'assets/images/womens/blacksocks.webp', 'Comfortable ankle socks with reinforced stitching for longevity.', 200),
('Black Sweat Pants', 39.99, 'womens', 'assets/images/womens/blacksweatpants.jpeg', 'Slim-fit sweatpants with drawstring waist and soft fleece interior.', 200),
('Gray Long-Sleeve Shirt', 29.99, 'womens', 'assets/images/womens/bluegraylongsleeveshirt.jpeg', 'Lightweight long-sleeve tee in heather gray — easy to dress up or down.', 200),
('Blue Jeans', 59.99, 'womens', 'assets/images/womens/bluejeans.jpeg', 'High-rise jeans with a flattering cut and durable stretch denim.', 200),
('Blue Sweat Shirt', 44.99, 'womens', 'assets/images/womens/bluesweatshirt.webp', 'Cozy crewneck sweatshirt with soft interior and relaxed silhouette.', 200),
('Brown and Black Scarf', 22.99, 'womens', 'assets/images/womens/brownandblackscarf.webp', 'Patterned scarf with warm tones that pairs well with neutral coats.', 200),
('Brown Leather Jacket', 199.99, 'womens', 'assets/images/womens/brownleatherjacket.webp', 'Genuine leather jacket with tailored fit and stylish hardware details.', 200),
('Brown Pants', 44.99, 'womens', 'assets/images/womens/brownpants.jpeg', 'Tailored brown trousers with stretch for comfort and a polished look.', 200),
('Brown T-Shirt', 19.99, 'womens', 'assets/images/womens/browntshirt.jpg', 'Everyday cotton tee in a warm brown shade — soft and breathable.', 200),
('Gray Jacket', 89.99, 'womens', 'assets/images/womens/grayjacket.jpeg', 'Lightweight, structured jacket suitable for work or weekend wear.', 200),
('Gray Sweat Pants', 39.99, 'womens', 'assets/images/womens/graysweatpants.jpeg', 'Comfy fleece sweatpants with a tapered leg and elastic cuff.', 200),
('Light Blue Jeans', 59.99, 'womens', 'assets/images/womens/lightbluejeans.webp', 'Light-wash high-rise jeans with a relaxed, on-trend fit.', 200),
('Light Blue Pants', 42.99, 'womens', 'assets/images/womens/lightbluepants.jpeg', 'Soft woven pants in pale blue — smart-casual and easy to style.', 200),
('Light Brown Shirt', 24.99, 'womens', 'assets/images/womens/lightbrownshirt.webp', 'Light-brown blouse with a fluid drape and button front.', 200),
('Purple Blue', 26.99, 'womens', 'assets/images/womens/purpleblue.jpeg', 'Vibrant purple-blue top with a flattering neckline and soft fabric.', 200),
('Teel Long Sleeve Shirt', 24.99, 'womens', 'assets/images/womens/teellongsleeveshirt.jpeg', 'Teal long-sleeve tee in a slim, comfortable cut for everyday wear.', 200),
('White Socks', 6.99, 'womens', 'assets/images/womens/whitesocks.webp', 'Lightweight white ankle socks with soft elastic cuff.', 200),
('White Turtle Neck Shirt', 34.99, 'womens', 'assets/images/womens/whiteturtleneck.jpeg', 'Classic ribbed turtleneck — warm, fitted, and great for layering.', 200),
('Ash T-Shirt', 14.99, 'youth', 'assets/images/youth/ashtshirt.jpeg', 'Soft ash-gray tee sized for kids — breathable and machine washable.', 200),
('Black Sweat Pants', 24.99, 'youth', 'assets/images/youth/blacksweatpants.jpeg', 'Kids sweatpants with elastic waist and cozy fleece lining.', 200),
('Blue Hat', 14.99, 'youth', 'assets/images/youth/bluehat.jpeg', 'Adjustable cotton cap sized for kids — durable and easy to wear.', 200),
('Blue Jeans', 29.99, 'youth', 'assets/images/youth/bluejeans.webp', 'Sturdy denim for kids with a comfortable fit and reinforced seams.', 200),
('Blue T-Shirt', 12.99, 'youth', 'assets/images/youth/bluetshirt.jpg', 'Bright blue kids tee made from soft, durable cotton.', 200),
('Dark Blue Socks', 6.99, 'youth', 'assets/images/youth/darkbluesocks.jpeg', 'Comfort socks for kids with a snug, non-slip fit.', 200),
('Dark Gray Socks', 6.99, 'youth', 'assets/images/youth/darkgraysocks.webp', 'Everyday kids socks in a dark gray shade — machine washable.', 200),
('Gray Pants', 24.99, 'youth', 'assets/images/youth/graypants.jpg', 'Durable kids pants with a straight cut and adjustable waist.', 200),
('Gray Sweat Pants', 24.99, 'youth', 'assets/images/youth/graysweatpants.jpeg', 'Cozy kids sweatpants with elastic cuffs and pocket details.', 200),
('Green T-Shirt', 12.99, 'youth', 'assets/images/youth/greentshirt.jpeg', 'Fun green tee for kids — soft cotton and comfortable fit.', 200),
('Light Pink T-Shirt', 12.99, 'youth', 'assets/images/youth/lightpinktshirt.jpeg', 'Soft light-pink tee perfect for everyday play and school.', 200),
('Pink Sweat Pants', 19.99, 'youth', 'assets/images/youth/pinksweatpants.webp', 'Lightweight kids sweatpants in pink with elastic waistband.', 200),
('White Socks', 6.99, 'youth', 'assets/images/youth/whitesocks.webp', 'Basic white socks for kids with breathable cotton blend.', 200),
('Yellow Shirt', 12.99, 'youth', 'assets/images/youth/yellowshirt.webp', 'Bright yellow kids shirt made from comfortable, easy-care fabric.', 200),
('Faux fur hooded jacket', 119.99, 'mens', 'assets/images/mens/furjacket.jpg', 'Faux fur hooded jacket designed to keep you warm and give you an elegant look.', 200),
('Black Baggy jeans with studs', 79.99, 'mens', 'assets/images/mens/dotteddenimpants.jpg', 'Black baggy denim jeans with studs made with real denim cotton', 200),
('Lace-up ankle boots', 89.99, 'mens', 'assets/images/mens/boots.jpg', 'Black lace-up ankle boots. Flexible technical latex foam insole, designed to offer greater comfort.', 200),
('Grey Zip-up sweatshirt', 59.99, 'mens', 'assets/images/mens/zipup.jpg', 'Grey Zip-up sweatshirt made to keep you comfortable and give you a smart look.', 200),
('Slim-fit henley long sleeve T-shirt', 25.99, 'mens', 'assets/images/mens/henley.jpg', 'An off white slim fit style henley shirt made with real cotton', 200),
('Basic grey beanie', 5.99, 'mens', 'assets/images/mens/basicbeanie.jpg', 'A grey basic beanie that goes well with all of your outfits', 200),
('Oversize burgundy felt coat ', 179.99, 'mens', 'assets/images/mens/oversizecoat.jpg', 'An oversized burgundy felt coat designed to keep you warm at all times.', 200),
('Black Tailored flared trousers', 67.99, 'mens', 'assets/images/mens/tailoredFlaredTrousers.jpg', 'Tailored flared trouses that are designed to give you a mix of baggy and straight pants in one.', 200),
('Leather effect gloves', 15.99, 'mens', 'assets/images/mens/leathereffectgloves.jpg', 'Made with real leather to give you that shiny look and the warmth.', 200),
('Loafers with chunky soles', 69.99, 'mens', 'assets/images/mens/loaferswithchunkysoles.jpg', 'STARFIT®. Flexible technical latex foam insole, designed to offer greater comfort.', 200),
('Light blue Sweater with polo collar', 49.99, 'mens', 'assets/images/mens/sweaterwithpolocollar.jpg', 'Ligth blue polo collar sweater made for casual wear and warmth.', 200),
('Dark grey balloon fit flannel pants', 69.99, 'mens', 'assets/images/mens/balloonfitflannelpants.jpg', 'A ballon cut pair of pants made for that baggy look that everyone seeks for.', 200),
('Embroidered LEATHER clogs with buckle', 79.99, 'mens', 'assets/images/mens/embroideredleatherclogswithbuckle.jpg', 'AIRFIT®. Flexible technical latex foam insole, designed to offer greater comfort.', 200),
('Burgundy leather effect boxy fit jacket', 79.99, 'mens', 'assets/images/mens/leathereffectboxyfitjacket.jpg', 'Burgundy boxy leather fitted jacket designed to give you that wide look.', 200),
('Black oversize leather effect jacket', 79.99, 'womens', 'assets/images/womens/oversizeleather.jpg', 'An oversize black leather jacket made with poleyster.', 200),
('White oversize balloon T-shirt dress', 29.99, 'womens', 'assets/images/womens/oversizeballoont.jpg', 'Designed to be layered by another outwear piece.', 200),
('Black heeled boots with buckle', 128.99, 'womens', 'assets/images/womens/heeledbootswithbuckle.jpg', 'Heel height: 9 cm. Leg height: 37 cm. Leg width: 18 cm. AIRFIT®. Flexible technical latex foam insole, designed to offer greater comfort.', 200),
('Asymmetric striped knit sweater', 34.99, 'womens', 'assets/images/womens/asymmetricstripedknitsweater.jpg', 'A stripped knitted sweater with a shoulder drop.', 200),
('Grey plush barrel pants with stoppers', 45.99, 'womens', 'assets/images/womens/plushbarrelpantswithstoppers.jpg', 'Grey plush barrel sweat pants made with real cotton designed to keep you comfortable and warm.', 200),
('Black high-heel ballerinas', 47.99, 'womens', 'assets/images/womens/highheelballerinas.jpg', 'Heel height: 4 cm. AIRFIT®. Flexible technical latex foam insole, designed to offer greater comfort.', 200),
('Black long sleeve floral top', 34.99, 'womens', 'assets/images/womens/longsleevefloraltop.jpg', 'Blacl floral long sleeve with exposed shoulders.', 200),
('Black flared draped flower trousers', 49.99, 'womens', 'assets/images/womens/flareddrapedflowertrousers.jpg', 'Slim fitted black flared draped flower trousers.', 200),
('Black faux fur bag', 45.99, 'womens', 'assets/images/womens/fauxfurbag.jpg', 'Black faux fur bag made with real fur.', 200),
('Black ankle strap wedge heel shoe', 76.99, 'womens', 'assets/images/womens/anklestrapwedgeheelshoe.jpg', 'Heel height: 3.5 inches. AIRFIT®. Flexible technical latex foam insole, designed for enhanced comfort.', 200),
('Black bronco leather bomber jacket', 47.99, 'womens', 'assets/images/womens/broncoleatherbomberjacket.jpg', 'Crafted from durable vegan leather, this classic bomber jacket offers a smooth, flexible fit with a sleek zip closure and snap-button wrist cuffs for an added touch of structure.', 200),
('Black rib spaghetti tank', 12.99, 'womens', 'assets/images/womens/theribs.jpg', 'A year-round essential, effortlessly versatile for layering or wearing solo. Designed with a scoop neck, spaghetti straps, and a fine rib texture that provides the perfect amount of hold—no bra required.', 200),
('Grey Mid Rise Pleated Wide Leg Trousers', 34.99, 'womens', 'assets/images/womens/greypants.jpg', 'A regular fit type with a mid rise waist line.', 200),
('Black Nike Air Monarch IV', 99.99, 'womens', 'assets/images/womens/nike.jpg', 'Nike Air Monarch IV sets you up for working out with durable leather on top for support. Lightweight foam teams up with Nike Air cushioning for comfort in every stride.', 200)




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
