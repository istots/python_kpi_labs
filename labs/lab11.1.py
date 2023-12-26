def cons(head, tails = []):
    l = []
    for el in tails:
        l.append(el)
    l.insert(0, head)
    return l

l = cons(3, 
        cons(2, 
            cons(1)))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

def sum(lst):
    l = []
    if len(lst) == 0:
        return 0
    s = 0
    for i in range(len(lst)):
        if i == 0:
            s += lst[i]
        else:
            l.append(lst[i])        
    s += sum(l)
    return s

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')