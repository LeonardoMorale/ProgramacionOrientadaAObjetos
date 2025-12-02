from tkinter import *

ventana = Tk()
ventana.title("Mainloop")

ventana.geometry("800x600")


marco = Frame(ventana)
marco.config(
    bg="#F1F7A3",
    bd=98,
    height=400,
    width=600,
    relief=RAISED
)
marco.pack(
    padx= 100,
    pady= 100
)
ventana.mainloop()