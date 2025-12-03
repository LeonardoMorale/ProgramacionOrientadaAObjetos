"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las Operaciones
3.- Mostrar el Resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

def resultado(tipo,operacion):
    messagebox.showinfo(title=f"{tipo}", icon="info", message=f"El resultado de la {tipo} es: {operacion}")

def suma(n1,n2):
    tipo = "suma"
    operacion = n1 + n2
    resultado(tipo,operacion)

def resta(n1,n2):    
    tipo = "resta"
    operacion = n1 - n2
    resultado(tipo,operacion)

def multiplicacion(n1,n2):    
    tipo = "multiplicacion"
    operacion = n1 * n2
    resultado(tipo,operacion)
    
def division(n1,n2):    
    if n2 == 0:
        messagebox.showwarning(message="No se puede dividir entre cero")
    else:
        tipo = "division"
        operacion = n1 / n2
        resultado(tipo,operacion) 

#Interfaz
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

btn_suma = Button(ventana, text="+", command=lambda: suma(n1.get(),n2.get()))
btn_suma.pack()

btn_resta = Button(ventana, text="-", command=lambda: resta(n1.get(),n2.get()))
btn_resta.pack()

btn_multiplicar = Button(ventana, text="*", command=lambda: multiplicacion(n1.get(),n2.get()))
btn_multiplicar.pack()

btn_division = Button(ventana, text="/", command=lambda: division(n1.get(),n2.get()))
btn_division.pack()

btn_salir = Button(ventana, text="Salir", command=ventana.quit)
btn_salir.pack()

ventana.mainloop()