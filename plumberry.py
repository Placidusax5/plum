#!/usr/bin/env python3
"""
Plumberry Inventory Management System - Terminal Interface
Interactive command-line application for managing plumberry inventory
"""

from datetime import datetime
import os

# In-memory storage
products = {}
transactions = []
product_id = 1
transaction_id = 1

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_header():
    """Print application header"""
    print("\n" + "="*70)
    print(" "*15 + "🍇 PLUMBERRY INVENTORY SYSTEM 🍇")
    print("="*70)

def add_product():
    """Add a new product"""
    global product_id
    
    print("\n📦 ADD NEW PRODUCT")
    print("-" * 70)
    
    name = input("Product Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return
    
    sku = input("SKU: ").strip().upper()
    if not sku:
        print("❌ SKU cannot be empty!")
        return
    
    if sku in [p['sku'] for p in products.values()]:
        print(f"❌ SKU {sku} already exists!")
        return
    
    category = input("Category: ").strip()
    
    try:
        price = float(input("Price ($): "))
        quantity = int(input("Quantity: "))
        
        if price < 0 or quantity < 0:
            print("❌ Price and quantity must be positive!")
            return
        
        products[product_id] = {
            'id': product_id,
            'name': name,
            'sku': sku,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        product_id += 1
        print(f"\n✅ Product '{name}' added successfully!")
        
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")

def view_inventory():
    """Display all products"""
    print("\n📋 CURRENT INVENTORY")
    print("="*70)
    
    if not products:
        print("No products in inventory.")
        return
    
    total_value = 0
    for product in products.values():
        status = "🔴 LOW" if product['quantity'] < 30 else "🟢 OK "
        value = product['price'] * product['quantity']
        total_value += value
        
        print(f"{status} | SKU: {product['sku']:8} | {product['name']:20}")
        print(f"     Category: {product['category']:15} | Price: ${product['price']:6.2f} | Stock: {product['quantity']:3} | Value: ${value:.2f}")
        print("-" * 70)
    
    print(f"\n💰 Total Inventory Value: ${total_value:.2f}")
    print(f"📦 Total Products: {len(products)}")

def add_stock():
    """Add stock to existing product"""
    global transaction_id
    
    print("\n➕ ADD STOCK (Incoming)")
    print("-" * 70)
    
    sku = input("Product SKU: ").strip().upper()
    
    found = None
    for product in products.values():
        if product['sku'] == sku:
            found = product
            break
    
    if not found:
        print(f"❌ Product with SKU {sku} not found!")
        return
    
    try:
        quantity = int(input("Quantity to add: "))
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            return
        
        notes = input("Notes (optional): ").strip()
        
        found['quantity'] += quantity
        
        transactions.append({
            'id': transaction_id,
            'sku': sku,
            'product_name': found['name'],
            'type': 'IN',
            'quantity': quantity,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'notes': notes
        })
        transaction_id += 1
        
        print(f"\n✅ Added {quantity} units to {found['name']}")
        print(f"   New stock level: {found['quantity']}")
        
    except ValueError:
        print("❌ Invalid quantity!")

def remove_stock():
    """Remove stock from product"""
    global transaction_id
    
    print("\n➖ REMOVE STOCK (Outgoing/Sales)")
    print("-" * 70)
    
    sku = input("Product SKU: ").strip().upper()
    
    found = None
    for product in products.values():
        if product['sku'] == sku:
            found = product
            break
    
    if not found:
        print(f"❌ Product with SKU {sku} not found!")
        return
    
    print(f"   Available stock: {found['quantity']} units")
    
    try:
        quantity = int(input("Quantity to remove: "))
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            return
        
        if found['quantity'] < quantity:
            print(f"❌ Insufficient stock! Available: {found['quantity']}")
            return
        
        notes = input("Notes (optional): ").strip()
        
        found['quantity'] -= quantity
        
        transactions.append({
            'id': transaction_id,
            'sku': sku,
            'product_name': found['name'],
            'type': 'OUT',
            'quantity': quantity,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'notes': notes
        })
        transaction_id += 1
        
        print(f"\n✅ Removed {quantity} units from {found['name']}")
        print(f"   Remaining stock: {found['quantity']}")
        
    except ValueError:
        print("❌ Invalid quantity!")

def view_transactions():
    """Display transaction history"""
    print("\n📊 TRANSACTION HISTORY")
    print("="*70)
    
    if not transactions:
        print("No transactions recorded.")
        return
    
    count = min(20, len(transactions))
    print(f"Showing last {count} transactions:\n")
    
    for trans in reversed(transactions[-20:]):
        symbol = "➕ IN " if trans['type'] == 'IN' else "➖ OUT"
        print(f"{symbol} | ID: {trans['id']:3} | {trans['product_name']:20} ({trans['sku']})")
        print(f"       Qty: {trans['quantity']:3} | Time: {trans['timestamp']}")
        if trans['notes']:
            print(f"       Notes: {trans['notes']}")
        print("-" * 70)

def search_product():
    """Search for a product by SKU"""
    print("\n🔍 SEARCH PRODUCT")
    print("-" * 70)
    
    sku = input("Enter SKU: ").strip().upper()
    
    found = None
    for product in products.values():
        if product['sku'] == sku:
            found = product
            break
    
    if found:
        print("\n✅ Product Found!")
        print("="*70)
        print(f"Name:     {found['name']}")
        print(f"SKU:      {found['sku']}")
        print(f"Category: {found['category']}")
        print(f"Price:    ${found['price']:.2f}")
        print(f"Stock:    {found['quantity']} units")
        print(f"Value:    ${found['price'] * found['quantity']:.2f}")
        
        status = "🔴 LOW STOCK - Reorder needed!" if found['quantity'] < 30 else "🟢 Stock level OK"
        print(f"Status:   {status}")
    else:
        print(f"\n❌ No product found with SKU: {sku}")

def load_sample_data():
    """Load sample products and transactions"""
    global product_id, transaction_id
    
    # Add sample products
    sample_products = [
        ("Plumberry Jam", "PLM001", "Preserves", 12.99, 50),
        ("Dried Plumberries", "PLM002", "Dried Fruits", 8.50, 100),
        ("Plumberry Juice", "PLM003", "Beverages", 5.99, 75),
        ("Plumberry Tea", "PLM004", "Beverages", 7.25, 60),
    ]
    
    for name, sku, category, price, quantity in sample_products:
        products[product_id] = {
            'id': product_id,
            'name': name,
            'sku': sku,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        product_id += 1
    
    # Add sample transactions
    transactions.append({
        'id': transaction_id,
        'sku': 'PLM001',
        'product_name': 'Plumberry Jam',
        'type': 'IN',
        'quantity': 30,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'notes': 'Initial stock from supplier'
    })
    transaction_id += 1

def main():
    """Main application loop"""
    load_sample_data()
    
    while True:
        print_header()
        print("\n📱 MAIN MENU")
        print("-" * 70)
        print("1. Add New Product")
        print("2. View Inventory")
        print("3. Add Stock (Incoming)")
        print("4. Remove Stock (Sales/Outgoing)")
        print("5. View Transaction History")
        print("6. Search Product by SKU")
        print("7. Exit")
        print("-" * 70)
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            add_stock()
        elif choice == '4':
            remove_stock()
        elif choice == '5':
            view_transactions()
        elif choice == '6':
            search_product()
        elif choice == '7':
            print("\n✅ Thank you for using Plumberry Inventory System!")
            print("="*70 + "\n")
            break
        else:
            print("\n❌ Invalid option! Please select 1-7.")
        
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Application closed by user.")
        print("="*70 + "\n")
