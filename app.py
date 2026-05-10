from flask import Flask
from flask_mysqldb import MySQL
import os

# =========================
# IMPORT ROUTES
# =========================

from routes.main_routes import main_bp
from routes.shop_routes import shop_bp
from routes.cart_routes import cart_bp
from routes.payment_routes import payment_bp
from routes.admin_routes import admin_bp

# =========================
# CREATE APP
# =========================

app = Flask(__name__)

app.secret_key = "secret123"

# =========================
# MYSQL CONFIG
# =========================

app.config['MYSQL_HOST'] = os.environ.get("MYSQLHOST")

app.config['MYSQL_USER'] = os.environ.get("MYSQLUSER")

app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQLPASSWORD")

app.config['MYSQL_DB'] = os.environ.get("MYSQLDATABASE")

app.config['MYSQL_PORT'] = int(
    os.environ.get("MYSQLPORT", 3306)
)

# =========================
# MYSQL INIT
# =========================

mysql = MySQL(app)

# =========================
# REGISTER BLUEPRINTS
# =========================

app.register_blueprint(main_bp)

app.register_blueprint(shop_bp)

app.register_blueprint(cart_bp)

app.register_blueprint(payment_bp)

app.register_blueprint(admin_bp)

# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )