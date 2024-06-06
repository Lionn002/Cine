import time

import entradas as en
import comida as co
import cupones as cu

def menu():
    while True:
        print("1.- Comprar entradas")
        print("2.- Comprar comida")
        print("3.- Canjear cupon")
        print("4.- Salir")
        op = int(input("Ingrese su opción -> "))
        if op == 1:
            return en()
        elif op == 2:
            return co()
        elif op == 3:
            return cu()
        elif op == 4:
            print("Cerrando Sesión...")
            time.sleep(.5)
            break
        else:
            print("La opción ingresada no es valida.")

