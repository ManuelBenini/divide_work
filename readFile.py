import json

f = open('db/connection.json')

data = json.load(f)

string = ''

for i in data:
    if list(data)[-1] != i:
        string += f"{i}='{data[i]}',"
    else:
        string += f"{i}='{data[i]}'"
        
print(string)