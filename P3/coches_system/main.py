from view.menu_principal import MenuPrincipal
from tkinter import *

class App:
    @staticmethod
    def main(ventana):
        view=MenuPrincipal(ventana)

if __name__ == "__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()
