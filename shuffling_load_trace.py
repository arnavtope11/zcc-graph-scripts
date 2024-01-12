import random
import random
import sys


def shuffle_lines(ip_filename, op_filename):
    # Read the file into an array
    lines = []
    with open(ip_filename, 'r') as file:
        lines = file.readlines()

    # Shuffle the lines randomly
    random.shuffle(lines)

    # Write the shuffled lines to another file
    with open(op_filename, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python shuffling_load_trace.py <input_filename> <output_filename>")
    else:
        ip_filename = sys.argv[1]
        op_filename = sys.argv[2]
        shuffle_lines(ip_filename, op_filename)
