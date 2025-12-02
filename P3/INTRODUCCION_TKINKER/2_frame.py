from tkinter import *

ventana = Tk()
ventana.title("Uso de frame o Marcos")
ventana.geometry("800x600")

#Marcos o Frame
marco = Frame(ventana,width=300,height=200,bg="silver", border=2, relief=SOLID, )
marco.pack_propagate(False)
marco.pack(pady=200)

marco2 = Frame(marco,width=200,height=100, bg="red", border=2, relief=GROOVE).pack(padx=50,pady=50)


ventana.mainloop()