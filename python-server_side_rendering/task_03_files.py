#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def display_products():
    """
    Display products from JSON or CSV file
    Query parameters:
    - source: 'json' or 'csv' (required)
    - id: product ID to filter by (optional)
    """
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if not source:
        return render_template('product_display.html', 
                             error="Source parameter is required")
    
    # Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    products = []
    if source == 'json':
        products = read_json_file()
    else:  # source == 'csv'
        products = read_csv_file()
    
    # Filter by ID if provided
    if product_id:
        filtered_products = []
        for product in products:
            if str(product.get('id')) == str(product_id):
                filtered_products.append(product)
        
        if not filtered_products:
            return render_template('product_display.html', 
                                 error="Product not found")
        
        products = filtered_products
    
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
