import butacas as bu
import time as t

compras_entradas = []

def entradas(rut): 
    while True:
        print("Seleccione la pelicula\n")
        print("[1] El planeta de los simios: Nuevo reino")
        print("[2] Bad Boys: Hasta la muerte")
        print("[3] Observados")
        print("[4] Garfield: Fuera de casa")
        print("[5] Inmaculada")
        print("[6] Salir")
        opcion = int(input("Ingrese su opcion -> "))
        if opcion == 6:
            print("Volviendo al menu principal")
            return None

        peliculas = [
            ("El planeta de los simios: Nuevo reino", 5500),
            ("Bad Boys: Hasta la muerte - Normal", 6500),
            ("Bad Boys: Hasta la muerte - DBOX", 8900),
            ("Observados", 5500),
            ("Garfield: Fuera de casa - Normal", 5500),
            ("Garfield: Fuera de casa - DBOX", 8900),
            ("Inmaculada", 5500)
        ]

        if opcion in [1, 3, 5]:
            pelicula, val = peliculas[(opcion - 1) * 2]
            print(f"ENTRADA 2D - BUTACA TRADICIONAL\nVALOR: ${val} + IVA")
            en = int(input("¿Cuantas entradas desea comprar? "))
        elif opcion in [2, 4]:
            print(f"ENTRADA 2D - SALA XD\nVALOR: ${peliculas[(opcion - 1) * 2][1]} + IVA")
            print("¿Que tipo de entrada desea comprar?\n[1] Butaca Normal\n[2] Butaca DBOX")
            tipo = int(input("Ingrese su opción: "))
            if tipo == 1:
                pelicula, val = peliculas[(opcion - 1) * 2]
            elif tipo == 2:
                pelicula, val = peliculas[(opcion - 1) * 2 + 1]
            else:
                print("Opción no válida. Intente nuevamente.")
                continue
            en = int(input("¿Cuantas entradas desea comprar? "))
        else:
            print("Opción no válida. Intente nuevamente.")
            continue

        iva = val * 0.19 * en
        total = val * en + iva
        asientos(pelicula, en, val, iva, total)
        compras_entradas.append((rut, pelicula, en, val, iva, total))
        return

def asientos(op, en, val, iva, total):
    print(f"Usted esta comprando {en} entradas para la pelicula: {op}")
    print(f"El subtotal de la compra es: ${val * en}")
    print(f"El IVA de esta compra es de: ${iva}")
    print(f"El total de la compra de boletos es de: ${total}")
    print("Sera redirigido para elegir su/s butacas, las butacas marcadas con 'X' estan ocupadas, y marcadas con 'O' las desocupadas, el formato para elegir una butaca es: A(letra), 1(numero)")
    t.sleep(5)
    filas = 7
    columnas = 7
    butacas = bu.mapa_butacas(filas, columnas)
    butacas = bu.seleccionar_butacas(butacas, en)
    print("Mapa final de butacas:")
    bu.mostrar_mapa(butacas)
