from model.autos import Autos

class AutosController:
    @staticmethod
    def consultar():
        return Autos.consultar()

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        return Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)

    @staticmethod
    def actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas):
        return Autos.actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas)

    @staticmethod
    def borrar(id_coche):
        return Autos.borrar(id_coche)
