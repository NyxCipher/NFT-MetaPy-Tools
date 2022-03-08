# File Two
# Python program to demonstrate
# Conversion of JSON data to Dictionary
# 

# importing the module
import json


parser = json.JSONDecoder()
parsed = [] 

# Used Later
def check_if_exists(x, ls):
    arr = []
    with open('search.json', 'w') as srch:
        if x in ls:
            print(str(x) + str(ls))
            arr.append(str(x))
        else:
            print('none')
        data=json.dumps(arr)
        srch.write(data)
       

# Opening JSON file
# Opening Output File as 'outp'
with open('Nexu5JSONGAMEDATA2022_3.json') as json_file, open('metadata.json', 'w') as outp, open('search.json', 'w') as srch:

    # Json.Load our Data from CSV to JSON from Nex.Py
    data = json.load(json_file)

    # Arrays
    result = []

    # May Need/Want To Clone (Not In Our Case)
    # meta = []
    # array = {}

    # for loop over our Avatar NFT Max Count
    # Keep in mind that count starts at 0
    for i in range(1,8889):

        # Check Me
        count = i -1
        
        # Format the Object
        # Notice, our data was: '1' not 1
        # We had to read strings
        x = f'{i}'
        
        # Print & Confirm We Have Our Desired Output
        print(x)

        # In our dataset:
        # Properties: data[ID][Properties]['one, two, three, four']
        # Challenge: We had a nested array we needed to parse over
        # Goal: [Properties]['one', 'two', 'three', 'four']
        # Final Goal: Metadata Format...
        #
        # Print So We Can See Deep         
        print(data[x]['Properties'])

        # Print Properties: and split at 'commas, '
        print(data[x]['Properties'].split(', '))

        # Do Work
        Properties = data[x]['Properties'].split(', ')

        # use List.append
        # notice the "attributes" object
        # this is ETH-NFT MetaData Format
        # First block of code runs smooth
        # this is our outer array nested 
        # only in an ['ID']
        result.append({
                "id":data[x]['ID'],
                "name":"Nexu5 Avatar: " + data[x]['ID'],
                "description": "Nexu5 Avatar Series",
                "image": "https://nexu5-avatars.s3.us-east-2.amazonaws.com/"+x+".jpg",
                "attributes":[{"trait_type":"Rarity", "value":data[x]['Rarity']},
                {"trait_type":"Faction", "value":data[x]['Faction']},
                {"trait_type":"Class", "value":data[x]['Class']},
                {"trait_type":"Type", "value":data[x]['Type']},
                {"trait_type":"Type", "value":data[x]['Specials']}]
                })
        
        # output from result array 
        # nested attributes
        print(result[0]['attributes'])

        # set to a variable
        attributes = result[0]['attributes']
        
        # May want to copy() here
        #
        # meta = result.attributes.copy() 
        # print(meta)

        # Formatting the data
        # use this seperate section for testing
        #
        # newTraits = {"Attributes": [{ "trait_type":"Attribute 1", "value":Properties[0] }]}
        # result.append(newTraits)
        # print(result)

        # It looked muched simpiler at the start
        # Task: Iterate over 8,888 array objects nested with 1 - 14 traits
        # Tricks: We had i start at 1, so we need count to start at 0 since the keys start at 0
        # Challenge 1: Append Result[arr] with MetaData Formatted Properties
        # Challenge 2: Find a way to loop over the nested array[obj]
        # Challenge 3: Handle: 'index out of bounds' as some elemnts have 14 while others 7
        # Challenge 4: Print and Assign 'None' when 'index out of bounds'
        #
        #for i in range(14):
        #    while True:
        #        try:
        #            matches = []
        #            ls = Properties[i]
        #            count = ls.index("Metalplate")
        #            raise Exception(result[count]["attributes"].append({ 
        #            "trait_type":"Attribute 1", "value":Properties[0]
        #            
        #            break
        #        except Exception as inst:
        #            break
        #        else:
        #            print('err')
        #            break
    if False:
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 1", "value":Properties[0]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 1", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 2", "value":Properties[1]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 2", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 3", "value":Properties[2]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 3", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 4", "value":Properties[3]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 4", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 5", "value":Properties[4]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 5", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 6", "value":Properties[5]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 6", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 7", "value":Properties[6]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 7", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 8", "value":Properties[7]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 8", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 9", "value":Properties[8]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 9", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 10", "value":Properties[9]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 10", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 11", "value":Properties[10]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 11", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 12", "value":Properties[11]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 12", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 13", "value":Properties[12]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 13", "value":"None"
                })
        while True:
            try:
                raise Exception(result[count]["attributes"].append({ 
                    "trait_type":"Attribute 14", "value":Properties[13]
                }, ))
                # print(result)
                break
            except Exception as inst:
                # print(inst)
                break
            else:
                result.append({ 
                    "trait_type":"Attribute 14", "value":"None"
                })

        # Check Me Against Data
        # For Accuracy
        # count+1
                
        # Beginning Code For Referance
        # this is how we started
        # however, this is not MetaData Format
        # nor will this handle 8,888
        # 1 will run, error at 'index out of bounds'
        #
        # "Attribute 1":Properties[0]
        # "Attribute 2":Properties[1]
        # "Attribute 3":Properties[2]
        # "Attribute 4":Properties[3]
        # "Attribute 5":Properties[4]
        # "Attribute 6":Properties[5]
        # "Attribute 7":Properties[6]
        # "Attribute 8":Properties[7]
        # "Attribute 9":Properties[8]
        # "Attribute 10":Properties[9]
        # "Attribute 11":Properties[10]
        # "Attribute 12":Properties[11]
        # "Attribute 13":Properties[12]
        # "Attribute 14":Properties[13]
        
        # Trim Data if Needed
        # We needed to remove a few elements
        for element in result:
            element.pop('Nexu5', None)

    # output data & print to file
    data=json.dumps(result)
    # print(data)
    outp.write(data)
        
# for printing the key-value pair of
# nested dictionary for loop can be used
# print("\nPrinting nested dictionary as a key-value pair\n")
# for i in data['1']:
#    print("Properties:", i['Properties'])
#    print()

# If Needed To Restructure Json Data
# Use Following Code
#
#    data = json_file.read()
#    head = 0  # hold the current position as we parse
#    while True:
#        head = (data.find('{', head) + 1 or data.find('[', head) + 1) - 1
#        try:
#            struct, head = parser.raw_decode(data, head)
#            parsed.append(struct)
#        except (ValueError, json.JSONDecodeError):  # no more valid JSON structures
#          break
#
#    print(json.dumps(parsed, indent=2))

# The Concept
# for reading nested data [0] represents
# the index value of the list
# with open('Nexu5JSONGAMEDATA2022_2.json') as inp, open('test.json', 'w') as outp:
#    json_decode=json.load(inp)    
#    result = []
#    for data in json_decode:
#        Properties = data[1].split(",")
#        result.append({
#            "Properties":data[1],
#            "min":Properties[0],
#            "max":Properties[1]
#        })    
#    data=json.dumps(result)
#    outp.write(data)
#

# List Methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
