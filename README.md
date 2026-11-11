# Mini E-Commerce System

A console-based shopping application written in Python 3. An admin can add, view, update and delete products, and a customer can add products to a cart and check out. All product data is stored in a text file, so it is kept between runs.

**PS No.:** 39
**University:** Rungta International Skills University
**School:** School of Computer Science and Engineering
**Course:** Bachelor of Technology, Computer Science and Engineering
**Language:** Python 3
**Concepts:** Products, Cart, CRUD, File Handling

---

## Problem Statement

Create a console shopping application where an admin adds, updates and deletes products, and a customer adds products to a cart and checks out. Product data is stored in a file. The first product ID is P101. Checkout reduces the stock, and a customer cannot order more than the stock available.

## Features

- Add a new product with a name, price and stock (IDs are created automatically, starting at P101)
- View all available products
- Update the name, price or stock of a product
- Delete a product
- Add a product to the cart with a quantity
- View the cart with the amount for each item and the total
- Check out, which prints the order total and reduces the stock
- Warning message when a product has zero stock
- Products are loaded from `products.txt` when the program starts and saved after every change

## How the Program Works

1. When the program starts, `load_products()` reads `products.txt` (if it exists) into a list of dictionaries.
2. A menu with 8 options is shown in a loop until the user chooses Exit.
3. Every action that changes the data (add, update, delete, checkout) saves the products back to the file.
4. When the user exits, the products are saved one last time.

## Data Structures

**Products** are stored in a list of dictionaries:

```python
products = [
    {"id": "P101", "name": "Laptop", "price": 50000, "stock": 5},
    {"id": "P102", "name": "Pen", "price": 1, "stock": 0}
]
```

**Cart** is stored in a dictionary where the key is the product ID and the value is the quantity:

```python
cart = {"P101": 2}
```

## File Format

Products are stored in `products.txt`, one product per line, with the fields separated by the `|` symbol:

```
ID|name|price|stock
P101|Laptop|50000|5
P102|Pen|1|0
```

## Functions

| Function | What it does |
|---|---|
| `load_products()` | Reads the products from `products.txt` into the `products` list |
| `save_products()` | Writes all products from the list back to `products.txt` |
| `add_product()` | Asks for name, price and stock, checks them, creates the next ID, and saves the product |
| `view_products()` | Prints every product with its ID, name, price and stock |
| `update_product()` | Finds a product by ID and updates its name, price or stock |
| `delete_product()` | Finds a product by ID, removes it, and shows how many products are left |
| `add_to_cart()` | Adds a quantity of a product to the cart if enough stock is available |
| `view_cart()` | Shows each cart item with its amount and the total amount |
| `checkout()` | Checks the stock, prints the order total, reduces the stock, empties the cart and saves |

## Rules and Validation

- The price must be a positive whole number.
- The stock cannot be negative.
- The quantity must be a positive whole number.
- A product with zero stock cannot be added to the cart.
- The quantity ordered (including what is already in the cart) cannot be more than the stock available.
- Product IDs must be typed exactly as shown, for example `P101`.
- A product that does not exist shows a "not found" message.
- A new product ID is created by taking the highest existing number and adding 1, so IDs are never repeated.

## Requirements

- Python 3.x
- No external libraries are needed (only the built-in `os` module is used)

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python mini_ecommerce.py
```

4. Choose an option from the menu by typing its number.

If `products.txt` does not exist, the program starts with an empty product list and creates the file when the first product is added.

## Menu

```
===== MINI E-COMMERCE SYSTEM =====
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Add to Cart
6. View Cart
7. Checkout
8. Exit
```

## Test Cases

Each test case starts with an empty product list.

| Test Case | Input | Expected Output |
|---|---|---|
| 1. Normal input | Add product: Laptop, price 50000, stock 5 | `Product added.` and `ID: P101 \| Laptop \| Price: 50000 \| Stock: 5` |
| 2. Boundary input | Add product: Pen, price 1, stock 0 | Product added with ID P101, then `Warning: Pen is out of stock.` |
| 3a. Invalid input | Add product: Mouse, price -500 | `Invalid price. Price must be a positive number.` |
| 3b. Invalid input | Add to cart: P999 | `Product P999 not found.` |
| 4a. Valid scenario | Add to cart: P101, quantity 2 | `Laptop x 2 added \| Amount: 100000` |
| 4b. Valid scenario | Checkout | `Order Total: 100000` and `Laptop stock left: 3` |
| 4c. Valid scenario | Delete product P101 | `Product 'Laptop' deleted.` and `Products left: 0` |

## Sample Run

```
Enter your choice: 1
Enter product name: Laptop
Enter price: 50000
Enter stock: 5
Product added.
ID: P101 | Laptop | Price: 50000 | Stock: 5

Enter your choice: 5
Enter product ID: P101
Enter quantity: 2
Laptop x 2 added | Amount: 100000

Enter your choice: 7

===== BILL =====
Order Total: 100000
Laptop stock left: 3
Checkout successful!
```

## Project Structure

```
Mini-E-Commerce-System/
├── mini_ecommerce.py    # main program
├── products.txt         # product data (created automatically)
└── README.md            # project description
```

## Author

- Name: Paritosh
- ERP: RU-26-01337 
- Section: 1M
