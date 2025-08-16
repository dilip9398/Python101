import json

new_data = {
    "Amazon":{
        "Email":"kancherladilip",
        "password" : "dsfhsuhf",
    }
}



with open("data.json", "r") as data:
    h = json.load(data)

with open("data.json" ,"w") as data:
    json.dump(new_data, data, indent=4)

h.json.update(new_data)
