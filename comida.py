compras_comida = []

def comida(rut):
    total_compra = 0 
    while True:
        print("*** MENU COMIDA ***")
        print("1.- Golosinas")
        print("2.- Bebidas")
        print("3.- Cabritas")
        print("4.- Carrito")
        print("5.- Salir")
        op_principal = int(input("Ingrese una opción de comida: "))
        
        if op_principal == 5:
            print("!!!! GRACIAS POR USAR EL MENU DE COMIDAS !!!!")
            compras_comida.append((rut, total_compra))
            return

        if op_principal == 1:
            total_compra = menu_golosinas(total_compra)
        elif op_principal == 2:
            total_compra = menu_bebidas(total_compra)
        elif op_principal == 3:
            total_compra = menu_cabritas(total_compra)
        elif op_principal == 4:
            print("!!!!! ESTE ES SU CARRITO !!!!!")
            print(f"El total de su compra es: {total_compra}")
        else:
            print("La opción ingresada no es válida")

def menu_golosinas(total_compra):
    while True:
        print("*** MENU GOLOSINAS ***")
        print("1.- Papas fritas")
        print("2.- Alfajor")
        print("3.- Panqueque")
        print("4.- Salir")
        op_golosina = int(input("Escoja una golosina: "))
        
        if op_golosina == 4:
            break
        
        if op_golosina == 1:
            total_compra = sub_menu_papas(total_compra)
        elif op_golosina == 2:
            total_compra = sub_menu_alfajor(total_compra)
        elif op_golosina == 3:
            total_compra = sub_menu_panqueque(total_compra)
        else:
            print("La opción ingresada no es válida")
    return total_compra

def sub_menu_papas(total_compra):
    while True:
        print("1.- Papas fritas M - $1990")
        print("2.- Papas fritas L - $2890")
        print("3.- Papas fritas XL - $3500")
        print("4.- Salir")
        op_papas = int(input("Ingrese la opción deseada: "))
        
        if op_papas == 4:
            break
        
        if op_papas in [1, 2, 3]:
            precios = [1990, 2890, 3500]
            total_compra += precios[op_papas - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es válida")
    return total_compra

def sub_menu_alfajor(total_compra):
    while True:
        print("1.- Alfajor de Manjar - $1690")
        print("2.- Alfajor de Frambuesa - $1790")
        print("3.- Alfajor de Chocolate - $1790")
        print("4.- Salir")
        op_alfajor = int(input("Ingrese una opción: "))
        
        if op_alfajor == 4:
            break
        
        if op_alfajor in [1, 2, 3]:
            precios = [1690, 1790, 1790]
            total_compra += precios[op_alfajor - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es válida")
    return total_compra

def sub_menu_panqueque(total_compra):
    while True:
        print("1.- Panqueque de manjar - $1190")
        print("2.- Panqueque de manjar y helado - $1790")
        print("3.- Panqueque papayero - $990")
        print("4.- Salir")
        op_panqueque = int(input("Ingrese una opcion: "))

        if op_panqueque == 4:
            break
        
        if op_panqueque in [1, 2, 3]:
            precios = [1190, 1790, 990]
            total_compra += precios[op_panqueque - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es válida")
    return total_compra

def menu_bebidas(total_compra):
    while True:
        print("*** MENU BEBIDAS ***")
        print("1.- Fanta")
        print("2.- Coca-Cola")
        print("3.- Agua Gasificada")
        print("4.- Salir")
        op_bebidas = int(input("Escoja una Bebida: "))

        if op_bebidas == 4:
            break
        
        if op_bebidas == 1:
            total_compra = sub_menu_fanta(total_compra)
        elif op_bebidas == 2:
            total_compra = sub_menu_coca(total_compra)
        elif op_bebidas == 3:
            total_compra = sub_menu_agua(total_compra)
        else:
            print("La opción ingresada no es válida")
    return total_compra

def sub_menu_fanta(total_compra):
    while True:
        print("1.- Bebida Fanta de lata - $990")
        print("2.- Bebida Fanta de 250 ml - $450")
        print("3.- Bebida Fanta de 600 ml - $1290")
        print("4.- Salir")
        op_fanta = int(input("Escoja una opcion: "))
        if op_fanta == 4:
            break

        if op_fanta in [1, 2, 3]:
            precios = [990, 450, 1290]
            total_compra += precios[op_fanta - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción seleccionada no es valida")
    return total_compra

def sub_menu_coca(total_compra):
    while True:
        print("1.- Bebida Coca-Cola de lata - $990")
        print("2.- Bebida Coca-Cola de 250 ml - $450")
        print("3.- Bebida Coca-Cola de 600 ml - $1290")
        print("4.- Salir")
        op_coca = int(input("Escoja una opcion: "))
        if op_coca == 4:
            break 

        if op_coca in [1, 2, 3]:
            precios = [990, 450, 1290]
            total_compra += precios[op_coca - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción seleccionada no es valida")
    return total_compra

def sub_menu_agua(total_compra):
    while True:
        print("1.- Agua gasificada Benedictino 500ml - $1090")
        print("2.- Agua gasificada Cachantun 500ml - $990")
        print("3.- Agua gasificada Peyehue 500ml - $1190")
        print("4.- Salir")
        op_agua= int(input("Escoja una opcion: "))
        if op_agua == 4:
            break
        if op_agua in [1, 2, 3]:
            precios = [1090, 990, 1190]
            total_compra += precios[op_agua - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es valida")
    return total_compra

def menu_cabritas(total_compra):
    while True:
        print("*** MENU CABRITAS ***")
        print("1.- Cabritas con Mantequilla")
        print("2.- Cabritas con Chocolate")
        print("3.- Cabritas con Dulce")
        print("4.- Salir")
        op_cabritas = int(input("Escoja su sabor favorito: "))
        if op_cabritas == 4:
            break
        if op_cabritas == 1:
            total_compra = sub_menu_mantequilla(total_compra)
        elif op_cabritas == 2:
            total_compra = sub_menu_chocolate(total_compra)
        elif op_cabritas == 3:
            total_compra = sub_menu_dulce(total_compra)
        else:
            print("La opción ingresada no es valida")
    return total_compra

def sub_menu_mantequilla(total_compra):
    while True:
        print("1.- Cabritas con Mantequilla M - $4990")
        print("2.- Cabritas con Mantequilla L - $6290")
        print("3.- Cabritas con Mantequilla XL - $7990")
        print("4.- Salir")
        op_mantequilla= int(input("Escoja el tamaño: "))
        if op_mantequilla == 4:
            break
        if op_mantequilla in [1, 2, 3]:
            precios = [4990, 6290, 7990]
            total_compra += precios[op_mantequilla - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es valida")
    return total_compra

def sub_menu_chocolate(total_compra):
    while True:
        print("1.- Cabritas con Chocolate M - $5390")
        print("2.- Cabritas con Chocolate L - $6790")
        print("3.- Cabritas con Chocolate XL - $7990")
        print("4.- Salir")
        op_chocolate = int(input("Escoja una opcion: "))
        if op_chocolate == 4:
            break 
        if op_chocolate in [1, 2, 3]:
            precios = [5390, 6790, 7990]
            total_compra += precios[op_chocolate - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es valida")
    return total_compra

def sub_menu_dulce(total_compra):
    while True:
        print("1.- Cabritas con Dulce M - $5990")
        print("2.- Cabritas con Dulce L - $7190")
        print("3.- Cabritas con Dulce XL - $8990")
        print("4.- Salir")
        op_dulce = int(input("Ingrese una opcion: "))
        if op_dulce == 4:
            break
        if op_dulce in [1, 2, 3]:
            precios = [5990, 7190, 8990]
            total_compra += precios[op_dulce - 1]
            print(f"El total a pagar es: {total_compra}")
        else:
            print("La opción ingresada no es valida")
    return total_compra
