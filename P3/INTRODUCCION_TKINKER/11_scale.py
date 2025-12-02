from tkinter import *

ventana = Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarValor():
    resultado.config(text=f"Valor selecionado por el usuario: {valor.get()}")


valor = IntVar()
escala = Scale(ventana, from_=0, to=100, orient=HORIZONTAL, variable=valor)
escala.pack()

boton_escala = Button(ventana, text="Mostrar valor", command=mostrarValor)
boton_escala.pack()

resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()