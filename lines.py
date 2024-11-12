import sys
def lineeee(filename):
    try:
        with open(filename) as file:
            return sum(
                1 for line in file
                if line.strip() and not line.lstrip().startswith("#"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)



def main():
    # Check for exactly one command-line argument that ends with .py
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        print("Usage: python lines.py <filename.py>")
        sys.exit(1)


    print(lineeee(sys.argv[1]))
if __name__ == "__main__":

    main()
