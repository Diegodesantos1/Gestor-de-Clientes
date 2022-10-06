<h1 align="center">Evaluación Inicial</h1>

En este [repositorio](https://github.com/Diegodesantos1/Gestor-de-Clientes) queda resueltoel ejercicio del gestor de clientes.
Así queda el código organizado en la carpeta gestor con el archivo run.py fuera de ese directorio accediendo a todo y ejecutando el programa, además los test pasan correctamente.

***

![image](https://user-images.githubusercontent.com/91721855/194379648-e260227d-78ad-47bd-bb15-d90334d6f304.png)

<h2 align="center">Código del run</h2>

```python
import sys
import pathlib
sys.path.append(str(pathlib.Path().resolve()) + './gestor')
sys.path.append
import menu
from colorama import Fore
from ui import MainWindow

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
   else:
      seleccionar()
seleccionar()
```

***

<h2 align="center">Código de los test</h2>

El programa pasa los test correctamente:

![image](https://user-images.githubusercontent.com/91721855/194380735-913f6e60-d721-4044-84d8-fc3da82c0b29.png)

```python
pytest -v
```

![image](https://user-images.githubusercontent.com/91721855/194380877-3d654220-974b-4807-8c0f-5253e8a27f53.png)

```python
import csv
import copy
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_inexistente = db.Clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('28Z'))
        cliente_modificado = db.Clientes.modificar('28Z', 'Mariana', 'García')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('48H')
        cliente_rebuscado = db.Clientes.buscar('48H')
        self.assertEqual(cliente_borrado.dni, '48H')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('232323S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'García')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'García')

if __name__ == '__main__':
    unittest.main()
```
