from tkinter import *

def hazClick():
    lbl_titulo.config(
        text="POO con python",
        bg="green",
        foreground="red",
        width=50,
        height=4,
        font=("Arial",30,"bold"),
        border=2,
        relief=SUNKEN
    )

def regresarClick():
    lbl_titulo.config(
        text="Bienvenido a Tkinter",
        bg="lightblue",
        foreground="darkblue",
        width=50,
        height=4,
        font=("Helvetica",30,"italic"),
        border=2,
        relief=SUNKEN
    )

ventana = Tk()
ventana.title("Personalización de widgets u objetos")
ventana.geometry("500x500")

lbl_titulo = Label(ventana, text="Bienvenidos a Tkinter")
lbl_titulo.config(
    bg="lightblue",
    foreground="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    border=2,
    relief=SUNKEN
)
lbl_titulo.pack(pady=50)

btn_hazclick = Button(ventana, text="Haz click aqui", command=hazClick)
btn_hazclick.config(
    fg="#787878",
    activeforeground="yellow",
    width=15,
    font=("Arial",20,"bold")
)
btn_hazclick.pack()

btn_regresar = Button(ventana, text="Regresar click aqui", command=regresarClick)
btn_regresar.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial",20,"bold")
)
btn_regresar.pack(pady=5)

ventana.mainloop()