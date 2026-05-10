from flask import Blueprint, render_template, request, redirect, session
from database.db import mysql
import os

admin_bp = Blueprint("admin", __name__)

# =========================
# LOGIN
# =========================

@admin_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
            """
            SELECT
            id,
            username,
            email,
            phone,
            password,
            shop_id

            FROM users

            WHERE username=%s
            AND password=%s
            """,

            (username, password)
        )

        user = cur.fetchone()

        cur.close()

        if user:

            session["user_id"] = user[0]

            session["shop_id"] = user[5]

            return redirect("/dashboard")

    return render_template("login.html")


# =========================
# SIGNUP
# =========================

@admin_bp.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        phone = request.form["phone"]

        password = request.form["password"]

        shop_name = request.form["shop_name"]

        cur = mysql.connection.cursor()

        # CREATE SHOP

        cur.execute(
            """
            INSERT INTO shops(name,image)
            VALUES(%s,%s)
            """,
            (
                shop_name,
                "/static/images/default-shop.png"
            )
        )

        mysql.connection.commit()

        shop_id = cur.lastrowid

        # CREATE USER

        cur.execute(
            """
            INSERT INTO users
            (username,email,phone,password,shop_id)

            VALUES(%s,%s,%s,%s,%s)
            """,
            (
                username,
                email,
                phone,
                password,
                shop_id
            )
        )

        mysql.connection.commit()

        cur.close()

        return redirect("/login")

    return render_template("signup.html")


# =========================
# DASHBOARD
# =========================

@admin_bp.route("/dashboard")
def dashboard():

    if "shop_id" not in session:
        return redirect("/login")

    shop_id = session["shop_id"]

    cur = mysql.connection.cursor()

    cur.execute(
        """
        SELECT * FROM products
        WHERE shop_id=%s
        """,
        (shop_id,)
    )

    products = cur.fetchall()

    cur.close()

    return render_template(
        "dashboard.html",
        products=products
    )


# =========================
# ADD PRODUCT
# =========================

@admin_bp.route("/add-product", methods=["POST"])
def add_product():

    if "shop_id" not in session:
        return redirect("/login")

    name_en = request.form["name_en"]

    name_hi = request.form["name_hi"]

    price = request.form["price"]

    image = request.files["image"]

    # UNIQUE IMAGE NAME

    filename = (
        str(session["shop_id"])
        + "_"
        + image.filename
    )

    image_path = (
        "static/images/products/"
        + filename
    )

    image.save(image_path)

    db_image_path = "/" + image_path

    shop_id = session["shop_id"]

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO products
        (shop_id,name_en,name_hi,price,image)

        VALUES(%s,%s,%s,%s,%s)
        """,

        (
            shop_id,
            name_en,
            name_hi,
            price,
            db_image_path
        )
    )

    mysql.connection.commit()

    cur.close()

    return redirect("/dashboard")


# =========================
# DELETE PRODUCT
# =========================

@admin_bp.route("/delete-product/<int:id>")
def delete_product(id):

    if "shop_id" not in session:
        return redirect("/login")

    shop_id = session["shop_id"]

    cur = mysql.connection.cursor()

    cur.execute(
        """
        DELETE FROM products

        WHERE id=%s
        AND shop_id=%s
        """,

        (
            id,
            shop_id
        )
    )

    mysql.connection.commit()

    cur.close()

    return redirect("/dashboard")


# =========================
# EDIT PRODUCT
# =========================

@admin_bp.route("/edit-product/<int:id>", methods=["GET","POST"])
def edit_product(id):

    if "shop_id" not in session:
        return redirect("/login")

    shop_id = session["shop_id"]

    cur = mysql.connection.cursor()

    # GET PRODUCT

    cur.execute(
        """
        SELECT * FROM products

        WHERE id=%s
        AND shop_id=%s
        """,

        (
            id,
            shop_id
        )
    )

    product = cur.fetchone()

    # PRODUCT NOT FOUND

    if not product:

        cur.close()

        return redirect("/dashboard")

    # UPDATE PRODUCT

    if request.method == "POST":

        name_en = request.form["name_en"]

        name_hi = request.form["name_hi"]

        price = request.form["price"]

        image = request.files["image"]

        # UNIQUE IMAGE NAME

        filename = (
            str(session["shop_id"])
            + "_"
            + image.filename
        )

        image_path = (
            "static/images/products/"
            + filename
        )

        image.save(image_path)

        db_image_path = "/" + image_path

        cur.execute(
            """
            UPDATE products

            SET
            name_en=%s,
            name_hi=%s,
            price=%s,
            image=%s

            WHERE id=%s
            AND shop_id=%s
            """,

            (
                name_en,
                name_hi,
                price,
                db_image_path,
                id,
                shop_id
            )
        )

        mysql.connection.commit()

        cur.close()

        return redirect("/dashboard")

    cur.close()

    return render_template(
        "edit_product.html",
        product=product
    )


# =========================
# CHANGE PASSWORD
# =========================

@admin_bp.route("/change-password", methods=["GET","POST"])
def change_password():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        old_password = request.form["old_password"]

        new_password = request.form["new_password"]

        user_id = session["user_id"]

        cur = mysql.connection.cursor()

        # CHECK OLD PASSWORD

        cur.execute(
            """
            SELECT * FROM users

            WHERE id=%s
            AND password=%s
            """,

            (
                user_id,
                old_password
            )
        )

        user = cur.fetchone()

        # UPDATE PASSWORD

        if user:

            cur.execute(
                """
                UPDATE users

                SET password=%s

                WHERE id=%s
                """,

                (
                    new_password,
                    user_id
                )
            )

            mysql.connection.commit()

            cur.close()

            return redirect("/dashboard")

        cur.close()

    return render_template("change_password.html")


# =========================
# LOGOUT
# =========================

@admin_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/")