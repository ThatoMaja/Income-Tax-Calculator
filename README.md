#  Store Inventory Management System (Python + SQLite)

A simple terminal-based Python application to manage inventory and sales for a high-end store. Built using SQLite for lightweight data storage, this system allows users to manage product stock, process sales, and track updates in a structured way.

##  Features

-  Add new products to inventory
-  Update product details (name, price, quantity)
-  Remove products by ID
-  Display all available products
-  Sell products (with validation & auto-update of inventory)
-  Log each sale into a sales table with totals and dates

##  How It Works

Two tables are used:
- `product_table` – stores product ID, name, price, and quantity
- `sales_table` – logs sales with date, product, quantity sold, and total

All operations are performed using SQL queries via Python's `sqlite3` module.

##  How to Run

1. **Make sure you have Python 3 installed**
2. Clone/download the project
3. Run the script:

```bash
python store.py
