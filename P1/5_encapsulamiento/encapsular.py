import os
os.system("cls")

class Clase:
    atributo_publico = "Soy Publico"
    _atributo_protegido = "Soy Protegido"
    __atributo_privado = "Soy Privado"

    def __init__(self,color,size):
        self.__color = color
        self.__size = size

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color = color

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,size):
        self.__size = size

    def getAtributoPrivado(self):
        return self.__atributo_privado

    def setAtributoPrivado(self,atributo):
        self.__atributo_privado = atributo

objeto = Clase("Rojo","Grande")
print(f"El color del objeto es: {objeto.color} y el tamaño es: {objeto.size}")

#Usar los atributos y métodos de acuerdo a su encapsulamiento
print(f"Contenido del atributo publico: {objeto.atributo_publico}")    
print(f"Contenido del atributo protegido: {objeto._atributo_protegido}")      
print(f"Contenido del atributo privado: {objeto.getAtributoPrivado()}")
objeto.setAtributoPrivado("Se ha cambiado el valor del atributon privado")   
print(f"Contenido del atributo privado: {objeto.getAtributoPrivado()}")