# File One
# Use to Convert CSV To JSON
# Challenge: Begin With An Excel Table of MetaData Traits
# Challenge Goal: Export It To Ethereum NFT MetaData Standard ( ie: 1.json )
#
import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['ID']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=2))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'Nexu5GameData1.csv'
jsonFilePath = r'Nexu5JSONGameData2022.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
