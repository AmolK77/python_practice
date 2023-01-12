import json


data={'name':'vikram','place':'pune','profession':'driver'}


#writing  json file
json_data=json.dumps(data,indent=4)

#writting json data to file
with open('file.json',"w") as file:
    file.write(json_data)
    file.close()



#opening json file
with open('file.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))


