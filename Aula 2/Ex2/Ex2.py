#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


from colorama import Fore, Back, Style

#define functions here...


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


