from tkinter import *

def mostrarEstado():
    if opcion.get() == 1:
        lbl_notificaciones.config(text=f"Notificaciones activadas")
    elif opcion.get() == 0:
        lbl_notificaciones.config(text=f"Notificaciones desactivadas")
    

ventana = Tk()
ventana.title("Checkbutton")
ventana.geometry("500x500")

opcion=IntVar()
checkBoton = Checkbutton(ventana, text="¿Deseas recibir notificaciones?",variable=opcion, onvalue=1, offvalue=0)
checkBoton.pack()

btn_confirmar = Button(ventana, text="Confirmar", command=mostrarEstado)
btn_confirmar.pack()

lbl_notificaciones = Label(ventana, text="")
lbl_notificaciones.pack()

ventana.mainloop()