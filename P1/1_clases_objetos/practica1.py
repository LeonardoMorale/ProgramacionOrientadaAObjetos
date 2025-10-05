import os
os.system("cls")
#Implementar paradigmas Estructurados VS POO

#Estructurado
def sum(base,altura):
    suma = base*altura
    return suma

b = float(input("Tamaño de la base: "))
h = float(input("Tamaño de la altura: "))
a = sum(b,h)
print(f"El area del rectangulo es: {a}")

#POO
class Rectangulos:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura
    
rect1 = Rectangulos(b,h)
print(f"Area: {rect1.area()}")