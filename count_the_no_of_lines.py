# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:41:33 2024

@author: iTA
"""

# Create a program to count the number of lines in a text file.

def count_lines_in_file(filename):
    """Count the number of lines in a text file."""
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)  # Count lines using a generator expression
        return line_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    filename = input("Enter the name of the text file to count lines: ")
    line_count = count_lines_in_file(filename)
    
    if line_count is not None:
        print(f"The file '{filename}' contains {line_count} lines.")

if __name__ == "__main__":
    main()
