from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Menu")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

menuBar = Menu(ventana)
ventana.config(menu=menuBar)
archivoMenu = Menu(menuBar, tearoff=1)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command = ventana.quit)

archivoMenu2 = Menu(menuBar, tearoff=1)
menuBar.add_cascade(label="Edición", menu=archivoMenu2)
archivoMenu2.add_command(label="Copiar",command=lambda: mensaje("Copiar archivo") )
archivoMenu2.add_command(label="Recortar",command=lambda: mensaje("Recortar archivo") )
archivoMenu2.add_separator()
archivoMenu2.add_command(label="Cerrar", command = ventana.quit)

resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()