import os

products = []
cart = {}

# Load products from file
def load_products():
    global products

    if os.path.exists("products.txt"):
        file = open("products.txt", "r")
        products = []

        for line in file:
            data = line.strip().split("|")

            if len(data) == 4:
                product = {
                    "id": data[0],
                    "name": data[1],
                    "price": int(float(data[2])),
                    "stock": int(data[3])
                }
                products.append(product)

        file.close()


# Save products to file
def save_products():
    file = open("products.txt", "w")

    for p in products:
        file.write(
            p["id"] + "|" + p["name"] + "|" +
            str(p["price"]) + "|" + str(p["stock"]) + "\n"
        )

    file.close()


# Add product
def add_product():
    name = input("Enter product name: ")

    try:
        price = int(input("Enter price: "))
        stock = int(input("Enter stock: "))
    except ValueError:
        print("Invalid input!")
        return

    if price <= 0:
        print("Invalid price. Price must be a positive number.")
        return

    if stock < 0:
        print("Invalid stock!")
        return

    number = 101

    for p in products:
        product_number = int(p["id"][1:])
        if product_number >= number:
            number = product_number + 1

    pid = "P" + str(number)

    product = {
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)
    save_products()

    print("Product added.")
    print("ID:", pid, "|", name, "| Price:", price, "| Stock:", stock)

    if stock == 0:
        print("Warning:", name, "is out of stock.")


# View products
def view_products():
    if len(products) == 0:
        print("No products available.")
        return

    print("\nAvailable Products:")

    for p in products:
        print(p["id"], "|", p["name"],
              "| Price:", p["price"],
              "| Stock:", p["stock"])


# Update product
def update_product():
    pid = input("Enter product ID: ")

    for p in products:
        if p["id"] == pid:
            print("1. Update name")
            print("2. Update price")
            print("3. Update stock")

            choice = input("Enter choice: ")

            if choice == "1":
                p["name"] = input("Enter new name: ")

            elif choice == "2":
                try:
                    price = int(input("Enter new price: "))
                    if price <= 0:
                        print("Invalid price!")
                        return
                    p["price"] = price
                except ValueError:
                    print("Invalid price!")
                    return

            elif choice == "3":
                try:
                    stock = int(input("Enter new stock: "))
                    if stock < 0:
                        print("Invalid stock!")
                        return
                    p["stock"] = stock
                except ValueError:
                    print("Invalid stock!")
                    return

            else:
                print("Invalid choice!")
                return

            save_products()
            print("Product updated.")
            return

    print("Product not found.")


# Delete product
def delete_product():
    pid = input("Enter product ID: ")

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            save_products()
            print("Product '" + p["name"] + "' deleted.")
            print("Products left:", len(products))
            return

    print("Product not found.")


# Add product to cart
def add_to_cart():
    pid = input("Enter product ID: ")

    for p in products:
        if p["id"] == pid:

            if p["stock"] == 0:
                print("Product is out of stock.")
                return

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity!")
                return

            if quantity <= 0:
                print("Invalid quantity!")
                return

            if quantity > p["stock"]:
                print("Not enough stock available.")
                return

            if pid in cart:
                if cart[pid] + quantity > p["stock"]:
                    print("Not enough stock available.")
                    return
                cart[pid] += quantity
            else:
                cart[pid] = quantity

            amount = p["price"] * quantity

            print(p["name"], "x", quantity,
                  "added | Amount:", amount)
            return

    print("Product", pid, "not found.")


# View cart
def view_cart():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = 0

    print("\nYour Cart:")

    for pid in cart:
        for p in products:
            if p["id"] == pid:
                quantity = cart[pid]
                amount = p["price"] * quantity

                print(p["name"], "x", quantity,
                      "| Amount:", amount)

                total += amount

    print("Total Amount:", total)


# Checkout
def checkout():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = 0

    for pid in cart:
        for p in products:
            if p["id"] == pid:
                if cart[pid] > p["stock"]:
                    print("Not enough stock for", p["name"])
                    return

                total += p["price"] * cart[pid]

    print("\n===== BILL =====")
    print("Order Total:", total)

    for pid in cart:
        for p in products:
            if p["id"] == pid:
                p["stock"] -= cart[pid]
                print(p["name"], "stock left:", p["stock"])

    cart.clear()
    save_products()

    print("Checkout successful!")


# Main menu
load_products()

while True:
    print("\n===== MINI E-COMMERCE SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Checkout")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        add_to_cart()

    elif choice == "6":
        view_cart()

    elif choice == "7":
        checkout()

    elif choice == "8":
        save_products()
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")