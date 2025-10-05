import os
os.system("cls")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
    
    #Primera Forma
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca=marca  
    
    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color=color
    
    def getModelo(self):
        return self._modelo
    
    def setModelo(self, modelo):
        self._modelo=modelo
    
    def getVelocidad(self):
        return self._velocidad
    
    def setVelocidad(self, velocidad):
        self._velocidad=velocidad
    
    def getCaballaje(self):
        return self._caballaje
    
    def setCaballaje(self, caballaje):
        self._caballaje=caballaje
    
    def getPlazas(self):
        return self._plazas
    
    def setPlazas(self, plazas):
        self._plazas=plazas
    
    
    def acelerar(self):
        return "Estas acelerando el coche"

    def frenar(self):
        return "Estas frenando el coche"

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidad):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje = eje
        self.__capacidad = capacidad

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando el camión"

    def frenar(self):
        return "Estas frenando el camión"

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self,eje):
        self.__eje = eje

    @property
    def capacidad(self):
        return self.__capacidad
    
    @capacidad.setter
    def capacidad(self,capacidad):
        self.__capacidad = capacidad

    
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,num_pasajero):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__num_pasajero = num_pasajero

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando la camioneta"

    def frenar(self):
        return "Estas frenando la camioneta"

    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def traccion(self,traccion):
        self.__traccion = traccion

    @property
    def num_pasajero(self):
        return self.__num_pasajero
    
    @num_pasajero.setter
    def num_pasajero(self,num_pasajero):
        self.__num_pasajero = num_pasajero
