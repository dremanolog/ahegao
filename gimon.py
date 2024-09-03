def sum(x,y):
    result=a+b
    return sum
def min(x,y):
    min=a-b
    return min
def delenie(x,y):
    result=a/b
    return delenie
def umn(x,y):
    result=a*b
    return umn
def ste(x,y):
    result=a**b
    return ste

print("этот калькулятор умножает, складывает, делит, вычитает и степень")
print("для выбора действия впишите + - / * **")
a=int(input("первое число"))
c=str(input("введите действие"))
b=int(input("второе число"))
l=[]
if c=="+":
    print(sum)
if c=="-":
    print(min)
if c=="/":
    print(delenie)
if c=="*":
    print(umn)
if c=="**":
    print(ste)
else:
    print(0)
    
# Where are you looking and what do you see?
# Well, this is my broken password generator code.
# p.s. Mika.

import random
import string

def gen_pas(length):
	letters = string.ascii_letters
	numbers = string.digits
	symbol = string.punctuation
	password = ''.join((random.choice(letters),random.choice(numbers), random.choice(symbol)))
	for i in range(length - 3):
		password += random.choice((letters, numbers, symbol))
	return password
length = int(input("Длинна пароля: "))
password = gen_pas(length)
print(password)
