# Create a program to write an array of integers to a binary file. Later, read the binary file and calculate the sum of all integers.

import struct

def write_integers_to_binary_file(filename, integers):
    """Write an array of integers to a binary file."""
    with open(filename, 'wb') as f:
        # Use struct to pack integers as binary data
        for integer in integers:
            f.write(struct.pack('i', integer))  # 'i' is the format for integers

def read_integers_from_binary_file(filename):
    """Read integers from a binary file and return them as a list."""
    integers = []
    with open(filename, 'rb') as f:
        while True:
            byte = f.read(4)  # Read 4 bytes for an integer
            if not byte:
                break
            integers.append(struct.unpack('i', byte)[0])  # Unpack the integer
    return integers

def calculate_sum_of_integers(integers):
    """Calculate the sum of a list of integers."""
    return sum(integers)

def main():
    # Example array of integers
    integers = [1, 2, 3, 4, 5, 100, -50, 42]
    binary_file = 'integers.bin'

    # Write integers to binary file
    write_integers_to_binary_file(binary_file, integers)
    print(f"Written integers to {binary_file}.")

    # Read integers from binary file
    read_integers = read_integers_from_binary_file(binary_file)
    print(f"Read integers: {read_integers}")

    # Calculate the sum of the integers
    total_sum = calculate_sum_of_integers(read_integers)
    print(f"The sum of the integers is: {total_sum}")

if __name__ == "__main__":
    main()