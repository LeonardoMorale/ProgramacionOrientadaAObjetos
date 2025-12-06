from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller.autos_controller import AutosController

class MenuCoches:
    def __init__(self, ventana, back_callback):
        self.ventana = ventana
        self.back_callback = back_callback

    def limipia_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_coches(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Autos")
        Label(self.ventana, text="AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Autos", command=self.insertar_autos).pack(pady=10)
        Button(self.ventana, text="Consultar Autos", command=self.consultar_autos).pack(pady=10)
        Button(self.ventana, text="Actualizar Autos", command=self.actualizar_autos).pack(pady=10)
        Button(self.ventana, text="Borrar Autos", command=self.borrar_autos).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.back_callback).pack(pady=10)

    def insertar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Insertar Autos")
        Label(self.ventana, text="INSERTAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Marca:").pack(pady=5); self.c_marca = Entry(self.ventana); self.c_marca.pack()
        Label(self.ventana, text="Color:").pack(pady=5); self.c_color = Entry(self.ventana); self.c_color.pack()
        Label(self.ventana, text="Modelo:").pack(pady=5); self.c_modelo = Entry(self.ventana); self.c_modelo.pack()
        Label(self.ventana, text="Velocidad:").pack(pady=5); self.c_velocidad = Entry(self.ventana); self.c_velocidad.pack()
        Label(self.ventana, text="Caballaje:").pack(pady=5); self.c_caballaje = Entry(self.ventana); self.c_caballaje.pack()
        Label(self.ventana, text="Plazas:").pack(pady=5); self.c_plazas = Entry(self.ventana); self.c_plazas.pack()

        def guardar_auto():
            if self.c_marca.get() == "":
                messagebox.showwarning("Error", "Faltan datos")
                return
            
            # Llamamos al modelo
            exito = AutosController.insertar(
                self.c_marca.get(), self.c_color.get(), self.c_modelo.get(),
                self.c_velocidad.get(), self.c_caballaje.get(), self.c_plazas.get()
            )
            if exito:
                messagebox.showinfo("Éxito", "Auto guardado correctamente")
                self.menu_acciones_coches()
            else:
                messagebox.showerror("Error", "Error al guardar")

        Button(self.ventana, text="Guardar", command=guardar_auto).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_coches).pack(pady=10)

    def consultar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Consultar Autos")
        Label(self.ventana, text="LISTADO DE AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Conexión real al modelo
        registros = AutosController.consultar()
        
        cadena=""
        if not registros:
            cadena = "No hay autos registrados."
        else:
            for registro in registros:
                cadena += f"ID: {registro[0]} | Marca: {registro[2]} | Color: {registro[1]} | Modelo: {registro[3]} | Vel: {registro[4]}\n"
        
        lbl_registros = Label(self.ventana, text=cadena, justify=LEFT)
        lbl_registros.pack(pady=10)
        
        Button(self.ventana, text="Volver", command=self.menu_acciones_coches).pack(pady=10)

    def actualizar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Actualizar Autos")
        Label(self.ventana, text="ACTUALIZAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # Frame para la búsqueda
        frame_busqueda = Frame(self.ventana)
        frame_busqueda.pack(pady=10)

        Label(frame_busqueda, text="ID del Auto a actualizar:").pack(side=LEFT, padx=5)
        self.c_id_upd = Entry(frame_busqueda)
        self.c_id_upd.pack(side=LEFT, padx=5)

        # Frame para los campos de edición
        self.frame_edicion = Frame(self.ventana)
        self.frame_edicion.pack(pady=10)

        def buscar_auto():
            id_buscar = self.c_id_upd.get()
            if not id_buscar:
                messagebox.showwarning("Error", "Ingrese un ID")
                return

            registro = AutosController.consultar_por_id(id_buscar)
            
            # Limpiar frame de edición por si acaso se busca otro ID
            for widget in self.frame_edicion.winfo_children():
                widget.destroy()

            if registro:
                messagebox.showinfo("Encontrado", "El auto existe, puede actualizar los datos.")
                
                # Campos
                Label(self.frame_edicion, text="Marca:").pack(); self.c_marca_upd = Entry(self.frame_edicion); self.c_marca_upd.pack()
                self.c_marca_upd.insert(0, registro[2]) # Marca

                Label(self.frame_edicion, text="Color:").pack(); self.c_color_upd = Entry(self.frame_edicion); self.c_color_upd.pack()
                self.c_color_upd.insert(0, registro[1]) # Color

                Label(self.frame_edicion, text="Modelo:").pack(); self.c_modelo_upd = Entry(self.frame_edicion); self.c_modelo_upd.pack()
                self.c_modelo_upd.insert(0, registro[3]) # Modelo

                Label(self.frame_edicion, text="Velocidad:").pack(); self.c_velocidad_upd = Entry(self.frame_edicion); self.c_velocidad_upd.pack()
                self.c_velocidad_upd.insert(0, registro[4]) # Velocidad

                Label(self.frame_edicion, text="Caballaje:").pack(); self.c_caballaje_upd = Entry(self.frame_edicion); self.c_caballaje_upd.pack()
                self.c_caballaje_upd.insert(0, registro[5]) # Caballaje

                Label(self.frame_edicion, text="Plazas:").pack(); self.c_plazas_upd = Entry(self.frame_edicion); self.c_plazas_upd.pack()
                self.c_plazas_upd.insert(0, registro[6]) # Plazas

                Button(self.frame_edicion, text="Actualizar", command=actualizar_datos).pack(pady=20)

            else:
                messagebox.showerror("Error", "No se encontró un auto con ese ID")

        def actualizar_datos():
            exito = AutosController.actualizar(
                self.c_id_upd.get(),
                self.c_marca_upd.get(),
                self.c_color_upd.get(),
                self.c_modelo_upd.get(),
                self.c_velocidad_upd.get(),
                self.c_caballaje_upd.get(),
                self.c_plazas_upd.get()
            )
            
            if exito:
                messagebox.showinfo("Éxito", "Auto actualizado correctamente")
                self.menu_acciones_coches()
            else:
                messagebox.showerror("Error", "Error al actualizar")

        Button(frame_busqueda, text="Buscar", command=buscar_auto).pack(side=LEFT, padx=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_coches).pack(pady=10)

    def borrar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Autos")
        Label(self.ventana, text="BORRAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Introduce el ID que deseas eliminar:").pack(pady=10)
        self.c_id_del = Entry(self.ventana)
        self.c_id_del.pack()

        def eliminar_auto():
            if AutosController.borrar(self.c_id_del.get()):
                messagebox.showinfo("Éxito", "Auto eliminado")
                self.menu_acciones_coches()
            else:
                messagebox.showerror("Error", "No se pudo eliminar (Revise el ID)")

        Button(self.ventana, text="Borrar", command=eliminar_auto).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_coches).pack(pady=10)
