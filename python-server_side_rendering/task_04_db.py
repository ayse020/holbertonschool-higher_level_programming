#!/usr/bin/python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def read_json_file():
    """Read and parse data from JSON file"""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def read_csv_file():
    """Read and parse data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return []
    except Exception:
        return []


def read_sqlite_db():
    """Read and parse data from SQLite database"""
    try:
        if not os.path.exists('products.db'):
            return []
            
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Get all products from database
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        
        products = []
        for row in rows:
            product = {
                'id': str(row[0]),
                'name': row[1],
                'category': row[2],
                'price': float(row[3])
            }
            products.append(product)
        
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Error reading database: {e}")
        return []


@app.route('/products')
def display_products():
    """
    Display products from JSON, CSV, or SQLite database
    Query parameters:
    - source: 'json', 'csv', or 'sql' (required)
    - id: product ID to filter by (optional)
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if not source:
        return render_template('product_display.html', 
                             error="Source parameter is required. Use ?source=json, ?source=csv, or ?source=sql")
    
    # Check if source is valid
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error=f"Wrong source: '{source}'. Use 'json', 'csv', or 'sql'.")
    
    # Read data based on source
    products = []
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:  # source == 'sql'
        products = read_sqlite_db()
    
    # Filter by ID if provided
    if product_id:
        product_id_str = str(product_id).strip()
        filtered_products = []
        for product in products:
            if str(product.get('id')) == product_id_str:
                filtered_products.append(product)
        
        if not filtered_products:
            return render_template('product_display.html', 
                                 error=f"Product with ID '{product_id}' not found.")
        
        products = filtered_products
    
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    # Check if required files exist
    if not os.path.exists('products.json'):
        print("Warning: products.json file not found!")
    if not os.path.exists('products.csv'):
        print("Warning: products.csv file not found!")
    if not os.path.exists('products.db'):
        print("Warning: products.db file not found! Run create_db.py first.")
    
    app.run(debug=True, port=5000)
