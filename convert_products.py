from routes.main_routes import products_data
translation_map = {
    "जैविक":"Organic",
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
    "किलो":"Kg"
}

new_products = []

for p in products_data:

    hindi_name = p["name"]

    english_name = hindi_name

    for hi, en in translation_map.items():
        english_name = english_name.replace(hi, en)

    new_product = {
        "product_id": p["product_id"],

        "name_en": english_name,

        "name_hi": hindi_name,

        "price": p["price"],

        "shop_id": p["shop_id"],

        "shop_name": p["shop_name"],

        "image": p["image"]
    }

    new_products.append(new_product)

print("products_data = [")

for item in new_products:
    print(item, ",")

print("]")