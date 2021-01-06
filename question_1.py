''' Python program to read a file line by line and store it into a list. '''

def get_file_lines(filename):
    ''' Read file by line by line and stores each line in a list.

    Args:
        filename str: name of the file.

    Retruns:
        out list: Returns the each line of a file in a list.
    '''
    out = []
    file_obj = open(filename, 'r')

    for line in file_obj.readlines():
        line = line.split('\n')
        if line:
            line = line[0]
            out.append(line)
    
    file_obj.close()
    return out


if __name__ == "__main__":
    print("Enter Filename : ")
    FILENAME = input()
    print(get_file_lines(FILENAME))
