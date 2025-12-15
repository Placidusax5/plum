import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# In-memory storage for stock transactions
transactions = []
transaction_id_counter = 1

# Import products from inventory_management
# For demo, we'll maintain a local copy
stock_data = {
    "PLM001": {"name": "Plumberry Jam", "quantity": 50},
    "PLM002": {"name": "Dried Plumberries", "quantity": 100},
    "PLM003": {"name": "Plumberry Juice", "quantity": 75},
    "PLM004": {"name": "Plumberry Tea", "quantity": 60}
}

def add_stock(sku, quantity, notes=""):
    """Add stock to inventory (incoming)"""
    global transaction_id_counter
    
    if sku not in stock_data:
        return False, f"Product with SKU {sku} not found!"
    
    stock_data[sku]["quantity"] += quantity
    
    transaction = {
        'id': transaction_id_counter,
        'sku': sku,
        'product_name': stock_data[sku]["name"],
        'type': 'IN',
        'quantity': quantity,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'notes': notes
    }
    transactions.append(transaction)
    transaction_id_counter += 1
    
    return True, f"Added {quantity} units to {stock_data[sku]['name']}"

def remove_stock(sku, quantity, notes=""):
    """Remove stock from inventory (outgoing/sales)"""
    global transaction_id_counter
    
    if sku not in stock_data:
        return False, f"Product with SKU {sku} not found!"
    
    if stock_data[sku]["quantity"] < quantity:
        return False, f"Insufficient stock! Available: {stock_data[sku]['quantity']}"
    
    stock_data[sku]["quantity"] -= quantity
    
    transaction = {
        'id': transaction_id_counter,
        'sku': sku,
        'product_name': stock_data[sku]["name"],
        'type': 'OUT',
        'quantity': quantity,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'notes': notes
    }
    transactions.append(transaction)
    transaction_id_counter += 1
    
    return True, f"Removed {quantity} units from {stock_data[sku]['name']}"

def get_stock_level(sku):
    """Get current stock level for a product"""
    if sku in stock_data:
        return stock_data[sku]["quantity"]
    return None

def get_all_stock():
    """Get all stock levels"""
    result = "Current Stock Levels:\n" + "="*50 + "\n"
    for sku, data in stock_data.items():
        status = "🔴 LOW" if data["quantity"] < 30 else "🟢 OK"
        result += f"{status} SKU: {sku}, Product: {data['name']}, Stock: {data['quantity']}\n"
    return result

def get_transaction_history():
    """Get transaction history"""
    if not transactions:
        return "No transactions recorded."
    
    result = "Transaction History:\n" + "="*50 + "\n"
    for trans in reversed(transactions[-20:]):  # Show last 20 transactions
        symbol = "➕" if trans['type'] == 'IN' else "➖"
        result += f"{symbol} ID: {trans['id']}, {trans['product_name']} ({trans['sku']})\n"
        result += f"   Qty: {trans['quantity']}, Time: {trans['timestamp']}\n"
        if trans['notes']:
            result += f"   Notes: {trans['notes']}\n"
        result += "\n"
    return result

def add_stock_button_click():
    """Handle add stock button click"""
    try:
        sku = sku_entry.get().strip()
        quantity = int(quantity_entry.get())
        notes = notes_entry.get().strip()
        
        if not sku:
            messagebox.showerror("Error", "Please enter SKU!")
            return
        
        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be positive!")
            return
        
        success, message = add_stock(sku, quantity, notes)
        
        if success:
            messagebox.showinfo("Success", message)
            sku_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            notes_entry.delete(0, tk.END)
            update_displays()
        else:
            messagebox.showerror("Error", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity!")

def remove_stock_button_click():
    """Handle remove stock button click"""
    try:
        sku = sku_entry.get().strip()
        quantity = int(quantity_entry.get())
        notes = notes_entry.get().strip()
        
        if not sku:
            messagebox.showerror("Error", "Please enter SKU!")
            return
        
        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be positive!")
            return
        
        success, message = remove_stock(sku, quantity, notes)
        
        if success:
            messagebox.showinfo("Success", message)
            sku_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            notes_entry.delete(0, tk.END)
            update_displays()
        else:
            messagebox.showerror("Error", message)
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity!")

def update_displays():
    """Update stock and transaction displays"""
    stock_text.delete(1.0, tk.END)
    stock_text.insert(1.0, get_all_stock())
    
    trans_text.delete(1.0, tk.END)
    trans_text.insert(1.0, get_transaction_history())

def view_transaction_history():
    """View transaction history button click"""
    trans_text.delete(1.0, tk.END)
    trans_text.insert(1.0, get_transaction_history())

if __name__ == "__main__":
    # Create main window
    window = tk.Tk()
    window.title("Plumberry Stock Tracking")
    window.geometry("800x700")
    window.configure(bg='#f0f0f0')
    
    # Title
    title_label = tk.Label(window, text="📦 Plumberry Stock Management", 
                          font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#6a0dad')
    title_label.pack(pady=10)
    
    # Stock Transaction Frame
    trans_frame = tk.LabelFrame(window, text="Stock Transaction", 
                               font=("Arial", 12, "bold"), bg='#f0f0f0', padx=20, pady=10)
    trans_frame.pack(padx=20, pady=10, fill='x')
    
    # SKU
    tk.Label(trans_frame, text="Product SKU:", bg='#f0f0f0').grid(row=0, column=0, sticky='w', pady=5)
    sku_entry = tk.Entry(trans_frame, width=30)
    sku_entry.grid(row=0, column=1, pady=5, padx=5)
    
    # Quantity
    tk.Label(trans_frame, text="Quantity:", bg='#f0f0f0').grid(row=1, column=0, sticky='w', pady=5)
    quantity_entry = tk.Entry(trans_frame, width=30)
    quantity_entry.grid(row=1, column=1, pady=5, padx=5)
    
    # Notes
    tk.Label(trans_frame, text="Notes:", bg='#f0f0f0').grid(row=2, column=0, sticky='w', pady=5)
    notes_entry = tk.Entry(trans_frame, width=30)
    notes_entry.grid(row=2, column=1, pady=5, padx=5)
    
    # Buttons
    button_frame = tk.Frame(trans_frame, bg='#f0f0f0')
    button_frame.grid(row=3, column=0, columnspan=2, pady=10)
    
    add_button = tk.Button(button_frame, text="➕ Add Stock (IN)", command=add_stock_button_click,
                          bg='#4CAF50', fg='white', font=("Arial", 10, "bold"), width=15)
    add_button.pack(side='left', padx=5)
    
    remove_button = tk.Button(button_frame, text="➖ Remove Stock (OUT)", command=remove_stock_button_click,
                             bg='#f44336', fg='white', font=("Arial", 10, "bold"), width=18)
    remove_button.pack(side='left', padx=5)
    
    # Current Stock Frame
    stock_frame = tk.LabelFrame(window, text="Current Stock Levels", 
                               font=("Arial", 12, "bold"), bg='#f0f0f0', padx=10, pady=10)
    stock_frame.pack(padx=20, pady=5, fill='both', expand=True)
    
    stock_text = tk.Text(stock_frame, height=8, width=80, wrap='word')
    stock_scrollbar = tk.Scrollbar(stock_frame, command=stock_text.yview)
    stock_text.configure(yscrollcommand=stock_scrollbar.set)
    
    stock_text.pack(side='left', fill='both', expand=True)
    stock_scrollbar.pack(side='right', fill='y')
    
    # Transaction History Frame
    history_frame = tk.LabelFrame(window, text="Transaction History", 
                                 font=("Arial", 12, "bold"), bg='#f0f0f0', padx=10, pady=10)
    history_frame.pack(padx=20, pady=5, fill='both', expand=True)
    
    trans_text = tk.Text(history_frame, height=10, width=80, wrap='word')
    trans_scrollbar = tk.Scrollbar(history_frame, command=trans_text.yview)
    trans_text.configure(yscrollcommand=trans_scrollbar.set)
    
    trans_text.pack(side='left', fill='both', expand=True)
    trans_scrollbar.pack(side='right', fill='y')
    
    # Add some sample transactions
    add_stock("PLM001", 20, "Restock from supplier")
    remove_stock("PLM002", 15, "Customer order #1234")
    add_stock("PLM003", 30, "New shipment")
    remove_stock("PLM004", 10, "Store sale")
    
    # Initial display
    update_displays()
    
    window.mainloop()