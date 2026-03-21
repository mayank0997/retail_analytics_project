import csv
import sys

def count_rows(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return sum(1 for _ in reader)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_rows.py <csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        row_count = count_rows(file_path)
        print(f"Total rows (excluding header): {row_count-1}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")