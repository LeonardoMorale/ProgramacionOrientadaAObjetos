import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='coches',
        port=3307
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Ocurrio un error con la BD verifique...")

