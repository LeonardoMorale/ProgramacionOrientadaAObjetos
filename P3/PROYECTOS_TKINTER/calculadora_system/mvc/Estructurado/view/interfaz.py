from tkinter import *
from controller import funciones

def interfaz_principal():
    ventana = Tk()
    ventana.geometry("600x800")
    ventana.resizable(False,False)
    ventana.title("Calculadora")

    n1 = IntVar()
    n2 = IntVar()

    numero1 = Entry(ventana, textvariable=n1)
    numero1.pack()

    numero2 = Entry(ventana, textvariable=n2)
    numero2.pack()

    btn_suma = Button(ventana, text="+", command=lambda: funciones.operaciones(n1.get(),n2.get(),"+"))
    btn_suma.pack()

    btn_resta = Button(ventana, text="-", command=lambda: funciones.operaciones(n1.get(),n2.get(),"-"))
    btn_resta.pack()

    btn_multiplicar = Button(ventana, text="*", command=lambda: funciones.operaciones(n1.get(),n2.get(),"x"))
    btn_multiplicar.pack()

    btn_division = Button(ventana, text="/", command=lambda: funciones.operaciones(n1.get(),n2.get(),"/"))
    btn_division.pack()

    btn_salir = Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack()

    ventana.mainloop()