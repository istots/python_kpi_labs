import numpy as np
import itertools

while True:
    try: 
        dim = int(input('Enter the size of your matrix: '))
        if dim <= 0:
            raise ValueError
    except ValueError:
        print('Please, enter positive number!')  
        continue
    break    

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))

    print('Here is your matrix\n', matrix)

    return matrix

def creating_permutation_list():
    """
    The function creates a list of permutations.
    """
    num = list(range(dim))
    permutation_list = list(itertools.permutations(num, dim))
    return permutation_list

def calculation_of_products(m):
    """
    The function calculates products
    """
    #m = random_matrix(dim)
    permutation_list = creating_permutation_list()


    calculation_list = []
    for perm in permutation_list:

        inversionCount = 0
        for ii in range(dim - 1):
            for ij in range(ii + 1, dim):
                if perm[ii] > perm[ij]:
                    inversionCount = inversionCount + 1

        if (inversionCount % 2 != 0):
            sign = -1
        else:
            sign = 1

        p = 1
        for j in range(dim):
            p *= m[j,perm[j]]

        calculation_list.append(sign * p)
    return calculation_list

def total_amount(calculation):
    """
    The function calculates matrix definition
    """
    #calculation = calculation_of_products(random_matrix(dim))
    s=0
    for i in range(len(calculation)):
        s+=calculation[i]    

    print('Here is the determinant of your matrix: ', s)   
    
total_amount(calculation_of_products(random_matrix(dim)))