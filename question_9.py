'''
    Python program to ping and check whether any given IPs are active.
'''

from shutil import which
import subprocess


def ping_address():
    '''
        PING the particular address.
    '''
    print("Enter Address to PING : \n")

    address = input()
    print()
    res = subprocess.call(['ping', '-c', '3', address])

    if res == 0:
        print("ping to " + address +" OK\n")
    elif res == 2:
        print("no response from " + address + '\n')
    else:
        print("ping to " + address, " failed!\n")


def is_software_exist():
    '''
        Check whether the particular software exists or not.
    '''
    print("Enter software to check in system : ")
    software_name = input()
    print()
    if which(software_name) is not None:
        print('Yes ' + software_name + ' is installed\n')
    else:
        print('NO ' + software_name + ' is installed\n')


if __name__ == "__main__":
    while 1:
        print('Enter 1 to PING Address : \n')
        print('Enter 2 to check software installation : \n')
        print('Enter 3 for exit : \n')
        try:
            INPUT_KEY = int(input())
            print()
        except ValueError:
            print('Enter a valid key\n')

        if INPUT_KEY == 1:
            ping_address()
        elif INPUT_KEY == 2:
            is_software_exist()
        else:
            break
