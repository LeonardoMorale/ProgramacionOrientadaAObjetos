from conexionBD import conexion, cursor 

# ---------------------------------------------------------
# CLASE CAMIONETAS (Tabla: camionetas)
# Campos extra: traccion, cerrada
# ---------------------------------------------------------
class Camionetas:
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar camionetas: {e}")
            return []

    @staticmethod
    def consultar_por_id(id_camioneta):
        try:
            cursor.execute("SELECT * FROM camionetas WHERE id = %s", (id_camioneta,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al consultar camioneta por ID: {e}")
            return None

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar camioneta: {e}")
            return False

    @staticmethod
    def actualizar(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            sql = """UPDATE camionetas SET 
                     marca = %s, 
                     color = %s, 
                     modelo = %s, 
                     velocidad = %s, 
                     caballaje = %s, 
                     plazas = %s,
                     traccion = %s,
                     cerrada = %s
                     WHERE id = %s""" 
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id_camioneta)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar camioneta: {e}")
            return False

    @staticmethod
    def borrar(id_camioneta):
        try:
            sql = "DELETE FROM camionetas WHERE id = %s"
            val = (id_camioneta,)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al borrar camioneta: {e}")
            return False
