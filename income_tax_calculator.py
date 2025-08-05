

import sqlite3
import datetime 

class Store:
    def __init__(self, inventory_database):
        self.conn = sqlite3.connect(inventory_database)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS product_table("
                         "product_id INTEGER, "
                         "product_name TEXT, "
                         "product_price REAL, "
                         "product_quantity INTEGER"
                         ")"
                         )
        
        self.cur.execute("CREATE TABLE IF NOT EXISTS sales_table("
                         "sale_id INTEGER, "
                         "sale_date TEXT, "
                         "product_name TEXT, "
                         "sale_quantity INTEGER, "
                         "sale_total REAL"
                         ")"
                         )
        
        self.conn.commit()
        
    def addProduct(self, name, price, quantity): #Adds a new product to the product table
        self.cur.execute("INSERT new product to product_table (product_name, product_price, product_quantity VALUES(?, ?, ?)", (name, price, quantity))
        self.conn.commit()
        
    def removeProduct(self, product_id): #Removes a product from the product table according on its product ID
        self.cur.execute("DELETE FROM product_table WHERE product_id=?", (product_id,))
        self.conn.commit()
        
    def updateProduct(self, product_id, name, price, quantity):
        self.cur.execute("UPDATE product_table SET product_name=?, product_price=?, product_quantity=? WHERE product_id=?", (name, price, quantity, product_id))
        self.conn.commit()
        
    def displayProduct(self):
        self.cur.execute("SELECT * FROM product_table")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
            
    def sellProduct(self, product_id, sale_date, sale_quantity):
        try:
            self.cur.execute("SELECT product_quantity, product_price FROM product_table WHERE product_id=?", (product_id,)) #This block of code checks if the product is available
            row = self.cur.fetchone()
            if row: 
                quantity_available, price = row
                if quantity_available >= sale_quantity:
                    updated_quantity = quantity_available - sale_quantity
                    self.cur.execute("UPDATE product_table SET product_quantity=? WHERE product_id=?", (updated_quantity, product_id))
                    sale_total = sale_quantity * price
                    self.cur.execute("INSERT INTO sales_table (sale_date, product_name, sale_total, sale_quantity) VALUES (?, (SELECT product_name FROM product_table WHERE product_id=?), ?, ?)",(sale_date, product_id, sale_quantity, sale_total))
                    self.conn.commit()
                else:
                    print("Not enough quantity is available to make a sale !")
            else:
                print("Error: Product is not found!")
                
        except Exception as e:
            print("An error occured while selling product:", e)
                          
    def __del__(self):
        self.conn.close()  #Closes the database
        
    
def main():
    try:
        store = Store("store_inventory.db")
            
        while True:
            print("\nMenu:")
            print("1. Add new product")
            print("2. Update details of product")
            print("3. Display all products")
            print("4. Sell product")
            print("5. Remove product")
            print("6. Exit")
                
            option = input("Select and enter your option: ")
                  
            if option == "1":
                    name = input("Enter the product name: ")
                    price = float(input("Enter the product price: "))
                    quantity = int(input("Enter the product quantity: "))
                    store.addProduct(name, price, quantity)
            elif option == "2":
                    product_id = int(input("Enter the product ID to update: "))
                    name = input("Enter the new product name: ")
                    price = float(input("Enter the new price for the product"))
                    quantity = int(input("Enter the new product quantity: "))
                    store.updateProduct(product_id, name, price, quantity)
            elif option == "3":
                    print("Product List:")
                    store.displayProducts()
            elif option == "4":
                    product_id = int(input("Enter the product you want to sell: "))
                    sale_date = datetime.now().strftime("%Y-%m-%d")
                    sale_quantity = int(input("Enter the quantity you want to sell: "))
                    store.sellProduct(product_id, sale_date, sale_quantity)
            elif option == "5":
                    product_id = int(input("Enter the product_id to remove: "))
                    store.removeProduct(product_id)
            elif option == "6":
                    print("Exiting")
                    break
            else:
                    print("Invalid option, please try again.")
                    
    except Exception as e:
            print("An error occured: ", e)
                    
if __name__ == "__main__":
    main()
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    