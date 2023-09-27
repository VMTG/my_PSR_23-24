#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


from colorama import Fore, Back, Style
from Ex2 import isPerfect

#define functions here...

maximum_number = 500

def main():
    print("Starting to compute perfect numbers up to" + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is Perfect.')


    if __name__ == "__main__":
        main()