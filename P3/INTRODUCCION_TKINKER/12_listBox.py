from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("ListBox")

def mostrarSeleccion():
    valor = lista.get(lista.curselection())
    seleccion.config(text=f"Seleccionaste: {valor}")

lista = Listbox(ventana, width=50, height=5, selectmode="single")
opciones=["Azul","Rojo","Negro","Amarillo"]

for i in opciones:
    lista.insert(END,i)


lista.pack()

boton = Button(ventana, text="Mostrar Selección del Usuario", command=mostrarSeleccion)
boton.pack()

seleccion = Label(ventana, text="")
seleccion.pack()

ventana.mainloop()