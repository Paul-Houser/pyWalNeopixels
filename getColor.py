import json

def get_hex_code(colorName, directory):
    with open(directory) as json_file:
        colors = json.load(json_file)["colors"]
        hexString = colors[colorName]
        return hexString
