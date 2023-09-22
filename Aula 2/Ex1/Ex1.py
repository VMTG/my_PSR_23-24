#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#define functions here....

from colorama import Fore, Back, Style

maximum_number = 500

def getDividers(value):
    """Gets a list of integer dividers of number value

    Args:
        value: number to get dividers.

    Returns:
        bool: is perfect (True) or not (False)
    """
    
    dividers = []

    for i in range (1,value):
        if value%i==0:
            dividers.append(i)

    return dividers

def isPerfect(value):

    dividers = getDividers(value)

    return value == sum(dividers)


def main():
    print("Starting to compute perfect numbers up to" + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is Perfect.')


    if __name__ == "__main__":
        main()