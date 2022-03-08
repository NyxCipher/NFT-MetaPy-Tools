# File Three
# Challenge: Randomize Our Metadata
import json
import random
import numpy as np
import codecs, json
from ast import literal_eval

# File Handler Var
in_file_path='metadata.json' # Change me!

# JSON Loads File
with open(in_file_path,'r+') as in_json_file:
        data = json.load(in_json_file)
        arr=[]

        # Challenge: Our Data Is Formatted as STR-String
        # data['id'] = '1'
        # we need to order the data as INT-integers
        for d in data:
            d['id'] = literal_eval(d['id'])
            arr.append(d)
        print(arr)

        # use numpy as np
        x = np.array(arr)
        print(x)

        # random numpy shuffle
        #
        shuffled_indices = np.random.permutation(len(x)) #return a permutation of the indices
        print(f"shuffled indices: {shuffled_indices}")
        x = x[shuffled_indices]
        print(f"shuffled x  = {x}")
        #
        # use this block to add additional formatting
        # first change from 1-D array to 2-D or 3-D
        # Then Roll, ReShape, Flip etc.
        # (see: https://numpy.org/doc/stable/reference/routines.array-manipulation.html)
        #
        zone3 = x
        #
        # output generated random data
        # 
        c = zone3.tolist() # nested lists with same data, indices
        file_path = "Generate.json" ## your path variable
        json.dump(c, codecs.open(file_path, 'w', encoding='utf-8'), 
                separators=(',', ':'), 
                sort_keys=False, 
                indent=4) ### this saves the array in .json format
            