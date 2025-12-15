import tkinter as tk
from tkinter import messagebox, ttk

# In-memory storage for products
products = {}
product_id_counter = 1

def add_product(name, sku, category, price, quantity):
    """Add a new product to inventory"""
    global product_id_counter
    
    if sku in [p['sku'] for p in products.values()]:
        return False, "SKU already exists!"
    
    products[product_id_counter] = {
        'id': product_id_counter,
        'name': name,
        'sku': sku,
        'category': category,
        'price': price,
        'quantity': quantity
    }
    product_id_counter += 1
    return True, "Product added successfully!"

def get_all_products():
    """Get all products in inventory"""
    result = ""
    if not products:
        return "No products in inventory."
    
    for product in products.values():
        result += f"SKU: {product['sku']}, Name: {product['name']}, Category: {product['category']}, "
        result += f"Price: ${product['price']:.2f}, Stock: {product['quantity']}\n"
    return result

def search_product_by_sku(sku):
    """Search for a product by SKU"""
    for product in products.values():
        if product['sku'] == sku:
            return product
    return None

def add_product_button_click():
    """Handle add product button click"""
    try:
        name = name_entry.get().strip()
        sku = sku_entry.get().strip()
        category = category_entry.get().strip()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        
        if not name or not sku or not category:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        if price < 0 or quantity < 0:
            messagebox.showerror("Error", "Price and quantity must be positive!")
            return
        
        success, message = add_product(name, sku, category, price, quantity)
        
        if success:
            messagebox.showinfo("Success", message)
            # Clear entries
            name_entry.delete(0, tk.END)
            sku_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            result_text.delete(1.0, tk.END)
            result_text.insert(1.0, get_all_products())
        else:
            messagebox.showerror("Error", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please check price and quantity.")

def view_all_button_click():
    """Handle view all products button click"""
    result_text.delete(1.0, tk.END)
    result_text.insert(1.0, get_all_products())

def search_button_click():
    """Handle search button click"""
    sku = search_entry.get().strip()
    if not sku:
        messagebox.showerror("Error", "Please enter SKU to search!")
        return
    
    product = search_product_by_sku(sku)
    if product:
        result = f"Product Found!\n"
        result += f"Name: {product['name']}\n"
        result += f"SKU: {product['sku']}\n"
        result += f"Category: {product['category']}\n"
        result += f"Price: ${product['price']:.2f}\n"
        result += f"Stock: {product['quantity']}\n"
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, result)
    else:
        messagebox.showinfo("Not Found", f"No product found with SKU: {sku}")

if __name__ == "__main__":
    # Create main window
    window = tk.Tk()
    window.title("Plumberry Inventory Management")
    window.geometry("700x650")
    window.configure(bg='#f0f0f0')
    
    # Title
    title_label = tk.Label(window, text="🍇 Plumberry Inventory System", 
                          font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#6a0dad')
    title_label.pack(pady=10)
    
    # Add Product Frame
    add_frame = tk.LabelFrame(window, text="Add New Product", 
                             font=("Arial", 12, "bold"), bg='#f0f0f0', padx=20, pady=10)
    add_frame.pack(padx=20, pady=10, fill='x')
    
    # Product Name
    tk.Label(add_frame, text="Product Name:", bg='#f0f0f0').grid(row=0, column=0, sticky='w', pady=5)
    name_entry = tk.Entry(add_frame, width=30)
    name_entry.grid(row=0, column=1, pady=5)
    
    # SKU
    tk.Label(add_frame, text="SKU:", bg='#f0f0f0').grid(row=1, column=0, sticky='w', pady=5)
    sku_entry = tk.Entry(add_frame, width=30)
    sku_entry.grid(row=1, column=1, pady=5)
    
    # Category
    tk.Label(add_frame, text="Category:", bg='#f0f0f0').grid(row=2, column=0, sticky='w', pady=5)
    category_entry = tk.Entry(add_frame, width=30)
    category_entry.grid(row=2, column=1, pady=5)
    
    # Price
    tk.Label(add_frame, text="Price ($):", bg='#f0f0f0').grid(row=3, column=0, sticky='w', pady=5)
    price_entry = tk.Entry(add_frame, width=30)
    price_entry.grid(row=3, column=1, pady=5)
    
    # Quantity
    tk.Label(add_frame, text="Quantity:", bg='#f0f0f0').grid(row=4, column=0, sticky='w', pady=5)
    quantity_entry = tk.Entry(add_frame, width=30)
    quantity_entry.grid(row=4, column=1, pady=5)
    
    # Add Button
    add_button = tk.Button(add_frame, text="Add Product", command=add_product_button_click,
                          bg='#6a0dad', fg='white', font=("Arial", 10, "bold"))
    add_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    # Search Frame
    search_frame = tk.LabelFrame(window, text="Search Product", 
                                font=("Arial", 12, "bold"), bg='#f0f0f0', padx=20, pady=10)
    search_frame.pack(padx=20, pady=5, fill='x')
    
    tk.Label(search_frame, text="Enter SKU:", bg='#f0f0f0').pack(side='left', padx=5)
    search_entry = tk.Entry(search_frame, width=20)
    search_entry.pack(side='left', padx=5)
    
    search_button = tk.Button(search_frame, text="Search", command=search_button_click,
                             bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
    search_button.pack(side='left', padx=5)
    
    view_all_button = tk.Button(search_frame, text="View All Products", command=view_all_button_click,
                               bg='#2196F3', fg='white', font=("Arial", 10, "bold"))
    view_all_button.pack(side='left', padx=5)
    
    # Results Frame
    results_frame = tk.LabelFrame(window, text="Inventory List", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0', padx=10, pady=10)
    results_frame.pack(padx=20, pady=10, fill='both', expand=True)
    
    # Text widget with scrollbar
    result_text = tk.Text(results_frame, height=10, width=70, wrap='word')
    scrollbar = tk.Scrollbar(results_frame, command=result_text.yview)
    result_text.configure(yscrollcommand=scrollbar.set)
    
    result_text.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    # Add some sample data
    add_product("Plumberry Jam", "PLM001", "Preserves", 12.99, 50)
    add_product("Dried Plumberries", "PLM002", "Dried Fruits", 8.50, 100)
    add_product("Plumberry Juice", "PLM003", "Beverages", 5.99, 75)
    add_product("Plumberry Tea", "PLM004", "Beverages", 7.25, 60)
    
    # Display initial inventory
    result_text.insert(1.0, get_all_products())
    
    window.mainloop()