# Write a program to create a JSON file with a dictionary of key-value pairs.

import json

def create_json_file(filename, data):
    """Create a JSON file from a dictionary."""
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)  
        print(f"JSON file '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the JSON file: {e}")

def main():
   
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science", "History"],
        "address": {
            "street": "123 Main St",
            "zipcode": "10001"
        }
    }

    filename = "data.json"  
    create_json_file(filename, data)

if __name__ == "__main__":
    main()