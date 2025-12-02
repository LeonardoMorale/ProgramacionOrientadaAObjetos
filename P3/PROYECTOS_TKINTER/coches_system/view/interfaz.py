from tkinter import *
from tkinter import ttk
from model import coches
from tkinter import messagebox

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Gestion de Coches")
        self.ventana.geometry("1150x900")
        self.ventana.resizable(False, False)
        
        self.menuprincipal()

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menuprincipal(self):
        self.limipia_ventana()
        self.ventana.title("Menu Principal")
        
        frame_menu = Frame(self.ventana)
        frame_menu.pack(expand=True)

        Label(frame_menu, text="GESTION DE COCHES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(frame_menu, text="Coches", command=self.menu_acciones).pack(pady=10)
        Button(frame_menu, text="Camionetas", command="").pack(pady=10)
        Button(frame_menu, text="Camiones", command="").pack(pady=10)

        Button(frame_menu, text="Salir", command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Autos")
        Label(self.ventana, text="AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Autos", command=self.insertar_autos).pack(pady=10)
        Button(self.ventana, text="Consultar Autos",command=self.consultar_autos).pack(pady=10)
        Button(self.ventana, text="Actualizar Autos", command="").pack(pady=10)
        Button(self.ventana, text="Borrar Autos", command="").pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.menuprincipal).pack(pady=10)

    def insertar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Autos")
        Label(self.ventana, text="INSERTAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(pady=10)
        Entry(self.ventana).pack()

        Label(self.ventana, text="Color:").pack(pady=10)
        Entry(self.ventana).pack()

        Label(self.ventana, text="Modelo:").pack(pady=10)
        Entry(self.ventana).pack()

        Label(self.ventana, text="Velocidad:").pack(pady=10)
        Entry(self.ventana).pack()

        Label(self.ventana, text="Caballaje:").pack(pady=10)
        Entry(self.ventana).pack()

        Label(self.ventana, text="Plazas:").pack(pady=10)
        Entry(self.ventana).pack()

        Button(self.ventana, text="Guardar", command=coches.Autos.insertar).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)

    def consultar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Autos")
        Label(self.ventana, text="LISTADO DE AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

    
        
        registros = coches.Autos.consultar()
        if not registros:
            messagebox.showinfo("Consulta", "No hay autos registradas en la base de datos.")
            return
        cadena=""
        contador=1
        for registro in registros:
            cadena+=f"Auto {contador} ID: {registro[0]} Marca: {registro[1]} Color: {registro[2]} Modelo: {registro[4]} Velocidad: {registro[3]} Caballaje: {registro[5]}\n"
            contador+=1
        lbl_registros = Label(self.ventana, text=cadena)
        lbl_registros.pack()
        
        btn_volver = Button(self.ventana, text="Volver", command=self.menu_acciones)
        btn_volver.pack(pady=10)

    def borrar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Autos")
        Label(self.ventana, text="BORRAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Introduce el ID que deseas eliminar:").pack(pady=10)
        Entry(self.ventana).pack()

        Button(self.ventana, text="Borrar", command=coches.Autos.borrar).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=10)
