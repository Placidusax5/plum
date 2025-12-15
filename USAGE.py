#!/usr/bin/env python3
"""
Quick Usage Examples for Plumberry Inventory Management System
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║         🍇 PLUMBERRY INVENTORY MANAGEMENT SYSTEM 🍇                 ║
║                    Quick Usage Guide                                 ║
╚══════════════════════════════════════════════════════════════════════╝

This system has been successfully converted from a Student Management
System to a Plumberry Inventory Management System!

📁 PROJECT STRUCTURE:
──────────────────────────────────────────────────────────────────────
  ├── main_app.py               → Main application launcher (GUI)
  ├── inventory_management.py   → Product inventory management (GUI)
  ├── stock_tracking.py         → Stock tracking & transactions (GUI)
  ├── demo.py                   → Command-line demo (no GUI needed)
  └── README.md                 → Full documentation

🚀 HOW TO RUN:
──────────────────────────────────────────────────────────────────────

1. Run the demo (works everywhere, no GUI needed):
   $ python demo.py

2. Run the full GUI application (requires display):
   $ python main_app.py

3. Run individual modules (requires display):
   $ python inventory_management.py    # Product management
   $ python stock_tracking.py          # Stock tracking

✨ KEY FEATURES:
──────────────────────────────────────────────────────────────────────

Product Inventory Management:
  • Add new products with SKU, name, category, price, and quantity
  • Search products by SKU
  • View all products in inventory
  • Pre-loaded with sample plumberry products

Stock Tracking & Transactions:
  • Add stock (incoming inventory)
  • Remove stock (sales/outgoing)
  • Real-time stock level monitoring
  • Transaction history with timestamps
  • Low stock alerts (< 30 units)
  • Sample transactions included

💾 DATA STORAGE:
──────────────────────────────────────────────────────────────────────
  ✓ In-memory storage (no database required!)
  ✓ Python dictionaries and lists
  ✓ Data persists during runtime
  ✓ Resets when application closes

📦 SAMPLE PRODUCTS INCLUDED:
──────────────────────────────────────────────────────────────────────
  • PLM001 - Plumberry Jam (Preserves)
  • PLM002 - Dried Plumberries (Dried Fruits)
  • PLM003 - Plumberry Juice (Beverages)
  • PLM004 - Plumberry Tea (Beverages)
  • PLM005 - Plumberry Extract (Extracts) [added in demo]

🎯 TYPICAL WORKFLOW:
──────────────────────────────────────────────────────────────────────

1. Launch main_app.py
2. Click "Product Inventory Management" to:
   - View existing products
   - Add new products
   - Search for products
3. Click "Stock Tracking & Transactions" to:
   - Add incoming stock
   - Record sales/outgoing stock
   - View transaction history
   - Check stock levels

📝 NOTES:
──────────────────────────────────────────────────────────────────────
  • This is a working prototype (no database setup needed)
  • Perfect for demonstrations and testing
  • Ready for extension with persistent storage
  • Cross-platform compatible (Windows, macOS, Linux)

🔧 TECHNICAL DETAILS:
──────────────────────────────────────────────────────────────────────
  • Language: Python 3.7+
  • GUI Framework: Tkinter (built-in)
  • Storage: In-memory (dictionaries/lists)
  • No external dependencies required!

💡 TIP:
──────────────────────────────────────────────────────────────────────
If you're running this in an environment without a GUI display
(like a dev container or server), use the demo.py script to see
the full functionality in action!

Try it now:  python demo.py

╚══════════════════════════════════════════════════════════════════════╝
""")
