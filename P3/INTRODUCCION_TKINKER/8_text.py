from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Text")

def mostrar():
    mostrarcontenido=textarea.get("1.0",END).strip()
    lbl_resultado.config(text=f"Comentario: {mostrarcontenido}")

label_uno = Label(ventana,text="Escriba su comentario: ")
label_uno.pack()

frametext = Frame(ventana,width=100,height=50)
frametext.pack()
textarea = Text(frametext,width=40,height=12)
textarea.pack()

btn = Button(ventana,text="Mostrar comentario",command=mostrar)
btn.pack()
lbl_resultado = Label(ventana,text="")
lbl_resultado.pack()

ventana.mainloop()