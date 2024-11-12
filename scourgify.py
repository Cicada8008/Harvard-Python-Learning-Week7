import sys

import csv



def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input.csv output.csv")

        sys.exit(1)
    input_filename = sys.argv[1]

    output_filename = sys.argv[2]

    try:
        with open(input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            rows = []


            for row in reader:
                last, first = row["name"].split(", ")

                # Create a new dictionary with first, last, and house

                rows.append({"first": first, "last": last, "house": row["house"]})



        # Open the output file and write data

        with open(output_filename, "w", newline="") as output_file:

            fieldnames = ["first", "last", "house"]

            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)



    except FileNotFoundError:

        print(f"Error: The file '{input_filename}' does not exist.")

        sys.exit(1)



if __name__ == "__main__":

    main()
