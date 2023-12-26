import math

def area_calculation(a,b,c):
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    p = (a+b+c)/2
    area = math.sqrt((p-a)*(p-b)*(p-c))
    return area

#print(area_calculation(0,0,0))

def check(a,b,c):
    while True:
        try:
            if a <= 0:
                raise ValueError
            if b <= 0:
                raise ValueError
            if c <= 0:
                raise ValueError
        except ValueError:
            print('Введіть додатнє число')
        break
    return True

print(check(area_calculation(0,0,0)))