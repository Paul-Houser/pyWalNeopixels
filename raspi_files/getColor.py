# Author: Paul Houser
# Date: 10/01/2019
# This code returns the hex code for the color name 'colorX' where X is 0-15, from the colors.json
# file generated by pywal.

import json

def get_hex_code(colorName, directory):
    with open(directory) as json_file:
        colors = json.load(json_file)["colors"]
        hexString = colors[colorName]
        return hexString
