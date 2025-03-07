from hmac import new
import random as rand


fruits = ["apple","banana","cherry"]
print(fruits)

my_list = [2,3,4,True,'sus',['babka',2,4]]
print(my_list)

print(4800000*0.04)

print(len(fruits))

my_list1 = [1,2,3]
my_list2 = [1,3,2]
my_list3 = [1,2,3]

print(my_list1==my_list2)
print(my_list1==my_list3)

print(bool([]))
print(bool([2]))

print("banana" in fruits)
print("watermelon" in fruits)

element1 = "apple"
element2 = "banana"
element3 = "cherry"

fruits3 = [element1,element2,element3]
print(fruits3)

word = "hello"
my_list4 = list(word)
print(my_list4)

my_list5 = [1,2,3]
my_list6 = [4,5,6]
my_list7 = my_list5 + my_list6
print(my_list7)

fruits.append("watermelon")
print(fruits)

my_string = "hello, world"
new_string = my_string.replace("world", "python")
print(new_string)

secondFruit = fruits[2]
print('second fruit is =', secondFruit)

#fruit = fruits.pop()
print(fruits)


secondFruit = fruits[2]
print('2 fruit is =', secondFruit)
fruits = ["apple","banana","cherry"]
secondFruit = fruits[2]
print('index 2 fruit is =', secondFruit)
print(fruits)
print('-2 fruit is =', fruits[-1])

# fruits = ['apple','banana','cherry']
# fruits2 = ['plum','kiwi','lichi','mango','peach']
# i=len(fruits2)
# #while i != 0:
#     i=i-1
#     rand_position=rand.randint(0,(len(fruits2)-1))
#     del fruits2[rand_position]
#     fruits.append(fruits2[rand_position-1])
#     print(fruits2)
#     print(fruits)

import random

fruits = ['apple', 'banana', 'cherry']
fruits2 = ['plum', 'kiwi', 'lichi','strawberry','melon', 'mango', 'peach']
print(fruits2)
fruits2[1],fruits2[-2]=fruits2[-2],fruits2[1]
fruits2[0],fruits2[-1]=fruits2[-1],fruits2[0]
print(fruits2)
fruits3 = []

while fruits2:
    # Выбираем случайный элемент из fruits2
    random_fruit = random.choice(fruits2)
    # Убираем его из fruits2
    fruits2.remove(random_fruit)
    # Добавляем в fruits3
    fruits3.append(random_fruit)

# Добавляем элементы из fruits в fruits3
fruits3.extend(fruits)

print("Итоговый список fruits3:", fruits3)

print(fruits3[::-1])

for i in fruits3:
    print(i)
    
count_o = 0    
greeting = "hello world, nice to see you, big O"
for i in greeting:
    print(i)
    if i == "o" or i == "O":
        count_o += 1
print(count_o)

#test git