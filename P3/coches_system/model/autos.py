from conexionBD import conexion, cursor 

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
    def consultar_por_id(id_coche):
        try:
            cursor.execute("SELECT * FROM coches WHERE id = %s", (id_coche,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al consultar coche por ID: {e}")
            return None

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
