fruits = ["apple","banana","cherry"]
fruits2 = ["melon","kiwi"]
print(fruits)
print(fruits2)

fruits.extend(fruits2)
print(fruits)

fruits.reverse()
print(fruits)

digits = [6,3,4,26,231,52,31,523,561,3,2,45,1]
print(digits)
digits.sort(reverse=False)
print(digits)
digits.sort(reverse=True)
print(digits)

my_string = "my name is Vova"
my_list = my_string.split(" ")
print(my_list)

jointed_string = " ".join(my_list)
print(my_string)

print(sum(digits))