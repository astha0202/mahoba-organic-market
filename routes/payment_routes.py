from flask import Blueprint, render_template, session

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment")
def payment():
    cart = session.get("cart", [])
    total = sum(item["price"] * item["qty"] for item in cart)
    return render_template("payment.html", total=total)

@payment_bp.route("/place_order")
def place_order():
    session.pop("cart", None)
    return "<h2>✅ Order Placed Successfully!</h2>"