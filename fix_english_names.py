from routes.main_routes import products_data
replacements = {
    "मक्का":"Makka",
    "ज्वार":"Jowar",
    "पीली":"Yellow",
    "सरसों":"Mustard",
    "तेल":"Oil",
    "गेहूं":"Wheat",
    "मल्टीग्रेन":"Multigrain",
    "कठिया":"Kathiya",
    "मूंग":"Moong",
    "बेसन":"Besan",
    "जौ":"Barley",
    "उड़द":"Urad",
    "काला":"Black",
    "पंचरंगी":"Mix",
    "सत्तू":"Sattu",
    "भरवा":"Stuffed",
    "लाल":"Red",
    "मिर्च":"Chilli",
    "अचार":"Pickle",
    "अरहर":"Arhar",
    "कोदो":"Kodo",
    "मिलेट्स":"Millets",
    "तिल":"Sesame",
    "नीम":"Neem",
    "दलिया":"Daliya",
    "मोरिंगा":"Moringa",
    "लेमनग्रास":"Lemongrass",
    "चिया":"Chia",
    "अश्वगंधा":"Ashwagandha",
    "सामा":"Sama",
    "अलसी":"Flaxseed",
    "चावल":"Rice",
    "ग्राम":"Gram",
    "किलो":"Kg",
    "का":"",
    "पांच सौ":"500",
    "सामान्य":"Regular",
    "शुद्ध प्राकृतिक":"Pure Natural"
}

fixed_products = []

for p in products_data:

    english_name = p["name_hi"]

    for hi, en in replacements.items():
        english_name = english_name.replace(hi, en)

    english_name = " ".join(english_name.split())

    updated = {
        "product_id": p["product_id"],
        "name_en": english_name,
        "name_hi": p["name_hi"],
        "price": p["price"],
        "shop_id": p["shop_id"],
        "shop_name": p["shop_name"],
        "image": p["image"]
    }

    fixed_products.append(updated)

print("products_data = [")

for item in fixed_products:
    print(item, ",")

print("]")