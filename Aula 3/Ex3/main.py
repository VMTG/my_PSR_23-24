#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

from collections import namedtuple

ComplexNumber = namedtuple("ComplexNumber", ["real","imaginary"])

def addComplex(x, y):
    # add code here ...
    real_part = x.real + y.real
    imag_part = x.imaginary + y.imaginary
    return ComplexNumber(real_part, imag_part)

def multiplyComplex(x, y):
    # add code here ...
    real_part = (x.real * y.real) - (x.imaginary * y.imaginary)
    imag_part = (x.real * y.imaginary) + (x.imaginary * y.real)
    return ComplexNumber(real_part, imag_part)


def printComplex(x):
    # add code here ...
    print(f"{x.real} + {x.imaginary}i")


def main():

    # define two complex numbers as tuples of size two
    # Test add
    c1 = ComplexNumber(5, 3)
    c2 = ComplexNumber(-2, 7)
    print ('c1 = ' + str(c1))
    print ('c2 = ' + str(c2))
    soma_complexos = addComplex(c1, c2)
    print ('Soma =')
    printComplex(soma_complexos)
 

    # test multiply
    print ('Multiplicação =')
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()