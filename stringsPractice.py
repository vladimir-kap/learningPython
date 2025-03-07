print('lol')
name='test'
age='77'

def print_numbers(x):
    if x <= 5:  # Базовый случай: если x больше 0
        print(x)  # Выводим текущее значение x
        print_numbers(x + 1)  # Рекурсивный вызов с уменьшенным значением x

x = 1 # Пример числа для рекурсии
print_numbers(x)

print(f"my name is {name}, and my age is {age}")

my_string = input('enter a number')

if my_string.isdigit():
    my_integer=int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
    
print(my_string.format(price=49))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 523))



string = """
Популярные команды
git status
Показывает статус работы. Новые, зафикс­иро­ванные, измененные файлы. Текущую ветку.
git diff [file]
Показывает изменения между рабочей директ­орией и зафикс­иро­ванными измене­ниями
git diff --staged [file]
Показывает изменения между зафикс­иро­ванными измене­ниями и индексом (заком­иче­нными измене­ниями)
git checkout [file]
Отменяет изменения в рабочей директории. Операция необра­тимая.
git add [file]
Фиксирует изменения файла. Исполь­зуйте ., чтобы добавить все изменения в директории и поддир­ект­ориях.
git reset [file]
Отменяет фиксацию файла.
"""

print(string)

first_name = 'Alice'
last_name = 'Smith'
name_operated = first_name + last_name
print(len(name_operated), name_operated)

