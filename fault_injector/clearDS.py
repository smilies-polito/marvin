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

def process_csv(input_file, output_file):
    # Read the input CSV file
    data = read_csv_file(input_file)

    # Separate header from the data
    header = data[0]
    data = data[1:]

    # Filter out rows where the sixth column has the value "crash/hangs"
    filtered_data = [row for row in data if row[5] != "crash/hangs"]

    # Replace "SDC" with 1 and "benign" with 0 in all columns
    for row in filtered_data:
        for i in range(len(row)):
            if row[i] == "SDC":
                row[i] = 1
            elif row[i] == "benign":
                row[i] = 0

    # Remove the first five columns from each row
    processed_data = [row[5:] for row in filtered_data]

    # Remove the header (not needed as per the requirement)
    # No action required because the header was already separated

    # Write the processed data to the output CSV file
    write_csv_file(output_file, processed_data)

# Usage example
input_csv_file = 'ds_sha_registers_1.csv'
output_csv_file = 'ds_sha_registers_1_processed.csv'
process_csv(input_csv_file, output_csv_file)