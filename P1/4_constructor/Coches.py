import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Método constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase.

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
      self.marca=marca
      self.color=color
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas
   
    
    # Crear los metodos getter y setter estos métodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los archivos a traves de estos métodos ... digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.
    #En teoría se debería de crear un método getters y setters por cada atributo que contenga la clase.
    #Los métodos get siempre regresan valor es decir el valor de la propiedad a traves del return 
    #Por otro lado el método set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión

    #1er forma
    def getMarca(self):
       return self.marca
    
    def setMarca(self, Marca):
       self.marca=Marca

    _marca2 = "" 
    #2da forma
    @property
    def marca2(self):
       return self._marca2
    
    @marca2.setter
    def marca2(self, marca):
       self._marca2=marca

    def getColor(self):
       return self.color
    
    def setColor(self, Color):
       self.color=Color

    def getModelo(self):
       return self.modelo
    
    def setModelo(self, Modelo):
       self.modelo=Modelo

    def getVelocidad(self):
       return self.velocidad
    
    def setVelocidad(self, Velocidad):
       self.velocidad=Velocidad

    def getCaballaje(self):
       return self.caballaje
    
    def setCaballaje(self, Caballaje):
       self.caballaje=Caballaje

    def getPlazas(self):
       return self.plazas
    
    def setPlazas(self, Plazas):
       self.plazas=Plazas

    
    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      pass

    def frenar(self):
      pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("W", "Blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3=Coches("Honda", "", "", 0, 0, 0)
coche1.num_serie="123456789"
coche4=Coches("","","",0,0,0)
coche4.marca2="Volvo"
print(coche4.marca2)


print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}\n Número de serie: {coche1.num_serie} ")

print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

coche3.marca2 = "Honda"
print(coche3.marca2)