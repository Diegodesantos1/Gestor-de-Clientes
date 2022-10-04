import sys

DATABASE_PATH = "./gestor/clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "./gestor/test/clientes_test.csv"