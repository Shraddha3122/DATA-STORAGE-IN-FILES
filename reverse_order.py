# Write a Python program that reads a text file containing a list of names and
# writes them to another file in reverse order.

def reverse_names(input_file, output_file):
    try:
        # Read names from the input file
        with open(input_file, 'r') as infile:
            names = infile.readlines()
        
        # Remove any trailing newline characters and reverse the list
        names = [name.strip() for name in names]
        names.reverse()
        
        # Write the reversed names to the output file
        with open(output_file, 'w') as outfile:
            for name in names:
                outfile.write(name + '\n')
        
        print(f"Reversed names have been written to {output_file}.")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'names.txt'  # Input file containing the list of names
output_file = 'reversed_names.txt'  # Output file for reversed names
reverse_names(input_file, output_file)