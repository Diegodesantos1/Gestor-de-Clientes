import menu as menu
from colorama import Fore
from ui import MainWindow
import test.test_database as TD

def seleccionar():
   eleccion = int(input(Fore.LIGHTGREEN_EX + "\n Bienvenido al menú de selección: \n\n Pulse 1 para ejecutarlo en terminal \n Pulse 2 para ejecutarlo en interfaz gráfica\n > " + Fore.RESET))
   if eleccion  == 1:
      menu.iniciar()

   if eleccion == 2:
      app = MainWindow()
      app.mainloop()
   if eleccion != 1 and eleccion != 2:
      print(Fore.RED + "Error, seleccione una opción válida" + Fore.RESET)
      seleccionar()
seleccionar()