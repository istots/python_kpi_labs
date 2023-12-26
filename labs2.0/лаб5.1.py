import math
print('Лабораторна робота 5. 9 варіант. Корсун Єлизавета, КМ-23')
print('Використання функцій. Завдання 1.\nМішень для стрільби являє собою концентричні кільця з центром на початку координат.\nРадіус внутрішнього кільця (“десятки”) — 1 см. Ширина всіх інших кілець — по 1 см.\nНаписати функцію, яка за координатами трьох точок попадання ху(х1,у1), ху(х2,у2) і ху(х3,у3) обчислює суму вибитих очок.')
while True:
    while True:
        try:
            x1 = float(input('Введіть координату попадання х1: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else: 
            break
    while True:
        try:
            x2 = float(input('Введіть координату попадання х2: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else:
            break
    while True:
        try:
            x3 = float(input('Введіть координату попадання х3: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else:
            break
    while True:
        try:
            y1 = float(input('Введіть координату попадання y1: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else:
            break
    while True:
        try:
            y2 = float(input('Введіть координату попадання y2: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else:
            break
    while True:
        try:
            y3 = float(input('Введіть координату попадання y3: '))
        except ValueError:
            print('Будь ласка, введіть дійсне число!')
            continue
        else:
            break

    def popadannya(x,y):
        z = math.sqrt(x**2 + y**2)
        if z <= 1:
            return 10
        elif 1 < z <= 2:
            return 9
        elif 2 < z <= 3:
            return 8
        elif 3 < z <= 4:
            return 7
        elif 4 < z <= 5:
            return 6
        elif 5 < z <= 6:
            return 5
        elif 6 < z <= 7:
            return 4
        elif 7 < z <= 8:
            return 3
        elif 8 < z <= 9:
            return 2
        elif 9 < z <= 10:
            return 1
        else:
            return 0
        
    def suma():
        return popadannya(x1,y1) + popadannya(x2, y2) + popadannya(x3, y3)

    print('Кількість набраних очок: ', suma())
    try_again = input("Введіть 1 - продовжити або будь-який інший символ - завершити: ") 
    if try_again == "1":
        continue
    else:
        exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break