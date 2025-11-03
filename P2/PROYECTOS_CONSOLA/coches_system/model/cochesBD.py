from conexionBD import *

class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
        
    def insertar(self):
        try:
            cursor.execute(
                "insert into autos values (null, %s,%s,%s,%s,%s,%s)",
                (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod    
    def consultar():
        try:
            cursor.execute("select * from autos")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas,id):
        try:
            cursor.execute(
                "update autos set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s where id_carro=%s",
                (marca, color, modelo, velocidad, caballaje, plazas,id)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from autos where id_carro=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False

class Camionetas:
    @staticmethod
    def insertar(marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            cursor.execute(
                "insert into camionetas values(null, %s,%s,%s,%s,%s,%s,%s,%s)", 
                (marca,color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod    
    def consultar():
        try:
            cursor.execute("select * from camionetas")
            return cursor.fetchall()
        except:
            return []
    
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas,traccion, cerrada, id):
        try:
            cursor.execute(
                "update camionetas set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,traccion=%s, cerrada=%s where id_camioneta=%s",
                (marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada, id)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from camionetas where id_camioneta=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False

class Camiones:
    @staticmethod
    def insertar(marca,color, modelo, velocidad, caballaje, plazas, eje,capacidadCarga):
        try:
            cursor.execute(
                "insert into camiones values(null, %s,%s,%s,%s,%s,%s,%s,%s)", 
                (marca,color, modelo, velocidad, caballaje, plazas,eje, capacidadCarga)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod    
    def consultar():
        try:
            cursor.execute("select * from camiones")
            return cursor.fetchall()
        except:
            return []     
        
    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id):
        try:
            cursor.execute(
                "update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s,eje=%s, capacidadCarga=%s where id_camion=%s",
                (marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga, id)
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from camiones where id_camion=%s",(id,)
            )
            conexion.commit()
            return True
        except:
            return False
        