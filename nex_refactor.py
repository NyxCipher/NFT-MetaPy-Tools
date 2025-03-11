import csv
import json

def csv_to_json(csv_path, json_path, primary_key='ID'):
    """
    Converts CSV file to JSON format.

    Args:
        csv_path (str): Path to input CSV file.
        json_path (str): Path to output JSON file.
        primary_key (str): Column name to be used as primary key.
    """
    with open(csv_path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = {row[primary_key]: row for row in reader}

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    # Paths to your CSV and JSON files
    csv_input = 'Nexu5GameData1.csv'
    json_output = 'Nexu5JSONGameData2022.json'

    csv_to_json(csv_input, json_output)
