import time
import entradas as en
import comida as co
import cupones as cu
import rutt

def main_menu(rut):
    while True:
        print(f"Bienvenido {rut}")
        print("[1] Comprar entradas")
        print("[2] Comprar comida")
        print("[3] Canjear cupon")
        print("[4] Generar boleta")
        print("[5] Salir")
        op = int(input("Ingrese su opción -> "))
        if op == 1:
            en.entradas(rut)
        elif op == 2:
            co.comida(rut)
        elif op == 3:
            cu.aplicar_descuentos(rut)
        elif op == 4:
            import boleta
            boleta.generar_boleta(rut)
            print("Fin del programa. Gracias por su compra.")
            break
        elif op == 5:
            print("Cerrando Sesión...")
            time.sleep(.5)
            break
        else:
            print("La opción ingresada no es valida.")

def menu():
    rut = rutt.main()
    if not rut:
        return
    main_menu(rut)

menu()
