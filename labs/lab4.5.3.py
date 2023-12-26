while True:
            try:
                real_year=int(input())
                real_year >= 1
            except ValueError:
                print("Error! Use real age!")
                continue
            else:
                break
if real_year < 3:
        dog_year=real_year*10.5
else:
        dog_year = 21 + 4*(real_year-2)
print(dog_year)
