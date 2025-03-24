import csv

def filter_and_count(file_path):
    count = 0

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip the header if there is one
        next(csvreader, None)

        for row in csvreader:
            # Check if the 6th column value is "SDC"
            if row[5] == "SDC":
                # Check if the 2nd column value is a substring of the 5th column value
                if 'r'+str(row[1]) in row[4]:
                    count += 1
    
    return count

# Example usage
file_path = '_DS/registrs/ds_rijndeal_registers_1.csv'  # Replace with the path to your .csv file
result = filter_and_count(file_path)
print(f"Number of matching rows: {result}")