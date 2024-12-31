# Write a script that reads all files in a directory and identifies duplicate files based on content. Save a list of duplicate files to a text file.

# Importing Libraries 
import os 
import sys 
from pathlib import Path 
import hashlib 


def FindDuplicate(SupFolder): 
	
	# Duplic is in format {hash:[names]} 
	Duplic = {} 
	for file_name in files: 
		
		# Path to the file 
		path = os.path.join(folders, file_name) 
		
		# Calculate hash 
		file_hash = Hash_File(path) 
		
		# Add or append the file path to Duplic 
		if file_hash in Duplic: 
			Duplic[file_hash].append(file_name) 
		else: 
			Duplic[file_hash] = [file_name] 
	return Duplic 

# Joins dictionaries 
def Join_Dictionary(dict_1, dict_2): 
	for key in dict_2.keys(): 
		
		# Checks for existing key 
		if key in dict_1: 
			
			# If present Append 
			dict_1[key] = dict_1[key] + dict_2[key] 
		else: 
			
			# Otherwise Stores 
			dict_1[key] = dict_2[key] 


import os
import hashlib

def hash_file(file_path):
    """Generate a hash for the file at the given path."""
    hasher = hashlib.md5()  # You can use other hash functions like sha256
    with open(file_path, 'rb') as f:
        # Read the file in chunks to avoid using too much memory
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """Find duplicate files in the given directory."""
    file_hashes = {}
    duplicates = []

    # Walk through the directory
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_hash = hash_file(file_path)
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                else:
                    file_hashes[file_hash] = file_path
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    return duplicates

def save_duplicates_to_file(duplicates, output_file):
    """Save the list of duplicate files to a text file."""
    with open(output_file, 'w') as f:
        for original, duplicate in duplicates:
            f.write(f"Original: {original}\nDuplicate: {duplicate}\n\n")

def main():
    directory = input("Enter the directory to scan for duplicates: ")
    output_file = "duplicates.txt"

    duplicates = find_duplicate_files(directory)
    if duplicates:
        save_duplicates_to_file(duplicates, output_file)
        print(f"Duplicate files have been saved to {output_file}.")
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()