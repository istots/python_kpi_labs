import math
print("Лабораторна робота 1. 9 варіант. Корсун Єлизавета, КМ-23")
print("Обчислення конкретної функції, в залежності від введеного значення Х")
while True:
    try:
        x = float(input())
        z = float(0.0)
    except ValueError:
        print("Помилка! Спробуйте ще раз, введіть число!")
        continue
    else:
        if x >= 0 or x <= 1:
            z = math.sqrt(x) - x
        else:
            if x > 1 or x < 0:
                z = math.sqrt(x) - math.sin(math.pi*math.sqrt(x))
        print("The answer is")
        print(z)
        try_again = input("Введіть 1 - продовжити або будь-який інший символ - завершити: ") 
        if try_again == "1":
            continue
        else:
            exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break

