x = int(input('Enter speed: ')) #x - змінна для позначення швидкості
if x < 0:
    print('Speed must be <0')   
elif x >= 0 and x <= 137:
    print('Minor')
elif x > 137 and x <= 177:
    print('Moderate')
elif x > 177 and x <= 217:
    print('Considerable') 
elif x > 177 and x <= 266:
    print('Serve')
elif x > 266 and x <= 322:
    print('Devastating')
else:
    print('Incredible')
    