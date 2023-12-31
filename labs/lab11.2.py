def rrange(begin, end, step = 1):
    if step > 0 and begin >= end:
        return []
    if step < 0 and begin <= end:
        return []
    if step == 0:
        return []
    
    l = rrange(begin+step, end, step)
    l.insert(0,begin)
    # l = rrange(begin, end-step, step)
    # l.append(end-step)
    return l

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
# print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')