from flask import Flask

# 🔹 Import all routes
from routes.main_routes import main_bp
from routes.shop_routes import shop_bp
from routes.cart_routes import cart_bp
from routes.payment_routes import payment_bp

# 🔹 Create app
app = Flask(__name__)
app.secret_key = "secret123"   # session ke liye zaroori

# 🔹 Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(shop_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(payment_bp)

# 🔹 Run app
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))