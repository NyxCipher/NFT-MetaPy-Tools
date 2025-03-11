import csv
import json
import pandas as pd
from pathlib import Path


class DataFabric:
    def __init__(self, source_csv: str):
        self.source_csv = Path(source_csv)
        self.data = None

    def load_csv(self):
        """Load data from CSV into DataFrame."""
        self.data = pd.read_csv(self.source_csv)
        return self.data

    def export_json(self, json_path: str, primary_key='ID'):
        """Export loaded data to JSON format using a specified primary key."""
        if self.data is None:
            raise ValueError("Data not loaded. Call load_csv first.")

        json_data = self.data.set_index(primary_key).to_dict(orient='index')

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=2)

    def reshape_json_metadata(self, input_json: str, output_json: str, image_base_url: str):
        """Reshape JSON to Ethereum NFT metadata standards."""
        with open(input_json, encoding='utf-8') as file:
            original_data = json.load(file)

        reshaped_data = []

        for key, value in original_data.items():
            properties = value.get('Properties', '').split(', ')

            attributes = [
                {"trait_type": "Rarity", "value": value.get('Rarity')},
                {"trait_type": "Faction", "value": value.get('Faction')},
                {"trait_type": "Class", "value": value.get('Class')},
                {"trait_type": "Type", "value": value.get('Type')},
                {"trait_type": "Specials", "value": value.get('Specials')}
            ]

            attributes += [
                {"trait_type": f"Attribute {idx+1}", "value": prop}
                for idx, prop in enumerate(properties)
            ]

            reshaped_data.append({
                "id": value.get('ID'),
                "name": f"Nexu5 Avatar: {value.get('ID')}",
                "description": "Nexu5 Avatar Series",
                "image": f"{image_base_url}/{key}.jpg",
                "attributes": attributes
            })

        with open(output_json, 'w', encoding='utf-8') as json_out:
            json.dump(reshaped_data, json_out, indent=2)

    def export_csv(self, json_path: str, csv_output: str):
        """Export reshaped JSON data back to CSV format."""
        with open(json_path, encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        df = pd.json_normalize(json_data, record_path=['attributes'],
                               meta=['id', 'name', 'description', 'image'],
                               errors='ignore')

        df.to_csv(csv_output, index=False)


# Example usage
if __name__ == "__main__":
    fabric = DataFabric('Nexu5GameData1.csv')

    # Step 1: Load CSV Data
    fabric.load_csv()

    # Step 2: Export Initial JSON
    fabric.export_json('Nexu5JSONGameData2022.json')

    # Step 3: Reshape JSON for NFT Metadata
    fabric.reshape_json_metadata(
        'Nexu5JSONGameData2022.json',
        'metadata.json',
        image_base_url='https://nexu5-avatars.s3.us-east-2.amazonaws.com'
    )

    # Step 4: Export Final JSON to CSV
    fabric.export_csv('metadata.json', 'reshaped_metadata.csv')
