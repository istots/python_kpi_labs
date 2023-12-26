def cards():
    suit = 'spades, clubs, diamonds, hearts'.split(', ')
    list_of_cards = ['A', *range(2, 11), 'J', 'Q', 'K']
    for i in suit:
        for j in list_of_cards:
            yield str(j) + ' ' + i


new_pack = cards()

while True:
    print(next(new_pack))