from tkinter import *

def entrar():
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
    lbl_resultado.config(
        text="BIENVENIDO"
    )

# def regresarClick():
#     lbl_titulo.config(
#         text="Bienvenido a Tkinter",
#         bg="lightblue",
#         foreground="darkblue",
#         width=50,
#         height=4,
#         font=("Helvetica",30,"italic"),
#         border=2,
#         relief=SUNKEN
#     )

ventana = Tk()
ventana.title("Entry")
ventana.geometry("500x500")

lbl_titulo = Label(ventana, text="Acceso al sistema")
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

lbl_nombre = Label(ventana, text="Ingrese el nombre: ")
lbl_nombre.pack(pady=5)

txt_nombre = Entry(ventana)
txt_nombre.pack()

lbl_password = Label(ventana, text="Ingrese la contraseña: ")
lbl_password.pack(pady=5)

txt_contraseña = Entry(ventana, show="*")
txt_contraseña.pack()

btn_entrar = Button(ventana, text="Entrar", command=entrar)
btn_entrar.pack(pady=5)

btn_borrar = Button(ventana, text="Borrar", command="borrar")
btn_borrar.pack(pady=5)

lbl_resultado = Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()