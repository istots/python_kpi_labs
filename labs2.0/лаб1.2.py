print("Лабораторна робота 1. 9 варіант. Корсун Єлизавета, КМ-23")
print("Підрахувати кількість цілих серед чисел а, b, с (ввести з клавіатури).")
while True:
    c = 0
    while True:
        try:
            x = float(input())
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть перше число!")
            continue
        else:
            if int(x) == x:
                c = c+1
            break
        
    while True:
        try:
            y = float(input())
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть друге число!")
            continue
        else:
            if int(y) == y:
                c = c+1
            break

    while True:
        try:
            z = float(input())
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть третє число!")
            continue
        else:
            if int(z) == z:
                c = c+1
            break

    print('Кількість цілих чисел:')
    print(c)
    try_again = input("Введіть 1 - продовжити або будь-який інший символ - завершити: ") 
    if try_again == "1":
        continue
    else:
        exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break
