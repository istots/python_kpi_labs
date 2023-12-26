import random 
print("Лабораторна робота 3. 9 варіант. Корсун Єлизавета, КМ-23")
print("Структури даних: списки, кортежі, множини. Завдання 1")
while True:
    mas =[] 
    for i in range(101): mas.append(random.randint(0, 100)) 
    print('Список, заповнений випадковими числами: ', mas)
    while True:
        try:
            min = int(input('Введіть мінімум: ' ))
            if min <= 0:
                raise ValueError
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть значення мінімуму не менше 0!")
            continue
        else:
            break
    while True:
        try:
            max = int(input('Введіть максимум: ' )) 
            if max <= min:
                raise ValueError
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть максимум не не менше мінімума!")
            continue
        else:
            break
            
    mas2 = [i for i, ch in enumerate(mas) if (ch >= min and ch <= max)]
    print('Загальне число знайдених індексів: ', len(mas2))
    print('Всі індекси окремо: ', mas2)
    mas3 = [mas[ch] for ch in mas2]
    mas2.sort()
    mas2.reverse()
    for ch in mas2: mas.pop(ch) 
    print('Список після видалення елементів за певним індексом: ', mas)
    print('Список видалених елементів: ', mas3)
    
    try_again = input("Введіть 1 - почати знову або будь-який інший символ - завершити: ") 
    if try_again == "1":
        continue
    else:
        exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break