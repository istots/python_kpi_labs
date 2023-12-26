while True:
    phrase_first = input('Enter first phrase:' )
    phrase_second = input('Enter second phrase:' )
    s1 = ''.join(ch for ch in phrase_first if ch.isalpha())
    s2 = ''.join(ch for ch in phrase_second if ch.isalpha())
    set1 = set(s1.lower())
    set2 = set(s2.lower())
    x = set1.issubset(set2)
    print(set1)
    print(set2)
    if x == True:
        print("It is possible to make a sentence")
    else:
        print("It is not possible to make a sentence")
    try_again = input("Enter 1 to continue or any other symbol for exit: ") 
    if try_again == "1":
        continue
    else:
        exit_program = input("Bye!\n For exit press Enter") 
        break
