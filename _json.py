import json
data = {
    "math": 80, 
    "science":40,
    "computer":90
}
json_data = json.dumps(data)
print(json_data)