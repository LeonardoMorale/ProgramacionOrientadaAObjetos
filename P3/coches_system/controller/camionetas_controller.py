from model.camionetas import Camionetas

class CamionetasController:
    @staticmethod
    def consultar():
        return Camionetas.consultar()

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        return Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

    @staticmethod
    def actualizar(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        return Camionetas.actualizar(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

    @staticmethod
    def borrar(id_camioneta):
        return Camionetas.borrar(id_camioneta)
