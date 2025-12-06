from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller.camiones_controller import CamionesController

class MenuCamiones:
    def __init__(self, ventana, back_callback):
        self.ventana = ventana
        self.back_callback = back_callback

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Camiones")
        Label(self.ventana, text="CAMIONES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Camion", command=self.insertar_camiones).pack(pady=10)
        Button(self.ventana, text="Consultar Camiones", command=self.consultar_camiones).pack(pady=10)
        Button(self.ventana, text="Actualizar Camion", command=self.actualizar_camiones).pack(pady=10)
        Button(self.ventana, text="Borrar Camion", command=self.borrar_camiones).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.back_callback).pack(pady=10)

    def insertar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Camiones")
        Label(self.ventana, text="INSERTAR CAMION", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(); self.cam_marca = Entry(self.ventana); self.cam_marca.pack()
        Label(self.ventana, text="Color:").pack(); self.cam_color = Entry(self.ventana); self.cam_color.pack()
        Label(self.ventana, text="Modelo:").pack(); self.cam_modelo = Entry(self.ventana); self.cam_modelo.pack()
        Label(self.ventana, text="Velocidad:").pack(); self.cam_vel = Entry(self.ventana); self.cam_vel.pack()
        Label(self.ventana, text="Caballaje:").pack(); self.cam_cab = Entry(self.ventana); self.cam_cab.pack()
        Label(self.ventana, text="Plazas:").pack(); self.cam_plazas = Entry(self.ventana); self.cam_plazas.pack()
        # Campos Específicos
        Label(self.ventana, text="Número de Ejes:").pack(); self.cam_eje = Entry(self.ventana); self.cam_eje.pack()
        Label(self.ventana, text="Capacidad Carga (Kg):").pack(); self.cam_carga = Entry(self.ventana); self.cam_carga.pack()

        def guardar_camion():
            if self.cam_marca.get() == "":
                messagebox.showwarning("Error", "Faltan datos")
                return

            exito = CamionesController.insertar(
                self.cam_marca.get(), self.cam_color.get(), self.cam_modelo.get(),
                self.cam_vel.get(), self.cam_cab.get(), self.cam_plazas.get(),
                self.cam_eje.get(), self.cam_carga.get()
            )
            if exito:
                messagebox.showinfo("Éxito", "Camión guardado correctamente")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "Error al guardar camión")

        Button(self.ventana, text="Guardar", command=guardar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)

    def consultar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Camiones")
        Label(self.ventana, text="LISTADO CAMIONES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Conexión real al modelo
        registros = CamionesController.consultar()
        
        cadena = ""
        if not registros:
            cadena = "No hay camiones registrados."
        else:
            for registro in registros:
                # id, color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga
                cadena += f"ID: {registro[0]} | Marca: {registro[2]} | Modelo: {registro[3]} | Ejes: {registro[7]} | Carga: {registro[8]}\n"

        Label(self.ventana, text=cadena, justify=LEFT).pack(pady=10)
        Button(self.ventana, text="Volver", command=self.menu_acciones_camiones).pack(pady=10)

    def actualizar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Actualizar Camion")
        Label(self.ventana, text="ACTUALIZAR CAMION", font=("Times New Roman", 24,"bold")).pack(pady=20)
        
        # Frame para la búsqueda
        frame_busqueda = Frame(self.ventana)
        frame_busqueda.pack(pady=10)

        Label(frame_busqueda, text="ID a actualizar:").pack(side=LEFT, padx=5)
        self.cam_id_upd = Entry(frame_busqueda)
        self.cam_id_upd.pack(side=LEFT, padx=5)

        # Frame para los campos de edición
        self.frame_edicion = Frame(self.ventana)
        self.frame_edicion.pack(pady=10)

        def buscar_camion():
            id_buscar = self.cam_id_upd.get()
            if not id_buscar:
                messagebox.showwarning("Error", "Ingrese un ID")
                return

            registro = CamionesController.consultar_por_id(id_buscar)
            
            # Limpiar frame de edición
            for widget in self.frame_edicion.winfo_children():
                widget.destroy()

            if registro:
                messagebox.showinfo("Encontrado", "El camión existe, puede actualizar los datos.")
                
                # registro: id, color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga
                
                Label(self.frame_edicion, text="Marca:").pack(); self.cam_marca_upd = Entry(self.frame_edicion); self.cam_marca_upd.pack()
                self.cam_marca_upd.insert(0, registro[2])

                Label(self.frame_edicion, text="Color:").pack(); self.cam_color_upd = Entry(self.frame_edicion); self.cam_color_upd.pack()
                self.cam_color_upd.insert(0, registro[1])

                Label(self.frame_edicion, text="Modelo:").pack(); self.cam_modelo_upd = Entry(self.frame_edicion); self.cam_modelo_upd.pack()
                self.cam_modelo_upd.insert(0, registro[3])

                Label(self.frame_edicion, text="Velocidad:").pack(); self.cam_vel_upd = Entry(self.frame_edicion); self.cam_vel_upd.pack()
                self.cam_vel_upd.insert(0, registro[4])

                Label(self.frame_edicion, text="Caballaje:").pack(); self.cam_cab_upd = Entry(self.frame_edicion); self.cam_cab_upd.pack()
                self.cam_cab_upd.insert(0, registro[5])

                Label(self.frame_edicion, text="Plazas:").pack(); self.cam_plazas_upd = Entry(self.frame_edicion); self.cam_plazas_upd.pack()
                self.cam_plazas_upd.insert(0, registro[6])

                Label(self.frame_edicion, text="Número de Ejes:").pack(); self.cam_eje_upd = Entry(self.frame_edicion); self.cam_eje_upd.pack()
                self.cam_eje_upd.insert(0, registro[7])

                Label(self.frame_edicion, text="Capacidad Carga (Kg):").pack(); self.cam_carga_upd = Entry(self.frame_edicion); self.cam_carga_upd.pack()
                self.cam_carga_upd.insert(0, registro[8])

                Button(self.frame_edicion, text="Actualizar", command=guardar_actualizacion).pack(pady=20)

            else:
                messagebox.showerror("Error", "No se encontró un camión con ese ID")

        def guardar_actualizacion():
            exito = CamionesController.actualizar(
                self.cam_id_upd.get(),
                self.cam_marca_upd.get(), self.cam_color_upd.get(), self.cam_modelo_upd.get(),
                self.cam_vel_upd.get(), self.cam_cab_upd.get(), self.cam_plazas_upd.get(),
                self.cam_eje_upd.get(), self.cam_carga_upd.get()
            )

            if exito:
                messagebox.showinfo("Éxito", "Camión actualizado correctamente")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "No se pudo actualizar")

        Button(frame_busqueda, text="Buscar", command=buscar_camion).pack(side=LEFT, padx=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)

    def borrar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Camion")
        Label(self.ventana, text="BORRAR CAMION", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="ID a eliminar:").pack(); self.cam_id_del = Entry(self.ventana); self.cam_id_del.pack()

        def eliminar_camion():
            if CamionesController.borrar(self.cam_id_del.get()):
                messagebox.showinfo("Éxito", "Camión eliminado")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el camión")

        Button(self.ventana, text="Borrar", command=eliminar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)
