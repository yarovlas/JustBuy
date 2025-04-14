DROP DATABASE IF EXISTS p1dorsgang;
CREATE DATABASE p1dorsgang;
USE p1dorsgang;

CREATE TABLE users (
    userid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    seller_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    date_added DATE NOT NULL,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (seller_id) REFERENCES users(userid)
);

CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    buyer_id INT NOT NULL,
    order_status VARCHAR(255) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (buyer_id) REFERENCES users(userid)
);

CREATE TABLE order_items (
    order_item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE carts (
    cart_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(userid)
);

CREATE TABLE cart_items (
    cart_item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
