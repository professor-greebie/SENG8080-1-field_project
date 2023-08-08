def file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read lines as a list
            return "".join(lines)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

# Replace 'file_path' with the actual path to your file
file_path = 'gnome.fa'
characters_list = file_to_list(file_path)
# print(characters_list)

import csv

# Read the input CSV file, extract substrings, and create a new list of rows
input_csv_path = 'Genome1.csv'
output_csv_path = 'Genome2.csv'
output_rows = []

with open(input_csv_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Read header row
    headers.append('Genome String')  # Add 'Genome String' column header
    output_rows.append(headers)  # Add modified header row to output_rows list

    for row in reader:
        start = int(row[3])  # Assuming start value is in the first column (index 0)
        end = int(row[4])    # Assuming end value is in the second column (index 1)
        genome = characters_list[start:end]
        output_row = row + [genome]  # Create a new row with extracted substring
        output_rows.append(output_row)  # Add updated row to output_rows list

# Write the updated data back to the output CSV file
with open(output_csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(output_rows)

print("Extraction and writing completed.")
