# Project Summary: Mini E-Commerce System

**PS No.:** 39

**Language:** Python 3

**Concepts:** Products, Cart, CRUD, File Handling

**Code file:** `one.py`

**Data file:** `products.txt`

---

## 1. Project Overview

This project is a console-based shopping application. An admin can add, view, update and delete products, and a customer can add products to a cart and check out. Product data is stored in `products.txt`, so the data is kept after the program is closed.

## 2. What I Have Done

- Stored the products in a **list of dictionaries** (`id`, `name`, `price`, `stock`) and the cart in a **dictionary** (`product ID: quantity`).
- Wrote a separate function for each task: `add_product`, `view_products`, `update_product`, `delete_product`, `add_to_cart`, `view_cart` and `checkout`.
- Added `load_products()` to read the file when the program starts and `save_products()` to write the file after every change.
- Made product IDs automatic. The first ID is `P101`, and each new product gets the highest existing number plus one.
- Reduced the stock at checkout and blocked orders that are more than the stock available.
- Added checks for wrong input: negative or non-numeric prices, negative stock, zero or negative quantity, and product IDs that do not exist.
- Added a warning message when a product is added with zero stock.
- Created a main menu with 8 options that runs in a loop until the user chooses Exit.
- Tested the program with all 4 given test cases and checked `products.txt` after each change.

## 3. Test Cases and Screenshots

### Test Case 1: Normal Input

**Input:** Add product Laptop, price 50000, stock 5

**Expected output:** `Product added.` and `ID: P101 | Laptop | Price: 50000 | Stock: 5`

The screenshot below shows `products.txt` after the Laptop was added. The file holds `P101|Laptop|50000|5`, so the product was created with ID P101 and saved correctly.
<img width="1487" height="711" alt="Screenshot 2026-11-11 180956" src="https://github.com/user-attachments/assets/c80011a5-7a95-4e08-b657-2e2758bf19e6" /><br>
<img width="1460" height="278" alt="Screenshot 2026-11-11 181443" src="https://github.com/user-attachments/assets/08b7d144-b05f-4899-9e02-6a75dca1584d" />






Output as text:

```text
P101|Laptop|50000|5
P102|Pen|1|0
```

### Test Case 2: Boundary / Minimum Input

**Input:** Add product Pen, price 1 (minimum), stock 0

**Expected output:** Product added, followed by `Warning: Pen is out of stock.`

The program accepted the minimum price of 1 and the stock of 0, and showed the out-of-stock warning. The ID is `P102` here because the Laptop from Test Case 1 was already in the file. On an empty product list it gets `P101`.


<img width="1492" height="711" alt="Screenshot 2026-11-11 181059" src="https://github.com/user-attachments/assets/0de4146d-8b12-44ef-babb-1f55b350c73c" />





Output as text:

```text
Enter your choice: 1
Enter product name: Pen
Enter price: 1
Enter stock: 0
Product added.
ID: P102 | Pen | Price: 1 | Stock: 0
Warning: Pen is out of stock.
```

### Test Case 3: Invalid Input

**Input:** (a) Add product Mouse with price -500, and (b) add to cart P999

**Expected output:** (a) `Invalid price. Price must be a positive number.` and (b) `Product P999 not found.`

Both invalid inputs were rejected with the correct messages, and the program returned to the menu without crashing.

<img width="1481" height="955" alt="WhatsApp Image 2026-11-11 at 6 42 32 PM" src="https://github.com/user-attachments/assets/b9f8749c-7494-4249-9cd3-ea4ee7941b8a" />





Output as text:

```text
Enter your choice: 1
Enter product name: Mouse
Enter price: -500
Enter stock: 1
Invalid price. Price must be a positive number.

Enter your choice: 5
Enter product ID: P999
Product P999 not found.
```

### Test Case 4: Different Valid Scenario

**Input:** (a) Add to cart P101, quantity 2, (b) checkout, and (c) delete product P101

**Expected output:**
- (a) `Laptop x 2 added | Amount: 100000`
- (b) `Order Total: 100000` and `Laptop stock left: 3`
- (c) `Product 'Laptop' deleted.`

**(a) and (b): Add to cart and checkout.** The amount was 2 x 50000 = 100000, and the stock dropped from 5 to 3 after checkout.
<img width="1442" height="946" alt="Screenshot 2026-11-11 181612" src="https://github.com/user-attachments/assets/fb874a9d-2874-4d74-8f80-25c33bb659bf" />






Output as text:

```text
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

**(c) Delete product.** The Laptop was deleted and the message was shown. It says `Products left: 1` instead of `0` only because the Pen from Test Case 2 was still in the file. With an empty starting list, as the test case says, the count is 0.

<img width="1437" height="931" alt="Screenshot 2026-11-11 181632" src="https://github.com/user-attachments/assets/9d557c70-73af-4b95-89dc-6e44268168c7" />





Output as text:

```text
Enter your choice: 4
Enter product ID: P101
Product 'Laptop' deleted.
Products left: 1
```

### File Handling Check

After the delete, `products.txt` holds only `P102|Pen|1|0`. This shows that the file is updated after every change.

<img width="1510" height="285" alt="Screenshot 2026-11-11 181646" src="https://github.com/user-attachments/assets/bf4328c4-d664-464f-82cd-6001128a7932" />





Output as text:

```text
P102|Pen|1|0
```

## 4. Hardships Faced and How I Overcame Them

| Hardship | How I Overcame It |
|---|---|
| **Saving and loading products from a file.** The data had to be stored as plain text and turned back into dictionaries each time the program started. | I used the `\|` symbol to separate the fields (`ID\|name\|price\|stock`), and split each line when loading. I also check that a line has exactly 4 parts, so a bad line does not crash the program. |
| **Creating product IDs.** Using the number of products as the next ID gave a repeated ID after a product was deleted. | I take the highest existing ID number and add 1. The IDs start at 101, so the first product is always P101 and IDs are never repeated. |
| **Wrong user input.** Typing letters instead of numbers, or a negative price, caused errors. | I check every price, stock and quantity before using it, and print a clear message such as `Invalid price. Price must be a positive number.` The program then returns to the menu. |
| **Ordering more than the stock.** A customer could add the same product to the cart several times and pass the stock limit. | In `add_to_cart` I check the new quantity together with what is already in the cart. At checkout I check the stock again before reducing it. |
| **Keeping the file and the program in sync.** If the file was not saved after a change, the old data came back on the next run. | I call `save_products()` after every add, update, delete and checkout, and once more on exit. I checked `products.txt` after each test to confirm it. |
| **Testing with the right data.** The test cases say to start with an empty list, but my file already had products from the earlier tests, so IDs and counts looked different (for example P102 and `Products left: 1`). | I understood that this came from the saved file and not from a bug. For a clean test I delete `products.txt` before running a test case. |
| **Understanding which messages to print.** The output had to match the format in the test cases. | I compared each message with the expected output word by word and fixed the spacing and wording until they matched. |

## 5. What I Learned

- How to read from and write to a text file in Python.
- How to use lists and dictionaries together to store and search data.
- How to split a program into small functions so it is easier to read, test and fix.
- Why input checking matters, and how to give clear error messages.
- How to test a program against given test cases and find the cause of a difference in output.

## 6. How to Run

```bash
python one.py
```

Delete `products.txt` before each test case so that it starts with an empty product list.

## 7. Files in This Project

```
Python-Projects/
├── one.py               # main program
├── products.txt         # product data (created automatically)
├── README.md            # project description
└── Summary.md           # this summary
```
