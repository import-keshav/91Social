'''
    Python program to convert the Python dictionary object
    (sort by key) to JSON data.
'''

import ast
import json

def convert_dict_to_json(dictionary):
    """ Convert the dictionary object (sort by key) to JSON data.

    Args:
        dictionary dict: Dictionary object.

    Returns:
        str: Desired json.
    """
    return json.dumps(dictionary, sort_keys=True, indent=4)


if __name__ == "__main__":
    print("Enter string dictionary i.e dictionary in string format: ")

    DICTIONARY = ast.literal_eval(input())

    print(convert_dict_to_json(DICTIONARY))
