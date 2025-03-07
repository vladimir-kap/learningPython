from random import randint
from unicodedata import numeric


# fruits = ['plum', 'kiwi', 'lichi','strawberry','melon', 'mango', 'peach']
# students = ['valery','anton','sasha','pavel','andrey','vova']

# for fruit in fruits:
#     print(fruit)
#     for char in fruit:
#         print(char)
        
numbers = [52,32,56,753,634,64,75,3,2,6,234,7,32,4,32,634,22,1,3,123,1523,2367,33,43,23,23]
random_numbers=[]
even_numbers=[]
count=10
i=0
while i < count:
    random_numbers.append(randint(1,1000))
    i += 1
print(random_numbers)
for number in random_numbers:
    if number%2 == 0:
        even_numbers.append(number)
        continue
    print(number)
print(even_numbers)

for i in range(10):
    if i == 7:
        print('7? I hate prime numbers bigger than 5!')
    else:
        print(f'Woo! I love the number {i}')
        

for i in range(10):
    if i == 7:
        print('7? I hate prime numbers bigger than 5!')
        continue
    print(f'Woo! I love the number {i}')
    
range_object=range(2,50,4)
range_list=list(range_object)
print(range_object)
print(range_list)
print(range_list[::2])
print(range_list[2:5])
print(range_list[50:5:-1])

range_object_reversed=range(2,50,2)
range_list_reversed=list(range_object_reversed[::-1])
print(range_list_reversed)