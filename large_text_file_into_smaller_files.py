# Write a program to split a large text file into smaller files, each containing a specified number of lines.


def split_file(input_file, lines_per_file):
    """Split a large text file into smaller files with a specified number of lines."""
    try:
        with open(input_file, 'r') as file:
            file_count = 0
            current_lines = []
            
            for line in file:
                current_lines.append(line)
                
                # When we reach the specified number of lines, write to a new file
                if len(current_lines) == lines_per_file:
                    output_file = f"{input_file}_part{file_count + 1}.txt"
                    with open(output_file, 'w') as output:
                        output.writelines(current_lines)
                    print(f"Created: {output_file}")
                    file_count += 1
                    current_lines = []  # Reset for the next file
            
            # Write any remaining lines to a new file
            if current_lines:
                output_file = f"{input_file}_part{file_count + 1}.txt"
                with open(output_file, 'w') as output:
                    output.writelines(current_lines)
                print(f"Created: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_file = input("Enter the name of the large text file to split: ")
    lines_per_file = int(input("Enter the number of lines per smaller file: "))
    
    split_file(input_file, lines_per_file)

if __name__ == "__main__":
    main()