# Import the json module to work with JSON data
import json

# Define a dictionary with some data
data = {
    "math": 80,      # Score in Math
    "science": 40,   # Score in Science
    "computer": 90   # Score in Computer
}

# Convert the dictionary `data` to a JSON-formatted string
json_data = json.dumps(data)

# Print the JSON-formatted string
print(json_data)