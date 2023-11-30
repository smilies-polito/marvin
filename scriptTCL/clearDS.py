import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def extract_changed_columns(input_file, output_file):
    # Read the input CSV file
    data = read_csv_file(input_file)

    # Separate header from the data
    header = data[0]
    data = data[1:]

    # Transpose the data to work with columns instead of rows
    transposed_data = list(map(list, zip(*data)))

    # Find the columns where all values change at least once, excluding cells with value '-'
    changed_columns = [column for column in transposed_data if len(set(column) - {'-'}) > 1]

    # Transpose the changed columns back to rows
    output_data = list(map(list, zip(*changed_columns)))

    # Prepare a mapping of the original column indices to the new indices in the output
    column_mapping = [i for i, column in enumerate(transposed_data) if column in changed_columns]

    # Remove the columns from the header that do not meet the criteria
    updated_header = [header[i] for i in column_mapping]

    # Add the header back to the output data
    output_data.insert(0, updated_header)

    # Write the output CSV file
    write_csv_file(output_file, output_data)

# Usage example
input_csv_file = 'dataset.csv'
output_csv_file = 'dataset_filtered.csv'
extract_changed_columns(input_csv_file, output_csv_file)
