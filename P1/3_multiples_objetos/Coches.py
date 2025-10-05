"""
COPIA CON multiples objetos (VARIOS OBJETOS DE LA MISMA CLASE)
"""

import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    #Crear los metodos setters y getters, estos metodos son importantes y ncesesarios en todas las clases para que el programador interactue con los valores de los atributos a través de estos métodos...digamos que esta es la manera mas adecuada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a través de un objeto.
    #En teoria se deberia crear un metodo Getters y Setters por cada atributo que contenga la clase

    #Los metodos get siempre regresan valor, es decir el valor de la propiedad a traves del return

    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión

    #1er forma
    def getMarca(self):
       return self.marca
    
    def setMarca(self,marca):
       self.marca=marca

    #2da Forma
    @property
    def marca2(self):
       return self.marca
    
    @marca2.setter
    def marca2(self, marca):
       self.marca=marca

    def getColor(self):
       return self.color
    
    def setColor(self,color):
       self.color=color

    def getModelo(self):
       return self.modelo
    
    def setModelo(self,modelo):
       self.modelo=modelo

    def getVelocidad(self):
       return self.velocidad
    
    def setVelocidad(self,velocidad):
       self.velocidad=velocidad

    def getCaballaje(self):
       return self.caballaje
    
    def setCaballaje(self,caballaje):
       self.caballaje=caballaje

    def getPlazas(self):
       return self.plazas
    
    def setPlazas(self,plazas):
       self.plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase
coche1 = Coches()
coche2 = Coches()
coche3 = Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie = "B013928493"


coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)


coche3.marca2 = "Honda"


print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n Numero de Serie: {coche1.num_serie} ")

"""
coche2.marca = "Nissan"
coche2.color = "Azul"
coche2.modelo = "2020"
coche2.velocidad = 180
coche2.caballaje = 150
coche2.plazas = 6
"""