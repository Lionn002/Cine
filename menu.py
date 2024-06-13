import time

import entradas as en
import comida as co
import cupones as cu
import cuenta as 

def menu():
    while True:
        print("1.- Comprar entradas")
        print("2.- Comprar comida")
        print("3.- Canjear cupon")
        print("4.- Ingresar cuenta")
        print("4.- Salir")
        op = 0
        op = int(input("Ingrese su opción -> "))
        if op == 1:
            op = 0
            return en.gEntradas()
        elif op == 2:
            op = 0
            return co()
        elif op == 3:
            op = 0
            return cu()
        elif op == 4:
            op = 0
            return es
        elif op == 5:
            op = 0
            print("Cerrando Sesión...")
            time.sleep(.5)
            break
        else:
            print("La opción ingresada no es valida.")
menu()
