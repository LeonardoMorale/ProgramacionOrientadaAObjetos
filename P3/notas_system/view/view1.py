from tkinter import *
from tkinter import messagebox
# Importamos el controlador desde su carpeta 'controller'
from controller import controlador

# Variables globales para mantener la sesión
id_user = None
nom_user = None
ape_user = None

class View:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title(".::Notas System::.")
        ventana.geometry("800x600")
        ventana.resizable(0,0)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..::Menú Principal::..", justify="center", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana,text="1.- Registro", command=lambda: View.registro(ventana), width=20)
        btn_registro.pack(pady=10)

        btn_login = Button(ventana,text="2.- Login", command=lambda: View.login(ventana), width=20)
        btn_login.pack(pady=10)

        btn_salir = Button(ventana,text="3.- Salir", command=ventana.quit, width=20)
        btn_salir.pack(pady=10)

    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..::Registro en el Sistema::..", justify="center")
        lbl_titulo.pack(pady=10)

        Label(ventana, text="Nombre:").pack()
        txt_nombre = Entry(ventana)
        txt_nombre.focus()
        txt_nombre.pack(pady=5)

        Label(ventana, text="Apellidos:").pack()
        txt_apellidos = Entry(ventana)
        txt_apellidos.pack(pady=5)

        Label(ventana, text="Email:").pack()
        txt_email = Entry(ventana)
        txt_email.pack(pady=5)

        Label(ventana, text="Contraseña:").pack()
        txt_contrasena = Entry(ventana, show="*")
        txt_contrasena.pack(pady=5)

        def realizar_registro():
            controlador.Controlador.registro(txt_nombre.get(), txt_apellidos.get(), txt_email.get(), txt_contrasena.get())
            View.login(ventana)

        btn_registro = Button(ventana,text="Registrar", command=realizar_registro)
        btn_registro.pack(pady=10)

        btn_volver = Button(ventana,text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def login(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text="..::Inicio de Sesión::..", justify="center")
        lbl_titulo.pack(pady=10)

        Label(ventana, text="Email:").pack()
        txt_email = Entry(ventana)
        txt_email.focus()
        txt_email.pack(pady=5)

        Label(ventana, text="Contraseña:").pack()
        txt_contrasena = Entry(ventana, show="*")
        txt_contrasena.pack(pady=5)

        btn_entrar = Button(ventana,text="Entrar", command=lambda: controlador.Controlador.inicio_sesion(ventana, txt_email.get(), txt_contrasena.get()))
        btn_entrar.pack(pady=10)

        btn_volver = Button(ventana,text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_notas(ventana, usuario_id, nombre, apellidos):
        global id_user, nom_user, ape_user
        id_user = usuario_id
        nom_user = nombre
        ape_user = apellidos
        
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..::Bienvenido {nombre} {apellidos}::..", justify="center", font=("Arial", 12))
        lbl_titulo.pack(pady=10)

        btn_crear = Button(ventana, text="1.- Crear Nota", command=lambda: View.crear_notas(ventana), width=30)
        btn_crear.pack(pady=5)

        btn_mostrar = Button(ventana, text="2.- Mostrar Mis Notas", command=lambda: View.mostrar_notas(ventana), width=30)
        btn_mostrar.pack(pady=5)

        btn_cambiar = Button(ventana, text="3.- Modificar Nota", command=lambda: View.cambiar_nota(ventana), width=30)
        btn_cambiar.pack(pady=5)

        btn_eliminar = Button(ventana, text="4.- Eliminar Nota", command=lambda: View.eliminar_nota(ventana), width=30)
        btn_eliminar.pack(pady=5)

        btn_regresar = Button(ventana, text="5.- Cerrar Sesión", command=lambda: View.menu_principal(ventana), width=30)
        btn_regresar.pack(pady=20)
    
    @staticmethod
    def crear_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"..::Crear Nota::..", justify="center")
        lbl_titulo.pack(pady=10)

        Label(ventana, text="Título:").pack()
        txt_titulo=Entry(ventana)
        txt_titulo.focus()
        txt_titulo.pack(pady=5)

        Label(ventana, text="Descripción:").pack()
        txt_descripcion=Entry(ventana)
        txt_descripcion.pack(pady=5)

        def guardar_nota():
            controlador.Controlador.crear_nota(id_user, txt_titulo.get(), txt_descripcion.get())
            txt_titulo.delete(0, END)
            txt_descripcion.delete(0, END)

        btn_guardar = Button(ventana, text="Guardar", command=guardar_nota)
        btn_guardar.pack(pady=10)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=10)
    
    @staticmethod
    def mostrar_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f"Tus notas son:", justify="center", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_notas = Frame(ventana)
        frame_notas.pack(pady=10)

        registros = controlador.Controlador.listar_notas(id_user)
        
        texto_notas = ""
        if len(registros) > 0:
            for fila in registros:
                texto_notas += f"ID: {fila[0]} | Título: {fila[2]} | Fecha: {fila[4]}\nDescripción: {fila[3]}\n{'-'*60}\n"
        else:
            texto_notas = "No tienes notas guardadas aún."

        lbl_datos = Label(frame_notas, text=texto_notas, justify="left", anchor="w")
        lbl_datos.pack()

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=20)

    @staticmethod
    def cambiar_nota(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::Modificar una Nota::.", justify="center")
        lbl_titulo.pack(pady=10)

        Label(ventana, text="ID de la nota a modificar:").pack()
        txt_id= Entry(ventana)
        txt_id.focus()
        txt_id.pack(pady=5)

        Label(ventana, text="Nuevo título:").pack()
        txt_nuevo_titulo= Entry(ventana)
        txt_nuevo_titulo.pack(pady=5)

        Label(ventana, text="Nueva descripción:").pack()
        txt_nueva_descripcion= Entry(ventana)
        txt_nueva_descripcion.pack(pady=5)

        def actualizar():
            controlador.Controlador.actualizar_nota(txt_id.get(), txt_nuevo_titulo.get(), txt_nueva_descripcion.get())
            txt_id.delete(0, END)
            txt_nuevo_titulo.delete(0, END)
            txt_nueva_descripcion.delete(0, END)

        btn_guardar = Button(ventana, text="Actualizar", command=actualizar)
        btn_guardar.pack(pady=10)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_nota(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana, text=f".::Eliminar una Nota::.", justify="center")
        lbl_titulo.pack(pady=10)

        Label(ventana, text="ID de la nota a eliminar:").pack()
        txt_id_eliminar=Entry(ventana)
        txt_id_eliminar.focus()
        txt_id_eliminar.pack(pady=5)

        def eliminar():
            controlador.Controlador.eliminar_nota(txt_id_eliminar.get())
            txt_id_eliminar.delete(0, END)

        btn_eliminar = Button(ventana, text="Eliminar permanentemente", bg="red", fg="white", command=eliminar)
        btn_eliminar.pack(pady=10)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=10)