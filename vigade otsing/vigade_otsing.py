#последовательность
from math import *
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala",round(S,1))
P=4*a
#либо двоиные кавычки,либо одиночные
print("Ruudu ümbermõõt",round(P,2))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
#лишняя скобка
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
#нету кавычки
print('Ristküliku pindala',S)
#Знак умножения
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
#убрать math
di=sqrt(b**2+c**2)

print("Ristküliku diagonaal", round(di,2))
print()
print("Ringi karakteristikud")
#изменить кавычки и убрать одну скобку
r=float(input("Sisesta ringi raadiusi pikkus =>"))
#добавить *
d=2*r
#добавить запятую
print("Ringi läbimõõt",str(d))
S=pi*r**2
#добавить скобку в конце
print("Ringi pindala", round(S,2))
#добавить *
C=2*pi*r
#добавить скобку в конце
print("Ringjoone pikkus", round(C,2))
