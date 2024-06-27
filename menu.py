import time

def menu():
    import entradas as en
    import comida as co
    import cupones as cu
    while True:
        print("[1] Comprar entradas")
        print("[2] Comprar comida")
        print("[3] Canjear cupon")
        print("[4] Salir")
        op = 0
        op = int(input("Ingrese su opción -> "))
        if op == 1:
            op = 0
            return en.entradas()
        elif op == 2:
            op = 0
            return co.comida()
        elif op == 3:
            op = 0
            return cu.aplicar_descuentos()
        elif op == 4:
            op = 0
            print("Cerrando Sesión...")
            time.sleep(.5)
            break
        else:
            print("La opción ingresada no es valida.")

if __name__ == "__main__":
    menu()
