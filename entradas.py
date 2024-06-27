import butacas as bu
import time as t


def entradas(): 
    import rutt
    while True:
        print("Seleccione la pelicula\n")
        print("[1] El planeta de los simios: Nuevo reino")
        print("[2] Bad Boys: Hasta la muerte")
        print("[3] Observados")
        print("[4] Garfield: Fuera de casa")
        print("[5] Inmaculada")
        print("[6] Salir")
        opcion = int(input("Ingrese su opcion -> "))
        if opcion == 1:
            print("""ENTRADA 2D - BUTACA TRADICIONAL
                  VALOR: $5.500 + IVA""")
            op = "El planeta de los simios: Nuevo reino"
            print("¿Cuantas entradas desea comprar?")
            en = int(input("Ingrese su respuesta: "))
            val = 5500
            iva = val * 0.19 * en
            total = val * en + iva
            return asientos(op, en, val, iva, total)
        elif opcion == 2:
            print("""ENTRADA 2D - SALDA XD
                  VALOR: $6.500 + IVA
                  
                  ENTRADA 2D - BUTACADA DBOX
                  VALOR: $8.900 + IVA""")
            print("""¿Que tipo de entrada desea comprar?
                  [1] Butaca Normal
                  [2] Butaca Dbox""")
            op = "Bad Boys: Hasta la muerte"
            sel = int(input("Ingrese su opción: "))
            while True:
                if sel == 1:
                    print("¿Cuantas entradas desea comprar?")
                    en = int(input("Ingrese su respuesta: "))
                    val = 6500
                    break
                elif sel == 2:
                    print("¿Cuantas entradas desea comprar?")
                    en = int(input("Ingrese su respuesta: "))
                    val = 8900
                    break
                else: 
                    print("Ingrese una opción valida")
            iva = val * 0.19 * en
            total = val * en + iva
            return asientos(op, en, val, iva, total)
        elif opcion == 3:
            print("""ENTRADA 2D - BUTACA TRADICIONAL
                  VALOR: $5.500 + IVA""")
            op = "Observados"
            print("¿Cuantas entradas desea comprar?")
            en = int(input("Ingrese su respuesta: "))
            val = 5500
            iva = val * 0.19 * en
            total = val * en + iva
            return asientos(op, en, val, iva, total)
        elif opcion == 4:
            print("""ENTRADA 2D - BUTACA TRADICIONAL
                  VALOR: $5.500 + IVA
                  
                  ENTRADA 2D - BUTACA DBOX
                  VALOR: $8.900 + IVA""")
            print("""¿Que tipo de entrada desea comprar?
                  [1] Butaca Normal
                  [2] Butaca Dbox""")
            op = "Garfield: Fuera de casa"
            sel = int(input("Ingrese su opción: "))
            while True:
                if sel == 1:
                    print("¿Cuantas entradas desea comprar?")
                    en = int(input("Ingrese su respuesta: "))
                    val = 5500
                    break
                elif sel == 2:
                    print("¿Cuantas entradas desea comprar?")
                    en = int(input("Ingrese su respuesta: "))
                    val = 8900
                    break
                else: 
                    print("Ingrese una opción valida")
            iva = val * 0.19 * en
            total = val * en + iva
            return asientos(op, en, val, iva, total)
        elif opcion == 5:
            print("""ENTRADA 2D - BUTACA TRADICIONAL
                  VALOR: $5.500 + IVA""")
            op = "Inmaculada"
            print("¿Cuantas entradas desea comprar?")
            en = int(input("Ingrese su respuesta: "))
            val = 5500
            iva = val * 0.19 * en
            total = val * en + iva
            return asientos(op, en, val, iva, total)
        elif opcion == 6:
            print("Volviendo al menu principal")
            return None
        else:
            print("Ingrese una opcion valida.")
    

def asientos(op, en, val, iva, total):
    print("Usted esta comprando ", en, " entradas para la pelicula:", op)
    print("El subtotal de la compra es: $", val * en)
    print("El IVA de esta compra es de: $", iva)
    print("El total de la compra de boletos es de: $", total)
    print("Sera redirigido para elegir su/s butacas, las butacas marcadas con 'X' estan ocupadas, y marcadas con 'O' las desocupadas, el formato para elegir una butaca es: A(letra), 1(numero)")
    t.sleep(5)
    filas = 7
    columnas = 7
    butacas = bu.mapa_butacas(filas, columnas)
    butacas = bu.seleccionar_butacas(butacas, en)
    print("Mapa final de butacas:")
    bu.mostrar_mapa(butacas)

