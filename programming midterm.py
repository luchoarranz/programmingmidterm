a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3

print(2+3*6/2)

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

strings = [ "6892149109325320763773670235239019412986", "1414884937242655719669145562427394884141", "9847255590886266818998186626880955527489", "6800923757255865070000705685527573290086"]
not_palindromes = [string for string in strings if not palindrome(string)]
print("Strings that are NOT palindromes:", not_palindromes)


list = [1, 2, 3, 4]
print(list)
list = [10, 20, 30, 40]
print(list)

string = "hey"
print(string)
new_string = "bye"
print(new_string)


import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

random_numbers = [number if number <= 50 else "XX" for number in random_numbers]


