'''
Ejercicio Practico 3
'''
import os
os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

    #Metodos o acciones o funciones que hace el objeto 
    '''
    Crear los métodos getter y setter, estos métodos son importantes y ncesarios en todas las clases 
    para que el programador interactue con los valores de los atributos a traves de estos métodos. 
    Digamos que es la manera más adecuada y recomendada para solicitar un valor (get) 
    y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.
    
    En teoria se debería de crear un método getters y setters por cada atributo que contenga la clase
    Los métodos get siempre regresan valor, es decir el valor de la propoedad a traves del return
    por otro lado el método set siempre recive parametros para cambiar o modificar el valor 
    del atributo o proiedad en cuestion
    '''
    
    #1er Forma
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca  
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self, caballaje):
        self.__caballaje = caballaje
    
    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self, plazas):
        self.__plazas = plazas
   
    def acelerar(self):
        print("Estas acelerando")

    def frenar(self):
        print("Estas frenando")  

#Fin definir clase

#Crear un objetos o instanciar la clase
""" 
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,5)

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3.marca2="Honda"
print(coche3.marca2) """

'''
class Coches:
    marca = ""
    color = ""
    modelo = ""
    velocidad = 0
    caballaje = 0
    piezas = 0
    
    def acelerar(self):
        pass
    def frenars(self):
        pass
    
coche1 = Coches()
coche1.marca = "BMW"
coche1.color = "Blanco"
coche1.modelo = "2022"
coche1.velocidad= "220"
coche1.caballaje= "150"
coche1.piezas= "5"

coche2 = Coches()
coche2.marca = "Nissan"
coche2.color= "Azul"
coche2.modelo = "2020"
coche2.velocidad = "180"
coche2.caballaje= "150"
coche2.piezas = "6"

print("=== Coche 1 ===")
print("Marca:", coche1.marca)
print("Color:", coche1.color)
print("Modelo:", coche1.modelo)
print("Velocidad:", coche1.velocidad)
print("Caballaje:", coche1.caballaje)
print("Piezas:", coche1.piezas)

print("\n=== Coche 2 ===")
print("Marca:", coche2.marca)
print("Color:", coche2.color)
print("Modelo:", coche2.modelo)
print("Velocidad:", coche2.velocidad)
print("Caballaje:", coche2.caballaje)
print("Piezas:", coche2.piezas)
'''