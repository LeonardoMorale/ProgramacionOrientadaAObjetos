from tkinter import *

'''
def cambiarTexto():
    mensajeCambiante.config(
        text="Hola, ¿Como estas?"
    )

def regresarTexto():
    mensajeCambiante.config(
        text="Texto original"
    )

ventana = Tk()
ventana.title("Uso de Botones")
ventana.geometry("800x600")

frame_principal = Frame(ventana)
frame_principal.config(
    bg="silver",
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)
label_titulo=Label(frame_principal,text="Uso de botones")
label_titulo.config(
    bg="silver",
    width=20,
)
label_titulo.pack(pady=10)

mensajeCambiante = Label(ventana, text="Texto Original")
mensajeCambiante.pack()

boton_cambiar = Button(ventana, text="Cambiar texto", command=cambiarTexto)
boton_cambiar.pack()

boton_regresar = Button(ventana, text="Regresar texto", command=regresarTexto)
boton_regresar.pack()


ventana.mainloop()
'''

def iniciarSesion():
    main_frame.destroy()
    login_frame = Frame(ventana)
    login_frame.config(
        bg="#FDDF1A",
        width=750,
        height=550,
        border=2,
        relief="flat"
    )
    login_frame.pack_propagate(False)
    login_frame.pack(pady=50)

    lbl_title = Label(login_frame, text=f"Bienvenido {user}", font=("Papyrus",40),bg="#FDDF1A")
    lbl_title.pack(pady=30)

    info_frame = Frame(login_frame)
    info_frame.config(
        bg="#FFFFFF",
        width=500,
        height=330,
        border=2,
        relief=GROOVE
    )
    info_frame.pack_propagate(False)
    info_frame.pack(pady=50)

ventana = Tk()
ventana.title("Inicio de sesion en Tkinter")
ventana.geometry("800x600")

main_frame = Frame(ventana)
main_frame.config(
    bg="#FDDF1A",
    width=750,
    height=550,
    border=2,
    relief="flat"
)
main_frame.pack_propagate(False)
main_frame.pack(pady=50)

user = "Juan Perez"
password = "123456"

lbl_title = Label(main_frame, text="Inicio de sesión", bg="#FDDF1A", font=("Papyrus",40))
lbl_title.pack(pady=100)

lbl_usuario = Label(main_frame, text=f"Nombre de usuario: {user}", bg="#FDDF1A", font=("Times New Roman",20))
lbl_usuario.pack()

lbl_usuario = Label(main_frame, text=f"Contraseña: {password}", bg="#FDDF1A", font=("Times New Roman",20))
lbl_usuario.pack()

button_login = Button(main_frame, text="Iniciar sesion", command=iniciarSesion)
button_login.config(
    width=40,
    height=10
)
button_login.pack_propagate(False)
button_login.pack(pady=30)

ventana.mainloop()