import json

json_file_path = "/home/pi/final/stats.json"

with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

if contents['hunger'] >= 1:
        contents['hunger'] -= 1
else:
    contents['hunger'] = 0
    
if contents['thirst'] >= 1:
        contents['thirst'] -= 1
else:
    contents['thirst'] = 0


with open(json_file_path, "w") as jsonFile:
    json.dump(contents, jsonFile)

    
