#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


def addComplex(x, y):
    # add code here ...
    real_part = x[0] + y[0]
    imag_part = x[1] + y[1]
    return (real_part, imag_part)

def multiplyComplex(x, y):
    # add code here ...
    real_part = (x[0] * y[0]) - (x[1] * y[1])
    imag_part = (x[0] * y[1]) + (x[1] * y[0])
    return (real_part, imag_part)


def printComplex(x):
    # add code here ...
    print(f"{x[0]} + {x[1]}i")


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    print ('Primeiro número complexo: ' + str(c1[0]) +' + '+ str(c1[1]) +'i')
    print ('Segundo número complexo: ' + str(c2[0]) +' + '+ str(c2[1]) +'i')

    # Test add
    c3 = addComplex(c1, c2)
    print ('Soma =')
    printComplex(c3)
 

    # test multiply
    print ('Multiplicação =')
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()
