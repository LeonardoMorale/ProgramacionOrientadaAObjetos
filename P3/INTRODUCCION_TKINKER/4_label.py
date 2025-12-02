from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Etiquetas")

#Etiqueta o Label

etiqueta1 = Label(ventana, text="Nombre de la persona", font=("papyrus", 30)).pack()

marco1=Frame(ventana, bg="#39429B",width=400, height=100)
marco1.pack_propagate(False)
marco1.pack()

etiqueta2 = Label(marco1, text="Soy una etiqueta dentro de un marco", bg="#39429B").pack()


ventana.mainloop()