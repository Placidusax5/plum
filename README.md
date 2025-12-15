# Plumberry Inventory Management System

# 🍇 Plumberry Inventory Management System  

A **Python-based Tkinter GUI** application for managing **plumberry inventory, stock levels, and sales**. This system allows users to add products, track inventory, manage stock, and view sales records using in-memory storage (no database required).  

## 📌 Features  

✅ **Product Management:**  
- Add new plumberry products (Name, SKU, Category, Price, Stock Quantity)  
- Update product information  
- View all products in inventory  
- Search products by SKU  

✅ **Stock Tracking:**  
- Track stock levels in real-time  
- Add stock (incoming inventory)  
- Remove stock (sales/outgoing inventory)  
- View low stock alerts  
- Generate inventory reports  

## 🛠️ Technologies Used  

- **Python** 🐍  
- **Tkinter** (for GUI)  
- **In-memory data structures** (dictionaries and lists)  

## 📂 File Overview  

1. **`inventory_management.py`** – Manages product inventory and operations  
2. **`stock_tracking.py`** – Handles stock levels and transactions  
3. **`main_app.py`** – Main application launcher  
4. **`README.md`** – Project documentation  

## 🚀 Quick Start Guide  

### **Step 1: Install Python**  

Make sure you have Python 3.7+ installed on your system.  

### **Step 2: Run the Application**  

Simply run the main application:

```sh
python main_app.py
```

Or run individual modules:

```sh
# Inventory Management
python inventory_management.py

# Stock Tracking
python stock_tracking.py
```

## 📱 Application Modules

### 1. Main Application Launcher (`main_app.py`)
- Central hub to access all modules
- Clean interface to launch different features
- Easy navigation between modules

### 2. Inventory Management (`inventory_management.py`)
- Add new plumberry products with details
- Search products by SKU
- View complete inventory list
- Pre-loaded with sample products:
  - PLM001: Plumberry Jam
  - PLM002: Dried Plumberries
  - PLM003: Plumberry Juice
  - PLM004: Plumberry Tea

### 3. Stock Tracking (`stock_tracking.py`)
- Add stock (incoming inventory)
- Remove stock (sales/outgoing)
- Real-time stock level monitoring
- Transaction history tracking
- Low stock alerts (< 30 units)
- Sample transactions included for demonstration

## 💡 Features Demonstration

### Adding Products
1. Launch Inventory Management module
2. Enter product details (Name, SKU, Category, Price, Quantity)
3. Click "Add Product" to save
4. View updated inventory list

### Managing Stock
1. Launch Stock Tracking module
2. Enter product SKU and quantity
3. Use "Add Stock" for incoming inventory
4. Use "Remove Stock" for sales/outgoing
5. View real-time stock levels and transaction history

### Sample Data
The system comes pre-loaded with sample products and transactions to demonstrate functionality immediately.

## 🎯 Technical Details

- **No Database Required**: Uses Python dictionaries and lists for data storage
- **In-Memory Storage**: Data persists during application runtime
- **GUI Framework**: Tkinter (comes with Python)
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 📝 Notes

This is a **working prototype** designed to demonstrate the Plumberry Inventory Management System without requiring database setup. All data is stored in memory and will be reset when the application is closed.

For production use, consider:
- Adding persistent storage (SQLite, PostgreSQL, etc.)
- Implementing user authentication
- Adding data export/import functionality
- Creating backup and restore features

---

**Version**: 1.0  
**Status**: Working Prototype  
**License**: MIT
