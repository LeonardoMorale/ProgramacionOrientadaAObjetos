from tkinter import messagebox

def operaciones(n1, n2, signo):
    ope = None
    tipo_ope = ""

    if signo == "+":
        ope = n1 + n2
        tipo_ope = "Suma"
    elif signo == "-":
        ope = n1 - n2
        tipo_ope = "Resta"
    elif signo == "x":
        ope = n1 * n2
        tipo_ope = "Multiplicacion"
    elif signo == "/":
        if n2 == 0:
            messagebox.showerror(
                title="Error de División", 
                message="¡No se puede dividir por cero!"
            )
            return 
        else:
            ope = n1 / n2
            tipo_ope = "Division"
    
    if ope is not None:
        messagebox.showinfo(title=tipo_ope, icon="info", message=f"{n1} {signo} {n2} = {ope}")

# def resultado(tipo,operacion):
#     messagebox.showinfo(title=f"{tipo}", message=f"El resultado de la {tipo} es: {operacion}")

# def suma(n1,n2):
#     tipo = "suma"
#     operacion = n1 + n2
#     resultado(tipo,operacion)

# def resta(n1,n2):    
#     tipo = "resta"
#     operacion = n1 - n2
#     resultado(tipo,operacion)

# def multiplicacion(n1,n2):    
#     tipo = "multiplicacion"
#     operacion = n1 * n2
#     resultado(tipo,operacion)
    
# def division(n1,n2):    
#     if n2 == 0:
#         messagebox.showwarning(message="No se puede dividir entre cero")
#     else:
#         tipo = "division"
#         operacion = n1 / n2
        
#     resultado(tipo,operacion)