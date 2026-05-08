#1
for number in range(11):
    print(number)
num = 0
while num <= 10:
    print(num)
    num +=1

#2
for number in range(10,-1,-1):
    print(number)
num = 10
while num >= 0:
    print(num)
    num -=1

#3
for row in range(7):
    print('#' * row)

#4
for i in range(8):
    for j in range(8):
        print('# ')
    print()

#5
for j in range(11):
    print(f"{j} * {j} = {j*j}", end='\n')


#6

langs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in langs:
    print(lang)


#7A
for num in range(101):
    if num % 2 != 0:
        continue
    print(num)

#7B
for num in range(0,101,2):
    print(num)


#8A
for num in range(100):
    if num % 2 == 0:
        continue
    print(num)

#8B
for num in range(1,100,2):
    print(num)
#2-1
old_num = 0
for num in range(101):
    new_num = old_num + num
    old_num = new_num
print(old_num)

#2-2
old_num = 0
odd_sum = 0
even_sum = 0
for num in range(101):
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num
print(f"suma de even es {even_sum} y la suma de odd es {odd_sum}")

#3-1
from data.countries import countries as cont
for country in cont:
    if country.__contains__("land"):
        print(country)

#3-2
fruits = ['banana', 'orange', 'mango', 'lemon']
rev_fruit = []
for fruit in range(len(fruits) -1, -1, -1):
    rev_fruit.append(fruits[fruit])
print(rev_fruit)

chacha = fruits[::-1]
print(chacha)

#3-1A
langs = 0
import data.codata as cod
for country in cod.countries:
    for lang in country["languages"]:
        langs += 1
print(langs)

#3-1B
import data.codata as cod
all_langs = []
for country in cod.countries:
    for lang in country["languages"]:
        all_langs.append(lang)
unique_langs = set(all_langs)
for unique_lang in unique_langs:
    repeated = all_langs.count(unique_lang)
    print(f"{unique_lang} appears {repeated} times")

from operator import itemgetter

#3-1C
import data.codata as cod
most_pop = []
for country in cod.countries:
    most_pop.append((country["name"], country["population"]))
top = most_pop.sort(key=itemgetter(1), reverse=True)
most_pop = most_pop[:10]
for i in most_pop:
    print(i)









