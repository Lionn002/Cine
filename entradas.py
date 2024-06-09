import butacas as bu
def entradas(): 
    while True:
        print("Tipos de entradas:")
        print("1.- Entrada 2D - Butaca Tradicional")
        print("VALOR 5700 + IVA")
        print("2.- Entrada 2D - Butaca Dbox")
        print("VALOR 9200 + IVA")
        print("0.- Volver al menu")
        O = int(input("Seleccione su opción -> "))
        if O == 1 or O == 2:
            print("¿Cuantas entradas desea comprar?")
            R = int(input("Ingrese su respuesta -> "))
            return R
        elif O == 0:
            return None
        else: 
            print("Ignrese una opción valida.")
def gEntradas():
    