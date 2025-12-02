import tkinter as tk
from controller import funciones
from tkinter import ttk

class Vista:
    def __init__(self, window):
        window.title("Calculadora POO")
        window.geometry("500x600") 
        window.resizable(False, False)
        window.config(bg="#f0f0f0") 
        Vista.interfaz_principal(window)
    
    @staticmethod
    def borrarPantalla(window):
        for widget in window.winfo_children():
            if widget != window.nametowidget(window.cget("menu")):
                widget.destroy()
    
    @staticmethod
    def menuPrincipal(window):
        menubar = tk.Menu(window)
        window.config(menu=menubar)
        menu_operaciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=menu_operaciones)
        menu_operaciones.add_command(label="Agregar (Inicio)", command=lambda:Vista.interfaz_principal(window))
        menu_operaciones.add_command(label="Consultar Registros", command=lambda:Vista.interfazConsultar(window))
        menu_operaciones.add_command(label="Modificar Registro", command=lambda:Vista.consultarActualizar(window))
        menu_operaciones.add_command(label="Eliminar Registro", command=lambda:Vista.interfazBorrar(window))
        menu_operaciones.add_separator()
        menu_operaciones.add_command(label="Salir", command=window.quit)
    
    @staticmethod
    def estilo_boton(padre, texto, comando, color_bg="#37474f"):
        return tk.Button(padre, text=texto, command=comando, 
                         bg=color_bg, fg="white", font=("Arial", 10, "bold"),
                         relief="raised", bd=3, cursor="hand2")

    @staticmethod
    def interfaz_principal(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        lbl_titulo = tk.Label(window, text="Nueva Operación", bg="#f0f0f0", font=("Verdana", 14, "bold"), fg="#333")
        lbl_titulo.pack(pady=20)

        frame_valores = tk.Frame(window, bg="white", bd=2, relief="groove")
        frame_valores.pack(pady=10, padx=20, ipadx=10, ipady=10)
        
        lbl_1 = tk.Label(frame_valores, text="Primer número:", bg="white", font=("Verdana", 10))
        lbl_1.grid(column=0, row=0, padx=15, pady=15, sticky="e")
        
        lbl_2 = tk.Label(frame_valores, text="Segundo número:", bg="white", font=("Verdana", 10))
        lbl_2.grid(column=0, row=1, padx=15, pady=15, sticky="e")
        
        num1 = tk.IntVar()
        num2 = tk.IntVar()
        
        entry_1 = tk.Entry(frame_valores, textvariable=num1, justify="right", font=("Arial", 12), bg="#ecf0f1")
        entry_1.focus()
        entry_1.grid(column=1, row=0, padx=15, pady=10)
        
        entry_2 = tk.Entry(frame_valores, textvariable=num2, justify="right", font=("Arial", 12), bg="#ecf0f1")
        entry_2.grid(column=1, row=1, padx=15, pady=10)
        
        frame_botones = tk.Frame(window, bg="#f0f0f0")
        frame_botones.pack(pady=30)
        
        btn_suma = Vista.estilo_boton(frame_botones, " + ", lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "+"))
        btn_suma.grid(row=0, column=0, padx=10, ipadx=10)
        
        btn_resta = Vista.estilo_boton(frame_botones, " - ", lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "-"))
        btn_resta.grid(row=0, column=1, padx=10, ipadx=10)
        
        btn_div = Vista.estilo_boton(frame_botones, " / ", lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "/"))
        btn_div.grid(row=0, column=2, padx=10, ipadx=10)
        
        btn_mult = Vista.estilo_boton(frame_botones, " x ", lambda:funciones.Funciones.operaciones(num1.get(), num2.get(), "x"))
        btn_mult.grid(row=0, column=3, padx=10, ipadx=10)
        
        btn_salir = tk.Button(window, text="Cerrar Aplicación", command=window.quit, bg="#c0392b", fg="white", relief="flat")
        btn_salir.pack(side="bottom", pady=20)

    @staticmethod
    def interfazBorrar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        tk.Label(window, text="Eliminar Registro", font=("Verdana", 14, "bold"), bg="#f0f0f0").pack(pady=20)
        
        frame_b = tk.Frame(window, bg="white", bd=2, relief="groove")
        frame_b.pack(pady=10, ipadx=20, ipady=20)

        tk.Label(frame_b, text="ID de la Operación a borrar:", bg="white", font=("Verdana", 10)).pack(pady=5)
        
        id = tk.IntVar()
        entry_1 = tk.Entry(frame_b, textvariable=id, justify="center", font=("Arial", 12), bg="#ecf0f1")
        entry_1.focus()
        entry_1.pack(pady=10)
        
        Vista.estilo_boton(window, "Eliminar", lambda:funciones.Funciones.borrar(id.get()), "#c0392b").pack(pady=10)
        tk.Button(window, text="Volver al inicio", command=lambda:Vista.interfaz_principal(window)).pack(pady=5)
    
    @staticmethod
    def interfazConsultar(window):
        Vista.borrarPantalla(window)
        Vista.menuPrincipal(window)
        
        lbl_titulo = tk.Label(window, text="Historial de Operaciones", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2c3e50")
        lbl_titulo.pack(pady=15)
        
        frame_listado = tk.Frame(window, bg="white", bd=1, relief="sunken")
        frame_listado.pack(fill="both", expand=True, padx=40, pady=10)

        registros = funciones.Funciones.consultar()
        cadena=""
        contador=1
        
        header = f"{'#':<5} {'ID':<5} {'FECHA':<20} {'DETALLE'}"
        cadena += header + "\n" + ("-"*60) + "\n"

        if registros:
            for registro in registros:
                detalle = f"{registro[2]} {registro[4]} {registro[3]} = {registro[5]}"
                cadena += f"{contador:<5} {registro[0]:<5} {str(registro[1])[:10]:<20} {detalle}\n"
                contador+=1
        else:
            cadena = "No hay registros disponibles."

        lbl_registros = tk.Label(frame_listado, text=cadena, justify="left", font=("Courier New", 9), bg="white", anchor="nw")
        lbl_registros.pack(fill="both", expand=True, padx=10, pady=10)
        
        btn_volver = tk.Button(window, text="Volver", command=lambda:Vista.interfaz_principal(window))
        btn_volver.pack(pady=20)

    @staticmethod
    def consultarActualizar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        
        tk.Label(ventana, text="Modificar Operación", font=("Verdana", 14, "bold"), bg="#f0f0f0").pack(pady=20)
        
        frame_c = tk.Frame(ventana, bg="white", bd=2, relief="groove")
        frame_c.pack(pady=10, ipadx=20, ipady=20)

        tk.Label(frame_c, text="Ingrese ID a buscar:", bg="white", font=("Verdana", 10)).pack(pady=5)
        
        id=tk.IntVar()
        caja0=tk.Entry(frame_c, textvariable=id, width=10, justify="center", font=("Arial", 12), bg="#ecf0f1")
        caja0.focus()
        caja0.pack(pady=10)
        
        Vista.estilo_boton(ventana, "Buscar ID", lambda:funciones.Funciones.consultar_id(ventana,id.get())).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=lambda:Vista.interfaz_principal(ventana)).pack(pady=10)
    
    @staticmethod
    def interfazAcualizar(ventana, registro):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        
        registro_id = registro[0]
        id_v = registro_id[0]
        num1_v = registro_id[2]
        num2_v = registro_id[3]
        simb_v = registro_id[4]
        res_v = registro_id[5]

        tk.Label(ventana, text="Editando Registro", font=("Verdana", 14, "bold"), bg="#f0f0f0").pack(pady=15)

        frame_edit = tk.Frame(ventana, bg="white", bd=2, relief="groove")
        frame_edit.pack(pady=10, padx=20, ipadx=20, ipady=10)

        tk.Label(frame_edit, text="ID Operación:", bg="white", fg="gray").pack()
        caja0=tk.Entry(frame_edit, width=5, justify="center", disabledbackground="#ddd")
        caja0.insert(0,id_v)
        caja0.config(state="readonly")
        caja0.pack(pady=(0, 10))

        f_campos = tk.Frame(frame_edit, bg="white")
        f_campos.pack()

        tk.Label(f_campos, text="Núm 1:", bg="white").grid(row=0, column=0, padx=5, pady=5)
        caja1=tk.Entry(f_campos, width=8, justify="right", bg="#ecf0f1")
        caja1.insert(0, num1_v)
        caja1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(f_campos, text="Núm 2:", bg="white").grid(row=1, column=0, padx=5, pady=5)
        caja2=tk.Entry(f_campos, width=8, justify="right", bg="#ecf0f1")
        caja2.insert(0, num2_v)
        caja2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(f_campos, text="Signo:", bg="white").grid(row=2, column=0, padx=5, pady=5)
        caja3=tk.Entry(f_campos, width=4, justify="center", bg="#ecf0f1")
        caja3.insert(0, simb_v)
        caja3.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(f_campos, text="Result:", bg="white").grid(row=3, column=0, padx=5, pady=5)
        caja4=tk.Entry(f_campos, width=8, justify="right", bg="#ecf0f1")
        caja4.insert(0, res_v)
        caja4.grid(row=3, column=1, padx=5, pady=5)

        Vista.estilo_boton(ventana, "Guardar Cambios", 
                           lambda:funciones.Funciones.actualizar(caja1.get(),caja2.get(),caja3.get(),caja4.get(),caja0.get()), 
                           "#27ae60").pack(pady=15)
                           
        tk.Button(ventana, text="Cancelar", command=lambda:Vista.interfaz_principal(ventana)).pack(pady=5)