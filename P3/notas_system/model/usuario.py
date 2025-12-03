import sys
import os
import hashlib
import datetime

# --- BLOQUE DE SOLUCIÓN DE IMPORTACIÓN ---
# Esto agrega la carpeta principal (root) a la ruta de búsqueda de Python
# para que pueda encontrar 'conexionBD.py' sin problemas.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexionBD import * # ------------------------------------------

class Usuario:
    @staticmethod
    def registrar(nombre, apellidos, email, password):
        try:
            fecha = datetime.datetime.now()
            # Encriptamos la contraseña
            pass_cifrada = hashlib.sha256(password.encode()).hexdigest()
            
            sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
            datos = (nombre, apellidos, email, pass_cifrada, fecha)
            
            cursor.execute(sql, datos)
            conexion.commit()
            return True
        except Exception as e:
            # ESTO ES IMPORTANTE: Imprime el error real en la consola
            print(f"Error en el registro: {e}")
            return False

    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            pass_cifrada = hashlib.sha256(contrasena.encode()).hexdigest()
            sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"
            
            cursor.execute(sql, (email, pass_cifrada))
            usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"Error en login: {e}")
            return None