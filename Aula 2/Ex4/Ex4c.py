#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------

import argparse

import readchar

# Use imports here
from colorama import Fore, Back, Style

# Define functions here ...

# maximum_number = 30

def countNumbersUpTo(stop_char):

    # Passo 1: ler um carater do terminal -> readchar 
    print('Start typing')
    keys=[]
    while True:
        key = readchar.readkey()
        keys.append(key)
        print('User pressed ' + key)

        if key == stop_char:
            break

    print(keys)

    n_numeric = 0
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
    print('You pressed on ' + str(n_numeric) + ' numeric keys')

#ex5b
numerical_keys = []
for key in keys:
    if key.isnumeric():
        numerical_keys.append(key)

print ('Numerical keys' + str(numerical_keys))

#ex5c

d_keys = {}
i = 0
for key_idx, key in enumerate(keys):
    d_keys[key_idx] = key

print('d_keys = ' + str(d_keys))

#ex5d

numerical_keys.sort()
print('NUmerical keys' + str(numerical_keys))

#ex5e

numerical_keys2 = [x for x in keys if x.isnumeric()]

d_keys2 = {idx:x for idx,x in enumerate(keys)}

print('Numerical keys2' + str(numerical_keys2))
print('d_keys2' + str(numerical_keys2))


def main():

    countNumbersUpTo('x')


if __name__ == "__main__":
    main()