import sys
import os

# --- BLOQUE DE SOLUCIÓN DE IMPORTACIÓN ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexionBD import * # ------------------------------------------

class Nota:  
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        try:
            sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
            cursor.execute(sql, (usuario_id, titulo, descripcion))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear nota: {e}")
            return False

    @staticmethod
    def mostrar(usuario_id):
        try:
            sql = "SELECT * FROM notas WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar notas: {e}")
            return []

    @staticmethod
    def actualizar(id_nota, titulo, descripcion):
       try:
         sql = "UPDATE notas SET titulo=%s, descripcion=%s WHERE id=%s"
         cursor.execute(sql, (titulo, descripcion, id_nota))
         conexion.commit()
         return True
       except Exception as e:
         print(f"Error al actualizar: {e}") 
         return False
    
    @staticmethod
    def eliminar(id_nota):
        try:
          sql = "DELETE FROM notas WHERE id=%s"
          cursor.execute(sql, (id_nota,)) 
          conexion.commit() 
          return True  
        except Exception as e:
          print(f"Error al eliminar: {e}")    
          return False