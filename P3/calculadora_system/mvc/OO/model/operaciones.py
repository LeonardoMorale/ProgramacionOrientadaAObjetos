from conexionBD import *

class Operaciones:
    @staticmethod
    def insertar(n1, n2, signo, resultado):
        try:
            cursor.execute("INSERT INTO operaciones VALUES (null, NOW(), %s, %s, %s, %s)", (n1, n2, signo, resultado))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM operaciones")
            operacion = cursor.fetchall()
            return operacion
        except:
            return []
    
    @staticmethod
    def consultar_id(id):
        try:
            cursor.execute("SELECT * FROM operaciones where id = %s",(id,))
            operacion = cursor.fetchall()
            return operacion
        except:
            return []

    @staticmethod
    def actualizar(n1, n2, signo, resultado, id):
        try:
            query = "UPDATE operaciones SET Fecha=NOW(), Numero1=%s, Numero2=%s, Signo=%s, Resultado=%s WHERE id=%s"
            cursor.execute(query, (n1, n2, signo, resultado, id))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM operaciones WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False
