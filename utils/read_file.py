import json

def dict_read(file_path):
    data=[]
    file = open(file_path,'r')
    json_file = json.load(file)
    for item in json_file:
        data.append(tuple(item.values()))
    return data
