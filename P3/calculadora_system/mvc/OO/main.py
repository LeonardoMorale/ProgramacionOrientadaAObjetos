"""
Crear una Calculadora: 
    1.- Dos campos de Texto
    2.- 4 Botones para la Operaciones
    3.- Mostrar el resultado en una Alerta
    4.- Programado de forma Orientada a Objetos
    5.- Considerar el MVC
"""
from view import interfaz
from tkinter import *

class App:
    def __init__(self, window):
        #Ejecutar Ventana
        view = interfaz.Vista(window)

if __name__=="__main__":
    window = Tk()
    app = App(window)
    window.mainloop()