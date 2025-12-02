from tkinter import *

def mostrarSeleccion():
    lbl_opcion.config(text=f"Opcion seleccionada: {opcion.get()} ")

ventana = Tk()
ventana.title("Radiobutton")
ventana.geometry("500x500")

opcion = StringVar()
rdn_op1 = Radiobutton(ventana, text="Opción 1", variable=opcion, value="opcion1")
rdn_op1.pack()

rdn_op2 = Radiobutton(ventana, text="Opción 2", variable=opcion, value="opcion2")
rdn_op2.pack()

rdn_op3 = Radiobutton(ventana, text="Opción 3", variable=opcion, value="opcion3")
rdn_op3.pack()

btn_mostrar = Button(ventana, text="Mostrar Selección", command=mostrarSeleccion)
btn_mostrar.pack()

lbl_opcion = Label(ventana, text="")
lbl_opcion.pack()

ventana.mainloop()