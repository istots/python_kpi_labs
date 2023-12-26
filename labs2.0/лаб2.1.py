import math
print("Лабораторна робота 2. 9 варіант. Корсун Єлизавета, КМ-23")
print("Організація циклу за допомогою оператора for. Обчислити")
while True:
    while True:
        try:
            x=int(input())
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть значення Х!")
            continue
        else:
            break
        
    while True:
        try:
            n=int(input())
        except ValueError:
            print("Помилка! Спробуйте ще раз, введіть кількість ітерацій!")
            continue
        else:
            break
    c=1
    for i in range(n):
        c=c*(math.pow(x,i+1)+i+1)

    print(c)
    try_again = input("Введіть 1 - продовжити або будь-який інший символ - завершити: ") 
    if try_again == "1":
        continue
    else:
        exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break
