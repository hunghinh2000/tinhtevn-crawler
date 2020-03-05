import json

def write_json_file(json_name = 'data.json', json_folder_path = None, data = None):
    """Write a json file from a given data 
    
    Inputs:
        json_name: str
				Ouput json name
        json_folder_path: str
                The path of output json
		data: dict
				The data you need to write as json file.
    Return:
        None
    Author:
    Last modified: 11:23_02/28/20
    """

    full_path = json_folder_path + json_name
    with open(full_path, 'w') as outfile:
        json.dump(data, outfile)