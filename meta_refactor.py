import json

# Utility function to safely get property values with default None
def get_property(properties, index):
    try:
        return properties[index]
    except IndexError:
        return None

# Read and process JSON data
with open('Nexu5JSONGAMEDATA2022_3.json') as json_file:
    data = json.load(json_file)

result = []

for i in range(1, 8889):
    key = str(i)
    properties = data[key]['Properties'].split(', ')

    attributes = [
        {"trait_type": "Rarity", "value": data[key]['Rarity']},
        {"trait_type": "Faction", "value": data[key]['Faction']},
        {"trait_type": "Class", "value": data[key]['Class']},
        {"trait_type": "Type", "value": data[key]['Type']},
        {"trait_type": "Type", "value": data[key]['Specials']}
    ]

    # Dynamically add property attributes
    for attr_num in range(14):
        prop_value = get_property(properties, attr_num)
        if prop_value:
            attributes.append({
                "trait_type": f"Attribute {attr_num + 1}",
                "value": prop_value
            })
        else:
            attributes.append({
                "trait_type": f"Attribute {attr_num + 1}",
                "value": "None"
            })

    result.append({
        "id": data[key]['ID'],
        "name": f"Nexu5 Avatar: {data[key]['ID']}",
        "description": "Nexu5 Avatar Series",
        "image": f"https://nexu5-avatars.s3.us-east-2.amazonaws.com/{key}.jpg",
        "attributes": attributes
    })

# Write the result to output file
with open('metadata.json', 'w') as outp:
    json.dump(result, outp, indent=4)

# Optional search functionality (if needed)
def check_if_exists(item, search_list, filename='search.json'):
    found = [str(item)] if item in search_list else []
    with open(filename, 'w') as srch:
        json.dump(found, srch)
