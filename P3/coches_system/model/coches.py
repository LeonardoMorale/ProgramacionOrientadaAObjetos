from conexionBD import conexion, cursor 

# ---------------------------------------------------------
# CLASE AUTOS (Tabla: coches)
# ---------------------------------------------------------
class Autos:
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar coches: {e}")
            return []

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO coches (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar coche: {e}")
            return False

    @staticmethod
    def actualizar(id_coche, marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = """UPDATE coches SET 
                     marca = %s, 
                     color = %s, 
                     modelo = %s, 
                     velocidad = %s, 
                     caballaje = %s, 
                     plazas = %s 
                     WHERE id = %s""" 
            val = (marca, color, modelo, velocidad, caballaje, plazas, id_coche)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar coche: {e}")
            return False

    @staticmethod
    def borrar(id_coche):
        try:
            sql = "DELETE FROM coches WHERE id = %s"
            val = (id_coche,)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al borrar coche: {e}")
            return False


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


# ---------------------------------------------------------
# CLASE CAMIONES (Tabla: camiones)
# Campos extra: eje, capacidadCarga
# ---------------------------------------------------------
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