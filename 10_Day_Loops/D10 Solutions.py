#1
"""
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
"""
old_num = 0
for num in range(101):
    new_num = old_num + num
    old_num = new_num
print(old_num)






