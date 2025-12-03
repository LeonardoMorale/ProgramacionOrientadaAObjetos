from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.coches import Autos, Camionetas, Camiones

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

    # ---------------------------------------------------------
    # MENU PRINCIPAL
    # ---------------------------------------------------------
    def menuprincipal(self):
        self.limipia_ventana()
        self.ventana.title("Menu Principal")
        
        frame_menu = Frame(self.ventana)
        frame_menu.pack(expand=True)

        Label(frame_menu, text="GESTION DE COCHES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        # He conectado los comandos a sus funciones correspondientes
        Button(frame_menu, text="Coches", command=self.menu_acciones_coches).pack(pady=10)
        Button(frame_menu, text="Camionetas", command=self.menu_acciones_camionetas).pack(pady=10)
        Button(frame_menu, text="Camiones", command=self.menu_acciones_camiones).pack(pady=10)

        Button(frame_menu, text="Salir", command=self.ventana.quit).pack(pady=10)

    # ---------------------------------------------------------
    # SECCION COCHES
    # ---------------------------------------------------------
    def menu_acciones_coches(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Autos")
        Label(self.ventana, text="AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Autos", command=self.insertar_autos).pack(pady=10)
        Button(self.ventana, text="Consultar Autos", command=self.consultar_autos).pack(pady=10)
        Button(self.ventana, text="Actualizar Autos", command=self.actualizar_autos).pack(pady=10)
        Button(self.ventana, text="Borrar Autos", command=self.borrar_autos).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.menuprincipal).pack(pady=10)

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
            exito = Autos.insertar(
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
        registros = Autos.consultar()
        
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
        
        Label(self.ventana, text="Nuevo Color:").pack(pady=5)
        self.c_color_upd = Entry(self.ventana)
        self.c_color_upd.pack()

        Button(self.ventana, text="Actualizar", command=lambda: messagebox.showinfo("Info", "Conectar Update Model")).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_coches).pack(pady=10)

    def borrar_autos(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Autos")
        Label(self.ventana, text="BORRAR AUTOS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="Introduce el ID que deseas eliminar:").pack(pady=10)
        self.c_id_del = Entry(self.ventana)
        self.c_id_del.pack()

        def eliminar_auto():
            if Autos.borrar(self.c_id_del.get()):
                messagebox.showinfo("Éxito", "Auto eliminado")
                self.menu_acciones_coches()
            else:
                messagebox.showerror("Error", "No se pudo eliminar (Revise el ID)")

        Button(self.ventana, text="Borrar", command=eliminar_auto).pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_coches).pack(pady=10)

    # ---------------------------------------------------------
    # SECCION CAMIONETAS (Campos extra: Traccion, Cerrada)
    # ---------------------------------------------------------
    def menu_acciones_camionetas(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Camionetas")
        Label(self.ventana, text="CAMIONETAS", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Camioneta", command=self.insertar_camionetas).pack(pady=10)
        Button(self.ventana, text="Consultar Camionetas", command=self.consultar_camionetas).pack(pady=10)
        Button(self.ventana, text="Actualizar Camioneta", command=self.actualizar_camionetas).pack(pady=10)
        Button(self.ventana, text="Borrar Camioneta", command=self.borrar_camionetas).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.menuprincipal).pack(pady=10)

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
            exito = Camionetas.insertar(
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
        registros = Camionetas.consultar()
        
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
            if Camionetas.borrar(id_borrar):
                messagebox.showinfo("Éxito", "Camioneta eliminada")
                self.menu_acciones_camionetas()
            else:
                messagebox.showerror("Error", "No se encontró el ID o hubo un error")

        Button(self.ventana, text="Borrar", command=eliminar_datos).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camionetas).pack(pady=10)


    # ---------------------------------------------------------
    # SECCION CAMIONES (Campos extra: Eje, CapacidadCarga)
    # ---------------------------------------------------------
    def menu_acciones_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Menu Acciones Camiones")
        Label(self.ventana, text="CAMIONES", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Button(self.ventana, text="Insertar Camion", command=self.insertar_camiones).pack(pady=10)
        Button(self.ventana, text="Consultar Camiones", command=self.consultar_camiones).pack(pady=10)
        Button(self.ventana, text="Actualizar Camion", command=self.actualizar_camiones).pack(pady=10)
        Button(self.ventana, text="Borrar Camion", command=self.borrar_camiones).pack(pady=10)

        Button(self.ventana, text="Regresar", command=self.menuprincipal).pack(pady=10)

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

            exito = Camiones.insertar(
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
        registros = Camiones.consultar()
        
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
        
        Label(self.ventana, text="ID a actualizar:").pack(); self.cam_id_upd = Entry(self.ventana); self.cam_id_upd.pack()
        Label(self.ventana, text="Nueva Capacidad:").pack(); self.cam_carga_upd = Entry(self.ventana); self.cam_carga_upd.pack()

        Button(self.ventana, text="Actualizar", command=lambda: messagebox.showinfo("Info", "Actualizar Camion")).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)

    def borrar_camiones(self):
        self.limipia_ventana()
        self.ventana.title("Borrar Camion")
        Label(self.ventana, text="BORRAR CAMION", font=("Times New Roman", 24,"bold")).pack(pady=20)

        Label(self.ventana, text="ID a eliminar:").pack(); self.cam_id_del = Entry(self.ventana); self.cam_id_del.pack()

        def eliminar_camion():
            if Camiones.borrar(self.cam_id_del.get()):
                messagebox.showinfo("Éxito", "Camión eliminado")
                self.menu_acciones_camiones()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el camión")

        Button(self.ventana, text="Borrar", command=eliminar_camion).pack(pady=20)
        Button(self.ventana, text="Regresar", command=self.menu_acciones_camiones).pack(pady=10)