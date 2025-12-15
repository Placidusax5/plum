#!/usr/bin/env python3
"""
Plumberry Inventory Management System - Demo Script
This script demonstrates the functionality without requiring a GUI.
"""

from datetime import datetime

# In-memory storage
products = {}
transactions = []
product_id = 1
transaction_id = 1

def add_product(name, sku, category, price, quantity):
    """Add a new product to inventory"""
    global product_id
    
    if sku in [p['sku'] for p in products.values()]:
        return False, "SKU already exists!"
    
    products[product_id] = {
        'id': product_id,
        'name': name,
        'sku': sku,
        'category': category,
        'price': price,
        'quantity': quantity
    }
    product_id += 1
    return True, f"✓ Added: {name} (SKU: {sku})"

def add_stock(sku, quantity, notes=""):
    """Add stock to inventory"""
    global transaction_id
    
    for product in products.values():
        if product['sku'] == sku:
            product['quantity'] += quantity
            transactions.append({
                'id': transaction_id,
                'sku': sku,
                'product_name': product['name'],
                'type': 'IN',
                'quantity': quantity,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'notes': notes
            })
            transaction_id += 1
            return True, f"✓ Added {quantity} units to {product['name']}"
    
    return False, f"Product with SKU {sku} not found!"

def remove_stock(sku, quantity, notes=""):
    """Remove stock from inventory"""
    global transaction_id
    
    for product in products.values():
        if product['sku'] == sku:
            if product['quantity'] < quantity:
                return False, f"Insufficient stock! Available: {product['quantity']}"
            
            product['quantity'] -= quantity
            transactions.append({
                'id': transaction_id,
                'sku': sku,
                'product_name': product['name'],
                'type': 'OUT',
                'quantity': quantity,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'notes': notes
            })
            transaction_id += 1
            return True, f"✓ Removed {quantity} units from {product['name']}"
    
    return False, f"Product with SKU {sku} not found!"

def display_inventory():
    """Display all products"""
    print("\n" + "="*70)
    print(" "*20 + "CURRENT INVENTORY")
    print("="*70)
    
    if not products:
        print("No products in inventory.")
        return
    
    for product in products.values():
        status = "🔴 LOW" if product['quantity'] < 30 else "🟢 OK "
        print(f"{status} | SKU: {product['sku']:8} | {product['name']:20} | "
              f"${product['price']:6.2f} | Stock: {product['quantity']:3}")
    print("="*70)

def display_transactions():
    """Display transaction history"""
    print("\n" + "="*70)
    print(" "*22 + "TRANSACTION HISTORY")
    print("="*70)
    
    if not transactions:
        print("No transactions recorded.")
        return
    
    for trans in reversed(transactions[-10:]):
        symbol = "➕ IN " if trans['type'] == 'IN' else "➖ OUT"
        print(f"{symbol} | ID: {trans['id']:3} | {trans['product_name']:20} | "
              f"Qty: {trans['quantity']:3} | {trans['timestamp']}")
        if trans['notes']:
            print(f"      Notes: {trans['notes']}")
    print("="*70)

def main():
    """Main demo function"""
    print("\n" + "="*70)
    print(" "*15 + "🍇 PLUMBERRY INVENTORY SYSTEM DEMO 🍇")
    print("="*70)
    
    # Demo: Adding Products
    print("\n📦 ADDING PRODUCTS TO INVENTORY...")
    print("-" * 70)
    
    success, msg = add_product("Plumberry Jam", "PLM001", "Preserves", 12.99, 50)
    print(msg)
    
    success, msg = add_product("Dried Plumberries", "PLM002", "Dried Fruits", 8.50, 100)
    print(msg)
    
    success, msg = add_product("Plumberry Juice", "PLM003", "Beverages", 5.99, 75)
    print(msg)
    
    success, msg = add_product("Plumberry Tea", "PLM004", "Beverages", 7.25, 60)
    print(msg)
    
    success, msg = add_product("Plumberry Extract", "PLM005", "Extracts", 15.99, 25)
    print(msg)
    
    # Display inventory
    display_inventory()
    
    # Demo: Stock Transactions
    print("\n📊 PERFORMING STOCK TRANSACTIONS...")
    print("-" * 70)
    
    success, msg = add_stock("PLM001", 30, "Restock from supplier ABC")
    print(msg)
    
    success, msg = remove_stock("PLM002", 20, "Customer order #1001")
    print(msg)
    
    success, msg = add_stock("PLM003", 50, "New shipment arrived")
    print(msg)
    
    success, msg = remove_stock("PLM004", 15, "Store sale - Weekend special")
    print(msg)
    
    success, msg = remove_stock("PLM001", 10, "Online order #1002")
    print(msg)
    
    success, msg = add_stock("PLM005", 20, "Restock low inventory")
    print(msg)
    
    # Display updated inventory
    display_inventory()
    
    # Display transactions
    display_transactions()
    
    # Demo: Search functionality
    print("\n🔍 SEARCHING FOR PRODUCT (SKU: PLM003)...")
    print("-" * 70)
    
    found = False
    for product in products.values():
        if product['sku'] == "PLM003":
            print(f"Product Found!")
            print(f"  Name: {product['name']}")
            print(f"  SKU: {product['sku']}")
            print(f"  Category: {product['category']}")
            print(f"  Price: ${product['price']:.2f}")
            print(f"  Stock: {product['quantity']} units")
            found = True
            break
    
    if not found:
        print("Product not found.")
    
    # Summary
    print("\n" + "="*70)
    print(" "*25 + "SUMMARY STATISTICS")
    print("="*70)
    print(f"Total Products: {len(products)}")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Stock Value: ${sum(p['price'] * p['quantity'] for p in products.values()):.2f}")
    
    low_stock = [p for p in products.values() if p['quantity'] < 30]
    print(f"Low Stock Alerts: {len(low_stock)} products")
    if low_stock:
        print("\nProducts needing restock:")
        for p in low_stock:
            print(f"  - {p['name']} (SKU: {p['sku']}): {p['quantity']} units")
    
    print("\n" + "="*70)
    print(" "*15 + "✓ DEMO COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nTo run the GUI version, execute:")
    print("  python main_app.py           (Main launcher)")
    print("  python inventory_management.py   (Product management)")
    print("  python stock_tracking.py         (Stock tracking)")
    print("\nNote: GUI requires a display environment.\n")

if __name__ == "__main__":
    main()
