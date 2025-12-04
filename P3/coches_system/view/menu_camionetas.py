from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller.camionetas_controller import CamionetasController

class MenuCamionetas:
    def __init__(self, ventana, back_callback):
        self.ventana = ventana
        self.back_callback = back_callback

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Camionetas")
        Label(self.ventana, text="CAMIONETAS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Camioneta", command=self.insertar_camionetas).pack(pady=10)
        Button(self.ventana, text="Consultar Camionetas", command=self.consultar_camionetas).pack(pady=10)
        Button(self.ventana, text="Actualizar Camioneta", command=self.actualizar_camionetas).pack(pady=10)
        Button(self.ventana, text="Borrar Camioneta", command=self.borrar_camionetas).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.back_callback).pack(pady=10)

    def insertar_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Camionetas")
        Label(self.ventana, text="INSERTAR CAMIONETA", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Definición de campos
        Label(self.ventana, text="Marca:").pack(); self.cta_marca = Entry(self.ventana); self.cta_marca.pack()
        Label(self.ventana, text="Color:").pack(); self.cta_color = Entry(self.ventana); self.cta_color.pack()
        Label(self.ventana, text="Modelo:").pack(); self.cta_modelo = Entry(self.ventana); self.cta_modelo.pack()
        Label(self.ventana, text="Velocidad:").pack(); self.cta_vel = Entry(self.ventana); self.cta_vel.pack()
        Label(self.ventana, text="Caballaje:").pack(); self.cta_cab = Entry(self.ventana); self.cta_cab.pack()
        Label(self.ventana, text="Plazas:").pack(); self.cta_plazas = Entry(self.ventana); self.cta_plazas.pack()
        Label(self.ventana, text="Tracción (ej. 4x4):").pack(); self.cta_traccion = Entry(self.ventana); self.cta_traccion.pack()
        Label(self.ventana, text="¿Cerrada? (1=Si, 0=No):").pack(); self.cta_cerrada = Entry(self.ventana); self.cta_cerrada.pack()

        # Función interna para capturar datos y guardar
        def guardar_datos():
            # Validar que no estén vacíos (opcional pero recomendado)
            if self.cta_marca.get() == "":
                messagebox.showwarning("Error", "Faltan datos")
                return

            # Llamar al MODELO
            exito = CamionetasController.insertar(
                self.cta_marca.get(), self.cta_color.get(), self.cta_modelo.get(),
                self.cta_vel.get(), self.cta_cab.get(), self.cta_plazas.get(),
                self.cta_traccion.get(), self.cta_cerrada.get()
            )

            if exito:
                messagebox.showinfo("Éxito", "Camioneta guardada correctamente")
                self.menu_acciones_camionetas() # Volver al menú
            else:
                messagebox.showerror("Error", "No se pudo guardar en la BD")

        Button(self.ventana, text="Guardar", command=guardar_datos).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camionetas).pack(pady=10)

    def consultar_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Camionetas")
        Label(self.ventana, text="LISTADO CAMIONETAS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Llamada al MODELO
        registros = CamionetasController.consultar()
        
        cadena = ""
        if not registros:
            cadena = "No hay camionetas registradas."
        else:
            for registro in registros:
                # registro es una tupla: (id, color, marca, modelo, velocidad, caballaje, plazas, traccion, cerrada)
                cadena += f"ID: {registro[0]} | Marca: {registro[2]} | Modelo: {registro[3]} | Tracción: {registro[7]}\n"

        Label(self.ventana, text=cadena, justify=LEFT).pack(pady=10)
        Button(self.ventana, text="Volver", command=self.menu_acciones_camionetas).pack(pady=10)

    def actualizar_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Actualizar Camioneta")
        Label(self.ventana, text="ACTUALIZAR CAMIONETA", font=("Times New Roman", 24,"bold")).pack(pady=20)
        
        Label(self.ventana, text="ID a actualizar:").pack(); self.cta_id_upd = Entry(self.ventana); self.cta_id_upd.pack()
        # Aquí puedes añadir los campos que quieras editar
        Label(self.ventana, text="Nueva Tracción:").pack(); self.cta_traccion_upd = Entry(self.ventana); self.cta_traccion_upd.pack()

        Button(self.ventana, text="Actualizar", command=lambda: messagebox.showinfo("Info", "Actualizar Camioneta")).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camionetas).pack(pady=10)

    def borrar_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Camioneta")
        Label(self.ventana, text="BORRAR CAMIONETA", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="ID a eliminar:").pack()
        self.cta_id_del = Entry(self.ventana)
        self.cta_id_del.pack()

        def eliminar_datos():
            id_borrar = self.cta_id_del.get()
            if not id_borrar:
                return
            
            # Llamada al MODELO
            if CamionetasController.borrar(id_borrar):
                messagebox.showinfo("Éxito", "Camioneta eliminada")
                self.menu_acciones_camionetas()
            else:
                messagebox.showerror("Error", "No se encontró el ID o hubo un error")

        Button(self.ventana, text="Borrar", command=eliminar_datos).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camionetas).pack(pady=10)
