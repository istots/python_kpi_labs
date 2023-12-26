import math
from math import sqrt
try: 
    a = float(input('Введіть a: '))
    b = float(input('Введіть b: '))
    c = float(input('Введіть c: '))

    D = (b**2) - (4*a*c)
    if D > 0:
        print('x1 = ', round((-b + sqrt(D)) / (2*a),3))     
        print('x2 = ', round((-b - sqrt(D)) / (2*a),3))
    elif D == 0:
        print('x1 = x2 = ', round(((-b)//(2*a)),3))
    else:
        raise UserWarning('UserWarning', 'Дискримінант менше 0. Корені відсутні.')

except ZeroDivisionError as err:
    print(err.args[0], ': Введіть a != 0 !')
except OverflowError as err:
    print(err.args[0], ': Переповнення розрядної сітки!')
except ValueError:
    print('Введіть число!')
except UserWarning as err:
    print(err.args[0], ': ', err.args[1])
