import tkinter as tk
from tkinter import messagebox
from model import operaciones
from view import interfaz

class Funciones:
    @staticmethod
    def respuesta(respuesta):
        if respuesta:
            messagebox.showinfo(title="Exito", message="Se ha realizado la operacion correctamente.")
        else:
            messagebox.showinfo(title="Error", message="Ha ocurrido un error al realizar la operacion")
    
    @staticmethod
    def operaciones(num1, num2, simbolo):
        if simbolo == "+":
            op = num1 + num2
            tipo = "SUMA"
        elif simbolo == "-":
            op = num1 - num2
            tipo = "RESTA"
        elif simbolo == "x":
            op = num1 * num2
            tipo = "MULTIPLICACION"
        elif simbolo == "/":
            if num2 == 0:
                messagebox.showerror(message="No se puede dividir entre 0")
                op = "ERROR"
            else:
                op = num1 / num2
                tipo = "DIVISION"
        if op == "ERROR":
            pass
        else:
            resultado=messagebox.askquestion(message=f"{num1} {simbolo} {num2} = {op}\n\n¿Deseas guardar en la base de datos?",icon="question", title=tipo)
            if resultado=="yes":
                respuesta = operaciones.Operaciones.insertar(num1, num2, simbolo, op)
                Funciones.respuesta(respuesta)    
    @staticmethod
    def borrar(id):
        respuesta = operaciones.Operaciones.eliminar(id)
        Funciones.respuesta(respuesta)

    @staticmethod
    def actualizar(num1, num2, signo, resultado, id):
        respuesta = operaciones.Operaciones.actualizar(num1, num2, signo, resultado, id)
        Funciones.respuesta(respuesta)
    
    @staticmethod
    def consultar_id(ventana, id):
        registro = operaciones.Operaciones.consultar_id(id)
        if len(registro) > 0:
            interfaz.Vista.interfazAcualizar(ventana, registro)
        else:
            messagebox.showinfo(title="Error", message="No se encuentra ese id")

    @staticmethod
    def consultar():
        registros = operaciones.Operaciones.consultar()
        if len(registros) > 0:
            return registros
        else:
            messagebox.showinfo(title="Error", message="Ha ocurrido un error al realizar la operacion")