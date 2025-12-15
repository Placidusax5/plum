#!/usr/bin/env python3
"""
Plumberry Inventory Management System - Streamlit Web Interface
A modern, web-based UI for managing plumberry inventory
"""

import streamlit as st
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Plumberry Inventory System",
    page_icon="🍇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stAlert {
        padding: 1rem;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #6a0dad;
    }
    h1 {
        color: #6a0dad;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'products' not in st.session_state:
    st.session_state.products = {
        1: {'id': 1, 'name': 'Plumberry Jam', 'sku': 'PLM001', 'category': 'Preserves', 'price': 12.99, 'quantity': 50},
        2: {'id': 2, 'name': 'Dried Plumberries', 'sku': 'PLM002', 'category': 'Dried Fruits', 'price': 8.50, 'quantity': 100},
        3: {'id': 3, 'name': 'Plumberry Juice', 'sku': 'PLM003', 'category': 'Beverages', 'price': 5.99, 'quantity': 75},
        4: {'id': 4, 'name': 'Plumberry Tea', 'sku': 'PLM004', 'category': 'Beverages', 'price': 7.25, 'quantity': 60},
    }

if 'transactions' not in st.session_state:
    st.session_state.transactions = []

if 'product_id_counter' not in st.session_state:
    st.session_state.product_id_counter = 5

if 'transaction_id_counter' not in st.session_state:
    st.session_state.transaction_id_counter = 1

# Functions
def add_product(name, sku, category, price, quantity):
    """Add a new product"""
    # Check if SKU exists
    for product in st.session_state.products.values():
        if product['sku'] == sku:
            return False, "SKU already exists!"
    
    st.session_state.products[st.session_state.product_id_counter] = {
        'id': st.session_state.product_id_counter,
        'name': name,
        'sku': sku,
        'category': category,
        'price': price,
        'quantity': quantity
    }
    st.session_state.product_id_counter += 1
    return True, "Product added successfully!"

def add_stock(sku, quantity, notes=""):
    """Add stock to existing product"""
    for product in st.session_state.products.values():
        if product['sku'] == sku:
            product['quantity'] += quantity
            st.session_state.transactions.append({
                'id': st.session_state.transaction_id_counter,
                'sku': sku,
                'product_name': product['name'],
                'type': 'IN',
                'quantity': quantity,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'notes': notes
            })
            st.session_state.transaction_id_counter += 1
            return True, f"Added {quantity} units to {product['name']}"
    return False, "Product not found!"

def remove_stock(sku, quantity, notes=""):
    """Remove stock from product"""
    for product in st.session_state.products.values():
        if product['sku'] == sku:
            if product['quantity'] < quantity:
                return False, f"Insufficient stock! Available: {product['quantity']}"
            product['quantity'] -= quantity
            st.session_state.transactions.append({
                'id': st.session_state.transaction_id_counter,
                'sku': sku,
                'product_name': product['name'],
                'type': 'OUT',
                'quantity': quantity,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'notes': notes
            })
            st.session_state.transaction_id_counter += 1
            return True, f"Removed {quantity} units from {product['name']}"
    return False, "Product not found!"

def get_inventory_df():
    """Get inventory as DataFrame"""
    if not st.session_state.products:
        return pd.DataFrame()
    
    data = []
    for product in st.session_state.products.values():
        value = product['price'] * product['quantity']
        status = "🔴 LOW" if product['quantity'] < 30 else "🟢 OK"
        data.append({
            'Status': status,
            'SKU': product['sku'],
            'Product Name': product['name'],
            'Category': product['category'],
            'Price ($)': f"${product['price']:.2f}",
            'Stock': product['quantity'],
            'Value ($)': f"${value:.2f}"
        })
    return pd.DataFrame(data)

def get_transactions_df():
    """Get transactions as DataFrame"""
    if not st.session_state.transactions:
        return pd.DataFrame()
    
    data = []
    for trans in reversed(st.session_state.transactions[-50:]):
        symbol = "➕ IN" if trans['type'] == 'IN' else "➖ OUT"
        data.append({
            'Type': symbol,
            'ID': trans['id'],
            'Product': trans['product_name'],
            'SKU': trans['sku'],
            'Quantity': trans['quantity'],
            'Timestamp': trans['timestamp'],
            'Notes': trans['notes']
        })
    return pd.DataFrame(data)

# Sidebar navigation
st.sidebar.title("🍇 Navigation")
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Inventory Management",
    "Stock Transactions",
    "Reports"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("Plumberry Inventory System v1.0\n\nManage your inventory without database dependencies.")

# Main content
if page == "Dashboard":
    st.title("🍇 Plumberry Inventory Dashboard")
    
    # Metrics
    total_products = len(st.session_state.products)
    total_value = sum(p['price'] * p['quantity'] for p in st.session_state.products.values())
    low_stock = sum(1 for p in st.session_state.products.values() if p['quantity'] < 30)
    total_transactions = len(st.session_state.transactions)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Products", total_products)
    with col2:
        st.metric("Total Value", f"${total_value:,.2f}")
    with col3:
        st.metric("Low Stock Items", low_stock, delta=None if low_stock == 0 else "Alert", delta_color="inverse")
    with col4:
        st.metric("Total Transactions", total_transactions)
    
    st.markdown("---")
    
    # Current Inventory
    st.subheader("📦 Current Inventory")
    df = get_inventory_df()
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No products in inventory.")
    
    # Recent Transactions
    st.markdown("---")
    st.subheader("📊 Recent Transactions")
    trans_df = get_transactions_df()
    if not trans_df.empty:
        st.dataframe(trans_df.head(10), use_container_width=True, hide_index=True)
    else:
        st.info("No transactions recorded.")

elif page == "Inventory Management":
    st.title("📦 Inventory Management")
    
    tab1, tab2 = st.tabs(["➕ Add Product", "🔍 View Inventory"])
    
    with tab1:
        st.subheader("Add New Product")
        with st.form("add_product_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Product Name *")
                sku = st.text_input("SKU *").upper()
                category = st.text_input("Category *")
            with col2:
                price = st.number_input("Price ($) *", min_value=0.0, step=0.01, format="%.2f")
                quantity = st.number_input("Initial Quantity *", min_value=0, step=1)
            
            submitted = st.form_submit_button("Add Product", use_container_width=True)
            
            if submitted:
                if not name or not sku or not category:
                    st.error("Please fill all required fields!")
                elif price <= 0:
                    st.error("Price must be greater than 0!")
                else:
                    success, message = add_product(name, sku, category, price, quantity)
                    if success:
                        st.success(message)
                        st.balloons()
                    else:
                        st.error(message)
    
    with tab2:
        st.subheader("Current Inventory")
        
        # Search
        search_col1, search_col2 = st.columns([3, 1])
        with search_col1:
            search_term = st.text_input("Search by SKU or Product Name", "")
        
        df = get_inventory_df()
        
        if not df.empty:
            if search_term:
                df = df[
                    df['SKU'].str.contains(search_term, case=False, na=False) |
                    df['Product Name'].str.contains(search_term, case=False, na=False)
                ]
            
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Summary
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Products Displayed", len(df))
            with col2:
                total = sum(float(v.replace('$', '').replace(',', '')) for v in df['Value ($)'])
                st.metric("Total Value", f"${total:,.2f}")
        else:
            st.info("No products in inventory.")

elif page == "Stock Transactions":
    st.title("📊 Stock Transactions")
    
    tab1, tab2, tab3 = st.tabs(["➕ Add Stock", "➖ Remove Stock", "📜 Transaction History"])
    
    with tab1:
        st.subheader("Add Stock (Incoming Inventory)")
        with st.form("add_stock_form"):
            sku_list = [p['sku'] for p in st.session_state.products.values()]
            sku = st.selectbox("Select Product SKU", sku_list)
            
            # Show current stock
            current_stock = next((p['quantity'] for p in st.session_state.products.values() if p['sku'] == sku), 0)
            st.info(f"Current Stock: {current_stock} units")
            
            quantity = st.number_input("Quantity to Add", min_value=1, step=1)
            notes = st.text_area("Notes (optional)")
            
            submitted = st.form_submit_button("Add Stock", use_container_width=True)
            
            if submitted:
                success, message = add_stock(sku, quantity, notes)
                if success:
                    st.success(message)
                else:
                    st.error(message)
    
    with tab2:
        st.subheader("Remove Stock (Sales/Outgoing)")
        with st.form("remove_stock_form"):
            sku_list = [p['sku'] for p in st.session_state.products.values()]
            sku = st.selectbox("Select Product SKU", sku_list, key="remove_sku")
            
            # Show current stock
            current_stock = next((p['quantity'] for p in st.session_state.products.values() if p['sku'] == sku), 0)
            st.info(f"Available Stock: {current_stock} units")
            
            quantity = st.number_input("Quantity to Remove", min_value=1, max_value=current_stock if current_stock > 0 else 1, step=1)
            notes = st.text_area("Notes (optional)", key="remove_notes")
            
            submitted = st.form_submit_button("Remove Stock", use_container_width=True)
            
            if submitted:
                success, message = remove_stock(sku, quantity, notes)
                if success:
                    st.success(message)
                else:
                    st.error(message)
    
    with tab3:
        st.subheader("Transaction History")
        
        trans_df = get_transactions_df()
        
        if not trans_df.empty:
            # Filter options
            col1, col2 = st.columns(2)
            with col1:
                trans_type = st.selectbox("Filter by Type", ["All", "➕ IN", "➖ OUT"])
            with col2:
                limit = st.slider("Show last N transactions", 10, 100, 20)
            
            # Apply filters
            filtered_df = trans_df.head(limit)
            if trans_type != "All":
                filtered_df = filtered_df[filtered_df['Type'] == trans_type]
            
            st.dataframe(filtered_df, use_container_width=True, hide_index=True)
            
            # Download option
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"transactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        else:
            st.info("No transactions recorded yet.")

elif page == "Reports":
    st.title("📈 Reports & Analytics")
    
    # Inventory Report
    st.subheader("📦 Inventory Summary Report")
    
    df = get_inventory_df()
    
    if not df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Stock Status")
            low_stock_items = len([p for p in st.session_state.products.values() if p['quantity'] < 30])
            ok_stock_items = len(st.session_state.products) - low_stock_items
            
            status_data = pd.DataFrame({
                'Status': ['🟢 OK', '🔴 LOW'],
                'Count': [ok_stock_items, low_stock_items]
            })
            st.bar_chart(status_data.set_index('Status'))
        
        with col2:
            st.markdown("#### Category Distribution")
            category_data = {}
            for p in st.session_state.products.values():
                category_data[p['category']] = category_data.get(p['category'], 0) + 1
            
            cat_df = pd.DataFrame({
                'Category': list(category_data.keys()),
                'Count': list(category_data.values())
            })
            st.bar_chart(cat_df.set_index('Category'))
        
        st.markdown("---")
        
        # Top Products by Value
        st.subheader("💰 Top Products by Inventory Value")
        products_list = []
        for p in st.session_state.products.values():
            value = p['price'] * p['quantity']
            products_list.append({
                'Product': p['name'],
                'Value': value
            })
        
        top_products_df = pd.DataFrame(products_list).sort_values('Value', ascending=False).head(5)
        st.bar_chart(top_products_df.set_index('Product'))
        
        # Low Stock Alert
        st.markdown("---")
        st.subheader("⚠️ Low Stock Alerts")
        low_stock_products = [p for p in st.session_state.products.values() if p['quantity'] < 30]
        
        if low_stock_products:
            for p in low_stock_products:
                st.warning(f"**{p['name']}** (SKU: {p['sku']}) - Only {p['quantity']} units remaining!")
        else:
            st.success("All products are adequately stocked!")
        
        # Export Report
        st.markdown("---")
        st.subheader("📥 Export Options")
        
        col1, col2 = st.columns(2)
        with col1:
            inventory_csv = df.to_csv(index=False)
            st.download_button(
                label="Download Inventory Report (CSV)",
                data=inventory_csv,
                file_name=f"inventory_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        
        with col2:
            trans_df = get_transactions_df()
            if not trans_df.empty:
                trans_csv = trans_df.to_csv(index=False)
                st.download_button(
                    label="Download Transactions Report (CSV)",
                    data=trans_csv,
                    file_name=f"transactions_report_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
    else:
        st.info("No data available for reports.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Plumberry Inventory Management System v1.0 | "
    "Developed by Amogh S Pattanashetti & Bhuvan M"
    "</div>",
    unsafe_allow_html=True
)
