from database.models import get_db, init_db
import random

def seed():
    init_db()
    db = get_db()
    cur = db.cursor()

    # Clear old data
    cur.execute("DELETE FROM shops")
    cur.execute("DELETE FROM products")
    cur.execute("DELETE FROM shop_products")

    # Shops
    shops = [
        "Aashiyana",
        "FPO 2",
        "Achyutam",
        "Kisan Jaivik Utpadak Sangathan",
        "Green Valley",
        "Desi Organic",
        "Farm Fresh",
        "Nature Basket",
        "Healthy Harvest",
        "Vedic Foods"
    ]

    for shop in shops:
        cur.execute("INSERT INTO shops (name) VALUES (?)", (shop,))

    # Products
    products = [
        ("Masoor Dal", "/static/images/products/masoor.jpg", "dal"),
        ("Arhar Dal", "/static/images/products/arhar.jpg", "dal"),
        ("Moong Chhilka Dal", "/static/images/products/moong.jpg", "dal"),
        ("Urad Chhilka Dal", "/static/images/products/urad.jpg", "dal"),
        ("Chana Dal", "/static/images/products/chana.jpg", "dal"),
        ("Toor Dal", "/static/images/products/toor.jpg", "dal"),
        ("Vedic Dal Combo", "/static/images/products/vedic.jpg", "dal")
    ]

    for p in products:
        cur.execute("INSERT INTO products (name, image, category) VALUES (?,?,?)", p)

    # Random mapping
    for shop_id in range(1, 11):
        for product_id in range(1, 7):
            price = random.randint(80, 150)
            cur.execute("""
            INSERT INTO shop_products (shop_id, product_id, price)
            VALUES (?,?,?)
            """, (shop_id, product_id, price))

    # Special: Kisan shop (id=4) only 4 dal
    cur.execute("DELETE FROM shop_products WHERE shop_id = 4")

    for product_id in range(1, 5):
        cur.execute("""
        INSERT INTO shop_products (shop_id, product_id, price)
        VALUES (?,?,?)
        """, (4, product_id, 120))

    db.commit()
    print("Final marketplace ready ✅")