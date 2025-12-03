from tkinter import messagebox
# Importamos los modelos desde su carpeta 'model'
from model import usuario 
from model import nota

class Controlador:
    @staticmethod
    def registro(nombre, apellidos, email, password):
        resultado = usuario.Usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(icon="info", message=f"{nombre} {apellidos}, se registró correctamente, con el email: {email}", title="Registro Exitoso")
        else:
            messagebox.showinfo(icon="info", message=f"** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...", title="Error")

    @staticmethod
    def inicio_sesion(ventana, email, password):
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(icon="info", message=f".::{registro[1]} {registro[2]}, iniciaste sesión correctamente::.", title="Bienvenido")
            
            # IMPORTACIÓN LOCAL: Hacemos el import aquí dentro para evitar
            # el error de referencia circular (porque view1 ya importa a controlador)
            from view import view1
            
            # Pasamos los datos a la vista de notas
            view1.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
            messagebox.showinfo(icon="info", message=f"** Email y/o contraseña incorrecta ... vuelva a intentarlo **", title="Error")
    
    @staticmethod
    def crear_nota(usuario_id, titulo, descripcion):
        if titulo and descripcion:
            respuesta = nota.Nota.crear(usuario_id, titulo, descripcion)
            Controlador.respuesta_sql(respuesta)
        else:
            messagebox.showwarning("Alerta", "El título y la descripción son obligatorios")

    @staticmethod
    def listar_notas(usuario_id):
        return nota.Nota.mostrar(usuario_id)

    @staticmethod
    def actualizar_nota(id_nota, nuevo_titulo, nueva_descripcion):
        if id_nota and nuevo_titulo and nueva_descripcion:
            respuesta = nota.Nota.actualizar(id_nota, nuevo_titulo, nueva_descripcion)
            Controlador.respuesta_sql(respuesta)
        else:
            messagebox.showwarning("Alerta", "Todos los campos son obligatorios")

    @staticmethod
    def eliminar_nota(id_nota):
        if id_nota:
            respuesta = nota.Nota.eliminar(id_nota)
            Controlador.respuesta_sql(respuesta)
        else:
            messagebox.showwarning("Alerta", "Debes ingresar el ID de la nota")

    @staticmethod
    def respuesta_sql(respuesta):
        if respuesta:
            messagebox.showinfo(icon="info", message="...¡Acción realizada con éxito!...")
        else:
            messagebox.showinfo(icon="info", message="...No fue posible realizar la acción, verifica los datos o vuelve a intentar...")