x=9
y=4
print (x//y)

integer = 2+3*5
print(integer)

my_int=10
my_float=5.6
print(float(my_int))
print(my_int+my_float)

print(round(my_float))

#task:
print('insert number of apartment')
x=24
#input(x)
p=(x-1)//20+1 #тут нужно сначала от вводимой квартиры отнять 1. Из-за особенности целочисленного деления. Иначе выдаст подъезд 2 при вводе квартиры 1;
f=(x-1)%20//4+1
print('your input value is ', x, 'so yours appartment floor', (int(f)) ,'and entrance is:', (int(p)))