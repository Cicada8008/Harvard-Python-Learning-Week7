import sys
import csv
from tabulate import tabulate

def load_csv(filename):
    try:
        print(f"Attempting to open {filename}...")
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
            print(f"CSV data loaded successfully. Found {len(rows)} rows.")
        return rows
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while loading file: {e}")
        sys.exit(1)
def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        print("Usage: python pizza.py <filename.csv>")
        sys.exit(1)

    filename = sys.argv[1]
    rows = load_csv(filename)
    if not rows:
        print(f"Error: The file '{filename}' is empty or improperly formatted.")
        sys.exit(1)

    print("Formatting table with tabulate...")

    table = tabulate(rows, headers="keys", tablefmt="grid")
    header_line, sep, *rest = table.splitlines()
    header_separator = sep.replace('-', '=')

    # Display the table with custom separator line
    print(f"{header_line}\n{header_separator}\n" + "\n".join(rest))

if __name__ == "__main__":
    main()
