'''
    Python program to convert an array to an array of
    machine values and return the bytes representation.
'''

import array
import binascii


def get_bytes_representation_of_array(input_list):
    ''' Converts a pytho list to an python array of machine values.

    Args:
        input_list list: Input list.

    Returns:
        bytes representation of array.
    '''
    python_array = array.array('i', input_list)
    bytes_array = python_array.tobytes()
    return  binascii.hexlify(bytes_array)


if __name__ == "__main__":
    print("Enter the length of array \n")
    LENGTH_OF_ARRAY = int(input())
    INPUT_ARRAY = []

    while len(INPUT_ARRAY) < LENGTH_OF_ARRAY:
        INPUT_NUMBER = input()
        try:
            INPUT_NUMBER = int(INPUT_NUMBER)
            INPUT_ARRAY.append(INPUT_NUMBER)
        except ValueError:
            print('Enter a valid key\n')

    print('Array of bytes is ')
    print(get_bytes_representation_of_array(INPUT_ARRAY))
