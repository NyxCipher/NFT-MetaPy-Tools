# File Four
# Challenge: won't read integers
# Solutions: convert back to STR-Strings
#
import json
in_file_path='Generate.json' # Change me!

with open(in_file_path,'r') as in_json_file:

    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)

# output method
def output(xxx, yyy):
         with open(yyy, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`
            json.dump(xxx, out_json_file, indent=4)

    # convert & assign file names here
    #for x in range(0,8888):

# Start at Zero by Force
i=0
for json_obj in json_obj_list:
    filename= str(i) + ".json"
    # output(xxx = json_obj, yyy = filename)
    with open(filename, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`
            json.dump(json_obj, out_json_file, indent=4)
            print(filename)
            print(json_obj)
            i+=1
            

# a list to hold individually parsed JSON structures
# with open('test.json') as f:
# in_file_path='metadata.json' # Change me!
#
# with open(in_file_path,'r') as in_json_file:
#
#    # Read the file and convert it to a dictionary
#    json_obj_list = json.load(in_json_file)
#
#    for json_obj in json_obj_list:
#        filename=json_obj['Name']+'.json'
#
#        with open(filename, 'w') as out_json_file:
#            # Save each obj to their respective filepath
#            # with pretty formatting thanks to `indent=4`
#            json.dump(json_obj, out_json_file, indent=4)
        