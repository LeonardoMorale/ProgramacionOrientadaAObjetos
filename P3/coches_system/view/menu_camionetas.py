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
            if self.cta_marca.get() == "":
                messagebox.showwarning("Error", "Faltan datos")
                return

            # Llamar al modelo
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

        # Llamada al modelo
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
        
        # Frame para la búsqueda
        frame_busqueda = Frame(self.ventana)
        frame_busqueda.pack(pady=10)

        Label(frame_busqueda, text="ID a actualizar:").pack(side=LEFT, padx=5)
        self.cta_id_upd = Entry(frame_busqueda)
        self.cta_id_upd.pack(side=LEFT, padx=5)

        # Frame para los campos de edición (inicialmente oculto o vacío)
        self.frame_edicion = Frame(self.ventana)
        self.frame_edicion.pack(pady=10)

        def buscar_camioneta():
            id_buscar = self.cta_id_upd.get()
            if not id_buscar:
                messagebox.showwarning("Error", "Ingrese un ID")
                return

            registro = CamionetasController.consultar_por_id(id_buscar)
            
            # Limpiar frame de edición
            for widget in self.frame_edicion.winfo_children():
                widget.destroy()

            if registro:
                messagebox.showinfo("Encontrado", "La camioneta existe, puede actualizar los datos.")
                
                # Campos a actualizar
                Label(self.frame_edicion, text="Marca:").pack(); self.cta_marca_upd = Entry(self.frame_edicion); self.cta_marca_upd.pack()
                self.cta_marca_upd.insert(0, registro[2])

                Label(self.frame_edicion, text="Color:").pack(); self.cta_color_upd = Entry(self.frame_edicion); self.cta_color_upd.pack()
                self.cta_color_upd.insert(0, registro[1])

                Label(self.frame_edicion, text="Modelo:").pack(); self.cta_modelo_upd = Entry(self.frame_edicion); self.cta_modelo_upd.pack()
                self.cta_modelo_upd.insert(0, registro[3])

                Label(self.frame_edicion, text="Velocidad:").pack(); self.cta_vel_upd = Entry(self.frame_edicion); self.cta_vel_upd.pack()
                self.cta_vel_upd.insert(0, registro[4])

                Label(self.frame_edicion, text="Caballaje:").pack(); self.cta_cab_upd = Entry(self.frame_edicion); self.cta_cab_upd.pack()
                self.cta_cab_upd.insert(0, registro[5])

                Label(self.frame_edicion, text="Plazas:").pack(); self.cta_plazas_upd = Entry(self.frame_edicion); self.cta_plazas_upd.pack()
                self.cta_plazas_upd.insert(0, registro[6])

                Label(self.frame_edicion, text="Tracción (ej. 4x4):").pack(); self.cta_traccion_upd = Entry(self.frame_edicion); self.cta_traccion_upd.pack()
                self.cta_traccion_upd.insert(0, registro[7])

                Label(self.frame_edicion, text="¿Cerrada? (1=Si, 0=No):").pack(); self.cta_cerrada_upd = Entry(self.frame_edicion); self.cta_cerrada_upd.pack()
                self.cta_cerrada_upd.insert(0, registro[8])

                Button(self.frame_edicion, text="Actualizar", command=guardar_actualizacion).pack(pady=20)

            else:
                messagebox.showerror("Error", "No se encontró una camioneta con ese ID")

        def guardar_actualizacion():
            exito = CamionetasController.actualizar(
                self.cta_id_upd.get(),
                self.cta_marca_upd.get(), self.cta_color_upd.get(), self.cta_modelo_upd.get(),
                self.cta_vel_upd.get(), self.cta_cab_upd.get(), self.cta_plazas_upd.get(),
                self.cta_traccion_upd.get(), self.cta_cerrada_upd.get()
            )

            if exito:
                messagebox.showinfo("Éxito", "Camioneta actualizada correctamente")
                self.menu_acciones_camionetas()
            else:
                messagebox.showerror("Error", "No se pudo actualizar")

        Button(frame_busqueda, text="Buscar", command=buscar_camioneta).pack(side=LEFT, padx=10)
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
            
            # Llamada al modelo
            if CamionetasController.borrar(id_borrar):
                messagebox.showinfo("Éxito", "Camioneta eliminada")
                self.menu_acciones_camionetas()
            else:
                messagebox.showerror("Error", "No se encontró el ID o hubo un error")

        Button(self.ventana, text="Borrar", command=eliminar_datos).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camionetas).pack(pady=10)
