''' 
    Python program that takes a text file as input and
    returns the number of words of a given text file.
'''

def get_number_of_words_in_file(filename):
    ''' Read file by line by line and stores each line in a list.

    Args:
        filename str: name of the file.

    Retruns:
        num_of_words int: Returns the number of words in a file.
    '''

    num_of_words = 0
    file_obj = open(filename, 'r')

    for line in file_obj.readlines():
        line = line.split('\n')
        if line and line[0]:
            line[0].replace(",", " ")
            num_of_words += len(line[0].split(' '))

    return num_of_words


if __name__ == "__main__":
    print("Enter Filename : ")
    FILENAME = input()
    print(get_number_of_words_in_file(FILENAME))
