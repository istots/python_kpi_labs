import re
import json
from collections import Counter
from string import ascii_lowercase as letters
def read_file(path):
    with open(path, encoding="utf8") as file:
        text = file.read().lower()
    return text

def find_letters(text):
    cnt = Counter()
    for letter in letters:
        cnt[letter] = text.count(letter)
    return dict(cnt)

txt = read_file('D:/Lisa/gadsby.txt')
print(find_letters(txt))