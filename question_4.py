''' Python program to sort a list of dictionaries using Lambda. '''

import ast

def sort_list_of_dictionaries(list_dict):
    """ Convert the dictionary object (sort by key) to JSON data.

    Args:
        list_dict list: Input list which needs to be sorted.

    Returns:
        list: List in sorted order.
    """
    return sorted(list_dict, key=lambda dictionary: dictionary['color'])


if __name__ == "__main__":
    print("Enter List of Dictionaries ")
    print("Enter Length of List ")

    NUM_OF_DICTS = int(input())
    INPUT_LIST = []

    for i in range(NUM_OF_DICTS):
        print("Enter string dictionary i.e dictionary in string format: ")
        INPUT_LIST.append(ast.literal_eval(input()))

    print(sort_list_of_dictionaries(INPUT_LIST))
