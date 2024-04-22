# import OS module
import os
import json
# Get the list of all files and directories
def getDict():
    path = '/Users/wanbo/Desktop/Pathway genes'
    dir_list = os.listdir(path)

    composite = dict()
    for filename in dir_list:
        if filename != '.DS_Store':
            with open(os.path.join(path, filename), 'rb') as f:
                json_data = f.read().decode('utf-8', 'ignore') 
            
            # print('file', filename + '\n', json_data)
            
            data = json.loads(json_data)
            for key in data:
                composite[key] = data[key]["geneSymbols"]
    return composite



  