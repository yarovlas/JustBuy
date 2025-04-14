from flask import render_template, request, redirect, url_for, flash, session
from datetime import datetime
from models import db, Product, User, Cart, CartItem
from forms import LoginForm, SignupForm, AddProductForm
import logging

logger = logging.getLogger(__name__)

def register_routes(app):
    # Route for the index page
    @app.route("/")
    def index():
        logger.info("Rendering index page")
        return render_template("main.html")

    # Route for the home page
    @app.route("/home")
    def home():
        logger.info("Rendering home page")
        return render_template("main.html")

    # Route to display all products
    @app.route("/products")
    def products():
        logger.info("Fetching all products")
        products = Product.query.all()
        # Sanitize product data for display
        sanitized_products = [
            {
                "product_id": product.product_id,
                "product_name": product.product_name.strip(),
                "price": f"{product.price:.2f}",
            }
            for product in products
        ]
        return render_template("products.html", products=sanitized_products)

    # Route to display details of a specific product
    @app.route("/products/<int:product_id>")
    def product_detail(product_id):
        logger.info(f"Fetching details for product_id: {product_id}")
        product = Product.query.get_or_404(product_id)
        return render_template("product_detail.html", product=product)

    # Route for the contact page
    @app.route("/contact")
    def contact():
        logger.info("Rendering contact page")
        return render_template("contact.html")

    # Route for the about page
    @app.route("/about")
    def about():
        logger.info("Rendering about page")
        return render_template("about.html")

    # Route for user login
    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user:
                logger.debug(f"User found: {user.email}")
                logger.debug(f"User password hash: {user.password_hash}")
                # Check if the password is correct
                if user.check_password(password):
                    session["user_id"] = user.userid
                    session["user_name"] = user.first_name
                    flash("Login successful!", "success")
                    logger.info(f"User {email} logged in successfully")
                    return redirect(url_for("index"))
                else:
                    logger.warning(f"Password check failed for user: {email}")
            else:
                logger.warning(f"No user found with email: {email}")
            flash("Invalid email or password", "danger")
        return render_template("login.html", form=form)

    # Route for user signup
    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        form = SignupForm()
        if form.validate_on_submit():
            email = form.email.data
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already registered. Please use a different email or log in.", "danger")
                logger.warning(f"Attempt to register with existing email: {email}")
                return redirect(url_for("signup"))

            # Create a new user and save to the database
            first_name = form.first_name.data
            surname = form.surname.data
            password = form.password.data
            
            user = User(first_name=first_name, surname=surname, email=email)
            user.set_password(password)
            
            db.session.add(user)
            db.session.commit()
            
            flash("Registration successful! Please log in.", "success")
            logger.info(f"New user registered with email: {email}")
            return redirect(url_for("login"))
        return render_template("signup.html", form=form)

    # Route for user logout
    @app.route("/logout")
    def logout():
        session.clear()
        flash("You have been logged out.", "success")
        logger.info("User logged out successfully")
        return redirect(url_for("home"))

    # Route to add a new product
    @app.route("/add_product", methods=["GET", "POST"])
    def add_product():
        form = AddProductForm()
        if form.validate_on_submit():
            if "user_id" not in session:
                flash("You must be logged in to add a product.", "danger")
                return redirect(url_for("login"))
            # Get product details from the form
            user_id = session["user_id"]
            product_name = form.product_name.data
            product_description = form.product_description.data
            price = form.price.data
            date_added = datetime.today()
            
            # Create a new product and save to the database
            product = Product(seller_id=user_id, product_name=product_name, product_description=product_description, price=price, date_added=date_added, status="Available")
            
            db.session.add(product)
            db.session.commit()
            
            flash("Product added successfully!", "success")
            logger.info(f"New product added: {product_name}")
            return redirect(url_for("products"))
        return render_template("add_product.html", form=form)

    # Route to view the user's cart
    @app.route("/cart", methods=["GET"])
    def view_cart():
        if "user_id" not in session:
            flash("You must be logged in to view your cart.", "danger")
            return redirect(url_for("login"))
        user_id = session["user_id"]
        cart = Cart.query.filter_by(user_id=user_id).first()
        # Fetch all items in the user's cart
        cart_items = cart.cart_items if cart else []
        return render_template("cart.html", cart_items=cart_items)

    # Route to add a product to the cart
    @app.route("/cart/add/<int:product_id>", methods=["POST"], endpoint="cart/add")
    def add_to_cart(product_id):
        if "user_id" not in session:
            flash("You must be logged in to add items to your cart.", "danger")
            return redirect(url_for("login"))
        product = Product.query.get(product_id)
        if not product or product.status.lower() != 'available':
            flash("Product is not available.", "danger")
            return redirect(url_for("products"))
        user_id = session["user_id"]
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            # Create a new cart if the user doesn't have one
            cart = Cart(user_id=user_id)
            db.session.add(cart)
            db.session.commit()
        # Check if the product is already in the cart
        cart_item = CartItem.query.filter_by(cart_id=cart.cart_id, product_id=product_id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = CartItem(cart_id=cart.cart_id, product_id=product_id, quantity=1)
            db.session.add(cart_item)
        db.session.commit()
        flash("Product added to cart!", "success")
        return redirect(url_for("products"))

    # Route to remove an item from the cart
    @app.route("/cart/remove/<int:cart_item_id>", methods=["POST"])
    def remove_from_cart(cart_item_id):
        cart_item = CartItem.query.get_or_404(cart_item_id)
        db.session.delete(cart_item)
        db.session.commit()
        flash("Item removed from cart.", "success")
        return redirect(url_for("view_cart"))

    # Route to view and update the user's profile
    @app.route("/profile_page", methods=["GET", "POST"])
    def profile_page():
        if "user_id" not in session:
            flash("You must be logged in to view your profile.", "danger")
            return redirect(url_for("login"))

        user_id = session["user_id"]
        user = User.query.get_or_404(user_id)

        if request.method == "POST":
            # Update user details if provided
            first_name = request.form.get("first_name")
            surname = request.form.get("surname")
            email = request.form.get("email")

            if first_name:
                user.first_name = first_name
            if surname:
                user.surname = surname
            if email:
                existing_user = User.query.filter_by(email=email).first()
                if existing_user and existing_user.userid != user_id:
                    flash("Email already in use by another account.", "danger")
                    return redirect(url_for("profile_page"))
                user.email = email

            db.session.commit()
            flash("Profile updated successfully!", "success")
            return redirect(url_for("profile_page"))

        return render_template("profile_page.html", user=user)

    # Error handler for 404 errors
    @app.errorhandler(404)
    def page_not_found(e):
        logger.error(f"Page not found: {request.url}")
        return render_template("404.html"), 404

    # Error handler for 500 errors
    @app.errorhandler(500)
    def internal_server_error(e):
        logger.error(f"Internal server error: {request.url}")
        return render_template("500.html"), 500