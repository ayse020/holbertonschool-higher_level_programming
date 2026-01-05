import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format
    
    Args:
        csv_filename (str): Path to the CSV file
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Read CSV data using DictReader
            csv_reader = csv.DictReader(csv_file)
            
            # Convert to list of dictionaries
            data_list = []
            for row in csv_reader:
                data_list.append(row)
        
        # Write JSON data to file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found")
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
