str = input('Enter list:' )
x = str.split()
#print(x)
s = ""
l = len(x)
for i, w in enumerate(x):
    if l == 1:
        s = w
    elif l == 2:
        if i == 0:
            s = w
        else:
            s = s + ' and ' + w
    else:
        if i != l - 1:
            s = s + w + ', '
        else: 
            s = s + 'and ' + w
print(s)