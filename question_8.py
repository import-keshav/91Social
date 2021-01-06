''' 
    Python program to Generate random logs and write in a file,
'''

from pathlib import Path

def generate_random_logs_file():
    ''' 
        Generate random logs and write in a file , once the file size
        reaches 2Mb open new file and continue writing.
    '''

    counter = 1
    while True:

        filname = str(counter) + '_log.txt'

        print('File : ' + filname + ' created')

        file_obj = open(filname, 'a')
        while Path(filname).stat().st_size <= 2 * 1000000:
            file_obj.write('random')
        file_obj.close()

        counter += 1

        print('File : '+ filname + ' reached 2MB')


if __name__ == "__main__":
    generate_random_logs_file()
