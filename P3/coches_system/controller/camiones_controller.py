from model.camiones import Camiones

class CamionesController:
    @staticmethod
    def consultar():
        return Camiones.consultar()

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        return Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)

    @staticmethod
    def actualizar(id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        return Camiones.actualizar(id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)

    @staticmethod
    def borrar(id_camion):
        return Camiones.borrar(id_camion)
