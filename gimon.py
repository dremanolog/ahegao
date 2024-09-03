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
print ("Where are you looking and what do you see?")
