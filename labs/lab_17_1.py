def f1(n):
    while True:
        try:
            n = int(input('Введіть натуральне число: '))
            if n <= 0:
                raise ValueError
        except ValueError:
            print('Помилка! Введіть натуральне число!')
            continue
        break
    f = 1
    while n != 1:
        f = f * n
        n -= 1
    return f

def exp2(n):
    n = float(input('Enter any number: '))
    f = n*n
    return f

def exp3(n):
    n = float(input('Enter any number: ')) 
    f = n*n*n
    return f

import math

def root2(n):
    while True:
        try:
            n = int(input('Enter a positive integer: '))
            if n < 0:
                raise ValueError
        except ValueError:
            print('Error! Please, enter a positive integer!')
            continue
        break
    f = n**(1./2)
    return f
def root3(n):
    n = float(input('Enter any number: '))
    f = n**(1./3)
    return f



def log(b):
    a = math.e
    while True:
        try:
            b = int(input('Enter a positive number: '))
            if b < 0:
                raise ValueError
        except ValueError:
            print('Error! Please, enter a number more than 1!')
            continue
        break
    f = math.log(b, a)
    return f

print(log(0))