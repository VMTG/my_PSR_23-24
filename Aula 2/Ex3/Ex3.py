#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

from math import sqrt

#define functions here...


def getDividers(value):
    """Gets a list of integer dividers of number value

    Args:
        value: number to get dividers.

    Returns:
        bool: is perfect (True) or not (False)
    """
    
    dividers = []

    limit = round((value/2)+1)

    for i in range (1,limit):
        if value%i==0:
            dividers.append(i)

    return dividers

def isPerfect(value):

    dividers = getDividers(value)

    return value == sum(dividers)


