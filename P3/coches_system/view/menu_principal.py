from tkinter import *
from tkinter import messagebox
from view.menu_coches import MenuCoches
from view.menu_camionetas import MenuCamionetas
from view.menu_camiones import MenuCamiones

class MenuPrincipal:
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

        # He conectado los comandos a sus funciones correspondientes
        Button(frame_menu, text="Coches", command=self.abrir_coches).pack(pady=10)
        Button(frame_menu, text="Camionetas", command=self.abrir_camionetas).pack(pady=10)
        Button(frame_menu, text="Camiones", command=self.abrir_camiones).pack(pady=10)

        Button(frame_menu, text="Salir", command=self.ventana.quit).pack(pady=10)

    def abrir_coches(self):
        menu = MenuCoches(self.ventana, self.menuprincipal)
        menu.menu_acciones_coches()

    def abrir_camionetas(self):
        menu = MenuCamionetas(self.ventana, self.menuprincipal)
        menu.menu_acciones_camionetas()

    def abrir_camiones(self):
        menu = MenuCamiones(self.ventana, self.menuprincipal)
        menu.menu_acciones_camiones()
