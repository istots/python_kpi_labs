a = [1]

while True:
    try:
        degree = int(input('Введіть ступінь полінома: '))
        if degree < 0:
            raise ValueError
    except ValueError:
        print('Ви повинні ввести додатнє ціле число!')
    break

for i in range(degree + 1):
    b = [1]
    b += [a[q] + a[q + 1] for q in range(len(a) - 1)] + [1]
    print(*a)
    a = b
