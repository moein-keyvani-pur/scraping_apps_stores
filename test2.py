# Load the list from the JSON file
import json


with open("cafebazaar/data/cafebazaar_apps.json", "r") as file:
    loaded_data = json.load(file)

print(len(loaded_data))


import csv

# Define the CSV file path
csv_file_path = "cafebazaar_apps.csv"

# Write the JSON data to a CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    # Create a CSV writer
    writer = csv.DictWriter(file, fieldnames=loaded_data[0].keys())
    
    # Write the header row
    writer.writeheader()
    
    # Write the data rows
    writer.writerows(loaded_data)

print(f"Data has been saved to {csv_file_path}")

