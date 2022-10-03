import menu
from colorama import Fore
from ui import MainWindow

def seleccionar():
   eleccion = int(input(Fore.LIGHTGREEN_EX + "Pulse 1 para ejecutarlo en terminal o 2 para ejecutarlo en interfaz gráfica\n >"))
   if eleccion  == 1:
      menu.iniciar()

   if eleccion == 2:
      app = MainWindow()
      app.mainloop()
seleccionar()