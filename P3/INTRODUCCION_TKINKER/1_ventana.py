'''
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio
'''
#from tkinter import *

# ventana= Tk()

import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primer App gráfica en Tkinter con Python")
ventana.geometry("800x600")
ventana.resizable(False,False) #! Metodo para dar permiso de redimensionar una ventana
ventana.mainloop() #! Metodo que permite mantener la ventana abierta e interactuar con ella
