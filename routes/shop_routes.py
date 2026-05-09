from flask import Blueprint, render_template
from routes.main_routes import products_data

shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/shop/<int:id>")
def shop(id):
    # 🔥 Sirf us shop ke products
    products = [p for p in products_data if p["shop_id"] == id]
    return render_template("shop.html", products=products)