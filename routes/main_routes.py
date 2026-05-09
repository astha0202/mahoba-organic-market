from flask import Blueprint, render_template, request
from flask import jsonify
main_bp = Blueprint("main", __name__)

# 🔹 Shops
shops_data = [
    {"id":1,"name":"Aashiyana","image":"/static/images/shops/aashiyana.png"},
    {"id":2,"name":"FPO 2","image":"/static/images/shops/default.jpg"},
    {"id":3,"name":"Achyutam","image":"/static/images/shops/default.jpg"},
    {"id":4,"name":"Kisan Jaivik Utpadak Sangathan","image":"/static/images/shops/default.jpg"},
    {"id":5,"name":"Green Valley","image":"/static/images/shops/default.jpg"},
    {"id":6,"name":"Desi Organic","image":"/static/images/shops/default.jpg"},
    {"id":7,"name":"Farm Fresh","image":"/static/images/shops/default.jpg"},
    {"id":8,"name":"Nature Basket","image":"/static/images/shops/default.jpg"},
    {"id":9,"name":"Healthy Harvest","image":"/static/images/shops/default.jpg"},

    # 🔥 VEDIC SPECIAL IMAGE
    {"id":10,"name":"Vedic Foods","image":"/static/images/shops/vedic.jpg"}
]

# 🔹 Products
products_data =[
    {'product_id': 101, 'name_en': 'Masoor Dal 1 Kg', 'name_hi': 'मसूर दाल 1 किलो', 'price': 170, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/masoor1kg.jpg'} ,
    {'product_id': 102, 'name_en': 'Sabudana Chana 1 Kg', 'name_hi': 'साबुत चना 1 किलो', 'price': 130, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/chana1kg.jpg'} ,
    {'product_id': 103, 'name_en': 'Sabut Masoor 1 Kg', 'name_hi': 'साबुत मसूर 1 किलो', 'price': 130, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sabutmasoor.jpg'} ,
    {'product_id': 104, 'name_en': 'Chana Dal 1kg', 'name_hi': 'चना दाल 1kg', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/chanadal.jpg'} ,
    {'product_id': 105, 'name_en': 'Bajre ka Atta', 'name_hi': 'बाजरे का आटा', 'price': 70, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/bajra.jpg'} ,
    {'product_id': 106, 'name_en': 'Organic Makka atta', 'name_hi': 'जैविक मक्का आटा', 'price': 70, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/makka.jpg'} ,
    {'product_id': 107, 'name_en': 'Jowar ka atta', 'name_hi': 'ज्वार का आटा', 'price': 80, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/jwar.jpg'} ,
    {'product_id': 108, 'name_en': 'Organic Yellow Mustard Oil 500 ml', 'name_hi': 'जैविक पीली सरसों का तेल 500 ml', 'price': 150, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sarso500.jpg'} ,
    {'product_id': 109, 'name_en': 'Yellow Mustard Oil 1 litre', 'name_hi': 'पीली सरसों का तेल 1 लीटर', 'price': 300, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sarso1l.jpg'} ,
    {'product_id': 110, 'name_en': 'Normal Wheat flour 5kg', 'name_hi': 'सामान्य गेहूं आटा 5kg', 'price': 250, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/gehu5kg.jpg'} ,
    {'product_id': 111, 'name_en': 'Multigrain flour 5kg', 'name_hi': 'मल्टीग्रेन आटा 5kg', 'price': 400, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/multigrain5kg.jpg'} ,
    {'product_id': 112, 'name_en': 'Kathiya Wheat Flour 5 Kg', 'name_hi': 'कठिया गेहूं आटा 5 किलो', 'price': 425, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kathiya5kg.jpg'} ,
    {'product_id': 113, 'name_en': 'Moong Dal 1kg', 'name_hi': 'मूंग दाल 1kg', 'price': 180, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/moong1kg.jpg'} ,
    {'product_id': 114, 'name_en': 'Besan 1 Kg', 'name_hi': 'बेसन 1 किलो', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/besan1kg.jpg'} ,
    {'product_id': 115, 'name_en': 'Besan 500 Gram', 'name_hi': 'बेसन 500 ग्राम', 'price': 80, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/besan500.jpg'} ,
    {'product_id': 116, 'name_en': 'Organic Barley Flour 1 Kg', 'name_hi': 'जैविक जौ आटा 1 किलो', 'price': 60, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/jau1kg.jpg'} ,
    {'product_id': 117, 'name_en': 'Moong Dal 500 Gram', 'name_hi': 'मूंग दाल 500 ग्राम', 'price': 90, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/moong500.jpg'} ,
    {'product_id': 118, 'name_en': 'Organic Urad Dal 500 Gram', 'name_hi': 'जैविक उड़द दाल 500 ग्राम', 'price': 85, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/urad500.jpg'} ,
    {'product_id': 119, 'name_en': 'Black Wheat Flour 5 Kg', 'name_hi': 'काला गेहूं का आटा 5 किलो', 'price': 400, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kalagehu5kg.jpg'} ,
    {'product_id': 120, 'name_en': 'Black Wheat Flour 2 Kg', 'name_hi': 'काला गेहूं आटा 2 किलो', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kalagehu2kg.jpg'} ,
    {'product_id': 121, 'name_en': 'Organic Kathiya Flour 2 Kg', 'name_hi': 'जैविक कठिया आटा 2 किलो', 'price': 170, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kathiya2kg.jpg'} ,
    {'product_id': 122, 'name_en': 'Organic Sabut masoor 500 Gram', 'name_hi': 'जैविक साबुत मसूर 500 ग्राम', 'price': 65, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sabutmasoor500.jpg'} ,
    {'product_id': 123, 'name_en': 'Organic Masoor Dal 500 Gram', 'name_hi': 'जैविक मसूर दाल 500 ग्राम', 'price': 85, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/masoor500.jpg'} ,
    {'product_id': 124, 'name_en': 'Mix Dal 500 Gram', 'name_hi': 'पंचरंगी दाल 500 ग्राम', 'price': 90, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/panchrangi.jpg'} ,
    {'product_id': 125, 'name_en': 'Sabut Moong 1 Kg', 'name_hi': 'साबुत मूंग 1 किलो', 'price': 140, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sabutmoong.jpg'}, 
    {'product_id': 126, 'name_en': 'Mustard Oil 1 litre', 'name_hi': 'सरसों तेल 1 लीटर', 'price': 260, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sarsooil.jpg'} ,
    {'product_id': 127, 'name_en': 'Multigrain Flour 2 Kg', 'name_hi': 'मल्टीग्रेन आटा 2 किलो', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/multigrain2kg.jpg'} ,
    {'product_id': 128, 'name_en': 'Urad Dal 1kg', 'name_hi': 'उड़द दाल 1kg', 'price': 170, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/urad1kg.jpg'} ,
    {'product_id': 129, 'name_en': 'Chana Sattu 500 Gram', 'name_hi': 'चना सत्तू 500 ग्राम', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sattu.jpg'} ,
    {'product_id': 130, 'name_en': 'Stuffed Red Chilli Pickle 500 Gram', 'name_hi': 'भरवा लाल मिर्च अचार 500 ग्राम', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/achar.jpg'} ,
    {'product_id': 131, 'name_en': 'Arhar Dal 1kg', 'name_hi': 'अरहर दाल 1kg', 'price': 190, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/arhar1kg.jpg'} ,
    {'product_id': 132, 'name_en': 'Foxtail millet 500gr', 'name_hi': 'Foxtail millet 500gr', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/foxtail.jpg'} ,
    {'product_id': 133, 'name_en': 'Little millet 500gr', 'name_hi': 'Little millet 500gr', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/littlemillet.jpg'} ,
    {'product_id': 134, 'name_en': 'Kodo Millets 500 Gram', 'name_hi': 'कोदो मिलेट्स 500 ग्राम', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kodo.jpg'} ,
    {'product_id': 135, 'name_en': 'Sabut Sesame 500 Gram', 'name_hi': 'साबुत तिल 500 ग्राम', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/til.jpg'} ,
    {'product_id': 136, 'name_en': 'shuddh praakrtik Neem khalee 1 Kg', 'name_hi': 'शुद्ध प्राकृतिक नीम खली 1 किलो', 'price': 50, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/neem.jpg'} ,
    {'product_id': 137, 'name_en': 'Black Wheat  Daliya 500 Gram', 'name_hi': 'काला गेहूं का दलिया 500 ग्राम', 'price': 60, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/daliya.jpg'} ,
    {'product_id': 138, 'name_en': 'Organic Kathiya Daliya 500 Gram', 'name_hi': 'जैविक कठिया दलिया पांच सौ ग्राम', 'price': 50, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kathiyadaliya.jpg'} ,
    {'product_id': 139, 'name_en': 'Neem Oil 500ml', 'name_hi': 'नीम तेल 500ml', 'price': 175, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/neemoil.jpg'} ,
    {'product_id': 140, 'name_en': 'Moringa Powder 100 Gram', 'name_hi': 'मोरिंगा पाउडर 100 ग्राम', 'price': 80, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/moringa.jpg'} ,
    {'product_id': 141, 'name_en': 'Lemongrass tea cut 100 Gram', 'name_hi': 'लेमनग्रास टी कट 100 ग्राम', 'price': 30, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/lemongrass.jpg'} ,
    {'product_id': 142, 'name_en': 'Chia Seed 100 Gram', 'name_hi': 'चिया सीड 100 ग्राम', 'price': 80, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/chia.jpg'} ,
    {'product_id': 143, 'name_en': 'Ashwagandha Powder 100 Gram', 'name_hi': 'अश्वगंधा पाउडर 100 ग्राम', 'price': 80, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/ashwagandha.jpg'} ,
    {'product_id': 144, 'name_en': 'Sama Rice 500 Gram', 'name_hi': 'सामा चावल 500 ग्राम', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/sama.jpg'} ,
    {'product_id': 145, 'name_en': 'Sesame Oil 500ml', 'name_hi': 'तिल तेल 500ml', 'price': 200, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/tiloil.jpg'} ,
    {'product_id': 146, 'name_en': 'Flaxseed Oil 500ml', 'name_hi': 'अलसी तेल 500ml', 'price': 160, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/alsioil.jpg'} ,
    {'product_id': 147, 'name_en': 'Black Wheat Daliya 1 Kg', 'name_hi': 'काला गेहूं दलिया 1 किलो', 'price': 120, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/daliya1kg.jpg'} ,
    {'product_id': 148, 'name_en': 'Kathiya Daliya 1 Kg', 'name_hi': 'कठिया दलिया 1 किलो', 'price': 100, 'shop_id': 1, 'shop_name': 'Aashiyana', 'image': '/static/images/products/kathiyadaliya1kg.jpg'} ,
    {'product_id': 5, 'name_en': 'Masoor Dal', 'name_hi': 'मसूर दाल', 'price': 95, 'shop_id': 2, 'shop_name': 'FPO 2', 'image': '/static/images/products/masoor.jpg'} ,
    {'product_id': 6, 'name_en': 'Arhar Dal', 'name_hi': 'अरहर दाल', 'price': 115, 'shop_id': 2, 'shop_name': 'FPO 2', 'image': '/static/images/products/arhar.jpg'} ,
    {'product_id': 7, 'name_en': 'Moong Chhilka Dal', 'name_hi': 'मूंग छिलका दाल', 'price': 105, 'shop_id': 2, 'shop_name': 'FPO 2', 'image': '/static/images/products/moong.jpg'} ,
    {'product_id': 8, 'name_en': 'Urad Chhilka Dal', 'name_hi': 'उड़द छिलका दाल', 'price': 125, 'shop_id': 2, 'shop_name': 'FPO 2', 'image': '/static/images/products/urad.jpg'} ,
    {'product_id': 9, 'name_en': 'Masoor Dal', 'name_hi': 'मसूर दाल', 'price': 90, 'shop_id': 3, 'shop_name': 'Achyutam', 'image': '/static/images/products/masoor.jpg'} ,
    {'product_id': 10, 'name_en': 'Arhar Dal', 'name_hi': 'अरहर दाल', 'price': 110, 'shop_id': 3, 'shop_name': 'Achyutam', 'image': '/static/images/products/arhar.jpg'} ,
    {'product_id': 11, 'name_en': 'Moong Chhilka Dal', 'name_hi': 'मूंग छिलका दाल', 'price': 100, 'shop_id': 3, 'shop_name': 'Achyutam', 'image': '/static/images/products/moong.jpg'} ,
    {'product_id': 12, 'name_en': 'Urad Chhilka Dal', 'name_hi': 'उड़द छिलका दाल', 'price': 120, 'shop_id': 3, 'shop_name': 'Achyutam', 'image': '/static/images/products/urad.jpg'} ,
    {'product_id': 13, 'name_en': 'Masoor Dal', 'name_hi': 'मसूर दाल', 'price': 100, 'shop_id': 4, 'shop_name': 'Kisan Jaivik Utpadak Sangathan', 'image': '/static/images/products/masoor.jpg'} ,
    {'product_id': 14, 'name_en': 'Arhar Dal', 'name_hi': 'अरहर दाल', 'price': 120, 'shop_id': 4, 'shop_name': 'Kisan Jaivik Utpadak Sangathan', 'image': '/static/images/products/arhar.jpg'} ,
    {'product_id': 15, 'name_en': 'Moong Chhilka Dal', 'name_hi': 'मूंग छिलका दाल', 'price': 110, 'shop_id': 4, 'shop_name': 'Kisan Jaivik Utpadak Sangathan', 'image': '/static/images/products/moong.jpg'} ,
    {'product_id': 16, 'name_en': 'Urad Chhilka Dal', 'name_hi': 'उड़द छिलका दाल', 'price': 130, 'shop_id': 4, 'shop_name': 'Kisan Jaivik Utpadak Sangathan', 'image': '/static/images/products/urad.jpg'} ,
    {'product_id': 17, 'name_en': 'Masoor Dal', 'name_hi': 'मसूर दाल', 'price': 105, 'shop_id': 10, 'shop_name': 'Vedic Foods', 'image': '/static/images/products/masoor.jpg'} ,
    {'product_id': 18, 'name_en': 'Arhar Dal', 'name_hi': 'अरहर दाल', 'price': 125, 'shop_id': 10, 'shop_name': 'Vedic Foods', 'image': '/static/images/products/arhar.jpg'} ,
    {'product_id': 19, 'name_en': 'Moong Chhilka Dal', 'name_hi': 'मूंग छिलका दाल', 'price': 115, 'shop_id': 10, 'shop_name': 'Vedic Foods', 'image': '/static/images/products/moong.jpg'} ,
    {'product_id': 20, 'name_en': 'Urad Chhilka Dal', 'name_hi': 'उड़द छिलका दाल', 'price': 135, 'shop_id': 10, 'shop_name': 'Vedic Foods', 'image': '/static/images/products/urad.jpg'} 
]

# 🏠 HOME
@main_bp.route("/")
def home():

    featured_shops = shops_data[:4]

    return render_template(
        "index.html",
        shops=shops_data,
        featured_shops=featured_shops
    )

# 🏪 ALL SHOPS
@main_bp.route("/shops")
def shops():
    return render_template("shops.html", shops=shops_data)

# 🔍 SEARCH (multi-shop)
@main_bp.route("/search")
def search():

    query = request.args.get("q", "").lower().strip()

    results = []

    # 🔥 English ↔ Hindi keyword mapping
    keyword_map = {

        "dal":"दाल",
        "moong":"मूंग",
        "urad":"उड़द",
        "arhar":"अरहर",
        "masoor":"मसूर",
        "besan":"बेसन",

        "atta":"आटा",
        "wheat":"गेहूं",
        "multigrain":"मल्टीग्रेन",
        "bajra":"बाजरे",
        "jwar":"ज्वार",
        "makka":"मक्का",

        "oil":"तेल",
        "mustard":"सरसों",
        "sarso":"सरसों",
        "til":"तिल",
        "alsi":"अलसी",

        "millet":"मिलेट्स",
        "kodo":"कोदो",

        "rice":"चावल",
        "sattu":"सत्तू",
        "pickle":"अचार",
        "achar":"अचार",

        "chia":"चिया",
        "moringa":"मोरिंगा",
        "ashwagandha":"अश्वगंधा",
        "lemongrass":"लेमनग्रास",

        "neem":"नीम"
    }

    translated_query = keyword_map.get(query, query)

    for p in products_data:

        product_name = (
            p["name_en"].lower()
            + " " +
            p["name_hi"].lower()
        )

        if (
            query in product_name
            or translated_query in product_name
        ):

            results.append(p)

    return render_template(
        "product.html",
        products=results,
        query=query
    )
# 🛍 INDIVIDUAL SHOP PAGE
@main_bp.route("/shop/<int:shop_id>")
def shop_page(shop_id):

    shop_products = []

    for p in products_data:

        if p["shop_id"] == shop_id:
            shop_products.append(p)

    return render_template(
        "shop.html",
        products=shop_products
    )
# LIVE SEARCH SUGGESTIONS
@main_bp.route("/suggest")
def suggest():

    query = request.args.get("q", "").lower()

    suggestions = []

    for p in products_data:

        text = (
            p["name_en"].lower()
            + " " +
            p["name_hi"].lower()
        )

        if query in text:

            suggestions.append({
                "name": p["name_en"]
            })

    unique = []
    seen = set()

    for s in suggestions:

        if s["name"] not in seen:
            unique.append(s)
            seen.add(s["name"])

    return jsonify(unique[:8])