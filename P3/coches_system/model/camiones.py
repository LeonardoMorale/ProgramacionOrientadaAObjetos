from conexionBD import conexion, cursor 

class Camiones:
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar camiones: {e}")
            return []

    @staticmethod
    def consultar_por_id(id_camion):
        try:
            cursor.execute("SELECT * FROM camiones WHERE id = %s", (id_camion,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al consultar camion por ID: {e}")
            return None

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar camion: {e}")
            return False

    @staticmethod
    def actualizar(id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            sql = """UPDATE camiones SET 
                     marca = %s, 
                     color = %s, 
                     modelo = %s, 
                     velocidad = %s, 
                     caballaje = %s, 
                     plazas = %s,
                     eje = %s,
                     capacidadCarga = %s
                     WHERE id = %s""" 
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id_camion)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar camion: {e}")
            return False

    @staticmethod
    def borrar(id_camion):
        try:
            sql = "DELETE FROM camiones WHERE id = %s"
            val = (id_camion,)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al borrar camion: {e}")
            return False
