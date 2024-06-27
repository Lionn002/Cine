def seleccionar_metodo_pago(total):
    while True:
        print("Seleccione el método de pago:")
        print("[1] Tarjeta")
        print("[2] Efectivo")
        metodo = int(input("Ingrese su opción: "))
        
        if metodo == 1:
            pagar_con_tarjeta(total)
            break
        elif metodo == 2:
            pagar_con_efectivo(total)
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def pagar_con_tarjeta(total):
    numero_tarjeta = input("Ingrese el número de la tarjeta: ")
    contrasena = input("Ingrese la contraseña: ")
    print(f"Pago de ${total:.2f} realizado con tarjeta {numero_tarjeta[-4:]}.")
    print("¡Gracias por su compra!")

def pagar_con_efectivo(total):
    billetes = [20000, 10000, 5000, 2000, 1000]
    monto_pagado = 0
    
    print("Ingrese los billetes que va a utilizar para el pago:")
    while monto_pagado < total:
        print(f"Total a pagar: ${total:.2f}")
        print(f"Monto pagado hasta ahora: ${monto_pagado:.2f}")
        for i, billete in enumerate(billetes):
            print(f"[{i+1}] ${billete}")
        print("[0] Terminar pago")
        
        opcion = int(input("Seleccione una opción: "))
        if opcion == 0:
            break
        elif 1 <= opcion <= len(billetes):
            monto_pagado += billetes[opcion-1]
        else:
            print("Opción no válida. Intente nuevamente.")
    
    if monto_pagado >= total:
        vuelto = monto_pagado - total
        print(f"Pago de ${total:.2f} realizado con efectivo.")
        print(f"Vuelto: ${vuelto:.2f}")
    else:
        print("No se ha pagado el monto total. Por favor, intente nuevamente.")

if __name__ == "__main__":
    total = float(input("Ingrese el total a pagar: "))
    seleccionar_metodo_pago(total)
