#!/usr/bin/env python3
"""
Plumberry Inventory Management System - Main Application Launcher
This is the main entry point that allows users to choose which module to run.
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class PlumberryMainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plumberry Inventory System - Main Menu")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Title
        title_label = tk.Label(
            root, 
            text="🍇 Plumberry Inventory\nManagement System", 
            font=("Arial", 20, "bold"), 
            bg='#f0f0f0', 
            fg='#6a0dad',
            justify='center'
        )
        title_label.pack(pady=30)
        
        # Subtitle
        subtitle_label = tk.Label(
            root, 
            text="Select a module to launch:", 
            font=("Arial", 12), 
            bg='#f0f0f0'
        )
        subtitle_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(root, bg='#f0f0f0')
        button_frame.pack(pady=20, expand=True)
        
        # Inventory Management Button
        inventory_btn = tk.Button(
            button_frame,
            text="📦 Product Inventory\nManagement",
            command=self.launch_inventory,
            bg='#6a0dad',
            fg='white',
            font=("Arial", 12, "bold"),
            width=20,
            height=3,
            cursor='hand2'
        )
        inventory_btn.pack(pady=10)
        
        # Stock Tracking Button
        stock_btn = tk.Button(
            button_frame,
            text="📊 Stock Tracking\n& Transactions",
            command=self.launch_stock_tracking,
            bg='#2196F3',
            fg='white',
            font=("Arial", 12, "bold"),
            width=20,
            height=3,
            cursor='hand2'
        )
        stock_btn.pack(pady=10)
        
        # Exit Button
        exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            command=self.exit_app,
            bg='#f44336',
            fg='white',
            font=("Arial", 10, "bold"),
            width=20,
            height=2,
            cursor='hand2'
        )
        exit_btn.pack(pady=20)
        
        # Footer
        footer_label = tk.Label(
            root,
            text="Version 1.0 | Database-Free Prototype",
            font=("Arial", 9),
            bg='#f0f0f0',
            fg='#666'
        )
        footer_label.pack(side='bottom', pady=10)
    
    def launch_inventory(self):
        """Launch the inventory management module"""
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'inventory_management.py')
            subprocess.Popen([sys.executable, script_path])
            messagebox.showinfo("Module Launched", "Inventory Management module is now running in a separate window.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Inventory Management:\n{str(e)}")
    
    def launch_stock_tracking(self):
        """Launch the stock tracking module"""
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'stock_tracking.py')
            subprocess.Popen([sys.executable, script_path])
            messagebox.showinfo("Module Launched", "Stock Tracking module is now running in a separate window.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Stock Tracking:\n{str(e)}")
    
    def exit_app(self):
        """Exit the application"""
        if messagebox.askokcancel("Exit", "Do you want to exit the Plumberry Inventory System?"):
            self.root.quit()

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PlumberryMainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
