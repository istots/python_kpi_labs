print("Лабораторна робота 2. 9 варіант. Корсун Єлизавета, КМ-23")
print("Написати програму, в результаті виконання якої з’ясується, чи входить цифра 2 в запис даного цілого числа n")
while True:
    try:
        x=int(input())
    except ValueError:
        print("Помилка! Спробуйте ще раз, введіть ціле число!")
        continue
    else:
        y=x
        c=0
        while y>0:
            z=y%10
           # print(y)
            # print(z)
            if z==2:
                print("Введене число містить в собі 2")
                c=1
                break
            y=y//10
            if y==2:
                print("Введене число містить в собі 2")
                c=1
                break
        if c==0:
            print("Введене число не містить в собі 2")
        try_again = input("Введіть 1 - продовжити або будь-який інший символ - завершити: ") 
        if try_again == "1":
            continue
        else:
            exit_program = input("До побачення!\n Щоб вийти, натисніть Enter") 
        break
