import csv
import sqlite3
from datetime import datetime

# Define a mapping for non-standard timezones
timezone_mappings = {
    'IST': '+0530',
}

# Step 1: Connect to (or create) the SQLite3 database
conn = sqlite3.connect('../transactions.sqlite3')  # or ':memory:' for an in-memory database
cursor = conn.cursor()

# Step 2: Create the table
# Make sure the table schema matches the structure of the CSV file.
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions_transaction (
    user_id INTEGER,
    transaction_id INTEGER,
    transaction_time TEXT,
    item_code TEXT,
    item_description TEXT,
    quantity_items INTEGER,
    item_cost REAL,
    country TEXT
)
''')

# Step 3: Read CSV data
csv_file_path = 'transaction_data.csv'  # Update with your CSV file path

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row if your CSV has headers
    next(csv_reader)

    # Step 4: Insert the data row by row
    for row in csv_reader:
        # Extract the transaction_time and handle timezone parsing
        transaction_time_str = row[2]  # Assuming transaction_time is the third column
        split_date_str = transaction_time_str.split()

        # Get the timezone from the last part of the date string
        timezone = split_date_str[-2]
        if timezone in timezone_mappings:
            # Replace timezone with the offset
            date_str_with_offset = transaction_time_str.replace(timezone, timezone_mappings[timezone])
        else:
            date_str_with_offset = transaction_time_str

        # Parse the datetime string with the offset
        try:
            parsed_date = datetime.strptime(date_str_with_offset, "%a %b %d %H:%M:%S %z %Y")
            # Format to the desired output
            formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            formatted_date = None  # Handle parsing errors as needed

        # Prepare the row data with the formatted date
        new_row = row[:2] + [formatted_date] + row[3:]  # Replace transaction_time with formatted_date

        # Insert the processed row into the database
        cursor.execute('''
        INSERT INTO transactions_transaction (user_id, transaction_id, transaction_time, item_code, item_description, quantity_items, item_cost, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', new_row)

# Step 5: Commit the transaction and close the connection
conn.commit()
conn.close()

print("CSV data imported successfully into SQLite3.")