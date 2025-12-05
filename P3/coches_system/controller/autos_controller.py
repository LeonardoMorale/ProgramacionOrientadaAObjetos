from model.autos import Autos

class AutosController:
    @staticmethod
    def consultar():
        return Autos.consultar()

    @staticmethod
    def consultar_por_id(id_coche):
        return Autos.consultar_por_id(id_coche)

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        return Autos.insertar(marca, color, modelo, velocidad, caballaje, plazas)

    @staticmethod
    def actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas):
        return Autos.actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas)

    @staticmethod
    def borrar(id_coche):
        return Autos.borrar(id_coche)
