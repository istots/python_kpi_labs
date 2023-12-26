print('Лабораторна робота 5. 9 варіант. Корсун Єлизавета, КМ-23')
print('Використання функцій. Завдання 2.\nНаписати функцію, що буде вставляти підрядок s1 y рядок s починаючи з n позиції')

def insert(s,s1,n): 
    result = ''
    for i in range(len(s)):
        if i == n:
            result += s1
        else:
            result += s[i]
    return result


