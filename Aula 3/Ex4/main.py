#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

from collections import namedtuple

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


    def add(self, y):
        # add code here ...
        real_part = self.real + y.real
        imag_part = self.imaginary + y.imaginary
        return ComplexNumber(real_part, imag_part)

    def multiply(self, y):
        # add code here ...
        real_part = (self.real * y.real) - (self.imaginary * y.imaginary)
        imag_part = (self.real * y.imaginary) + (self.imaginary * y.real)
        return ComplexNumber(real_part, imag_part)


    def __str__(self):
        # add code here ...
        return f"{self.real} + {self.imaginary}i"



def main():

    # define two complex numbers as tuples of size two
    # Test add
    c1 = ComplexNumber(5, 3)
    c2 = ComplexNumber(-2, 7)
    print ('c1 = ' + str(c1))
    print ('c2 = ' + str(c2))
    soma_complexos = c1.add(c2)
    print ('Soma =')
    print(soma_complexos)
 

    # test multiply
    print ('Multiplicação =')
    print(c1.multiply(c2))

if __name__ == '__main__':
    main()