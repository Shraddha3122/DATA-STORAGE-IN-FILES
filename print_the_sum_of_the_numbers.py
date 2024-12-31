# Read a list of numbers from a text file and print the sum of the numbers.


def read_numbers_from_file(filename):
    """Read numbers from a text file and return them as a list of floats."""
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to a float and add to the list
                numbers.append(float(line.strip()))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: One or more lines in the file could not be converted to a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return numbers

def main():
    filename = input("Enter the name of the text file containing numbers: ")
    numbers = read_numbers_from_file(filename)
    
    if numbers:
        total_sum = sum(numbers)
        print(f"The sum of the numbers in the file '{filename}' is: {total_sum}")

if __name__ == "__main__":
    main()