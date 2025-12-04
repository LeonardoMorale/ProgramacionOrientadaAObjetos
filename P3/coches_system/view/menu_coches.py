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
            
            # Llamamos a Autos del archivo model/coches.py
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
                # Ajustado a tu SQL: id, color, marca, modelo, velocidad, caballaje, plazas
                # Nota: Verifica el orden de columnas en tu BD, aquí asumo el orden estándar del SELECT *
                cadena += f"ID: {registro[0]} | Marca: {registro[2]} | Color: {registro[1]} | Modelo: {registro[3]} | Vel: {registro[4]}\n"
        
        lbl_registros = Label(self.ventana, text=cadena, justify=LEFT)
        lbl_registros.pack(pady=10)
        
        Button(self.ventana, text="Volver", command=self.menu_acciones_coches).pack(pady=10)

    def actualizar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Actualizar Autos")
        Label(self.ventana, text="ACTUALIZAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="ID del Auto a actualizar:").pack(pady=5)
        self.c_id_upd = Entry(self.ventana)
        self.c_id_upd.pack()
        
        Label(self.ventana, text="Nueva Marca:").pack(pady=5); self.c_marca_upd = Entry(self.ventana); self.c_marca_upd.pack()
        Label(self.ventana, text="Nuevo Color:").pack(pady=5); self.c_color_upd = Entry(self.ventana); self.c_color_upd.pack()
        Label(self.ventana, text="Nuevo Modelo:").pack(pady=5); self.c_modelo_upd = Entry(self.ventana); self.c_modelo_upd.pack()
        Label(self.ventana, text="Nueva Velocidad:").pack(pady=5); self.c_velocidad_upd = Entry(self.ventana); self.c_velocidad_upd.pack()
        Label(self.ventana, text="Nuevo Caballaje:").pack(pady=5); self.c_caballaje_upd = Entry(self.ventana); self.c_caballaje_upd.pack()
        Label(self.ventana, text="Nuevas Plazas:").pack(pady=5); self.c_plazas_upd = Entry(self.ventana); self.c_plazas_upd.pack()

        def actualizar_datos():
            if self.c_id_upd.get() == "":
                messagebox.showwarning("Error", "Falta el ID")
                return
            
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
                messagebox.showerror("Error", "Error al actualizar (Revise el ID)")

        Button(self.ventana, text="Actualizar", command=actualizar_datos).pack(pady=20)
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
