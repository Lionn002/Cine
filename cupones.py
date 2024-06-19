
#que el cupon sea aleatorio con minimo de 10 letras y numeros(no pueden ser solamente letras o unicamente numeros(tiene que tener minimo una letra y un numero))

#la parte del codigo linea 5 quizas no se tenga que utilizar ya que tiene que ser aleatorio o almenos que quiera que sea especifico el codigo del cupon

#entre 5 a 30% de descuento puede obtener de los cupones para pagar sus peliculas y comida (tienen que ser diferentes tipos de cupones)
#los cupones tienen limite 1 por dia en la compra total (por persona)
#tendre que importar el inicio de secion de la persona y validar si utilizo un cupon  en 24 horas y si utilizo un cupon, este le diga que no puede utilizar otro cupon 
import csv
import json 
Cuentas = []
ruts = []
#me falta hacer un rut verificador y hacer la opcion 2
def cuenta():
    while True: 
        print ("Ingrese su cuenta de Cinepolis ")
        print("1.-Si tengo una cuenta registrada con mi rut.")
        print("2.-Quiero crear una cuenta con mi rut. ")
        cuenta_registrada = int(input("Ingrese una opción:"))
        if cuenta_registrada == 1: 
            print("------------------------")
            while True:
                rut = input("Ingrese el RUT de la empresa (o 'salir' para terminar): ")
                if rut.lower() == 'salir':
                    break
                nombre = input("Ingrese el nombre de la empresa: ")
                Datos= {"rut": rut, "nombre": nombre}
                Cuentas.append(Datos)
                print(f"Cuenta registrada: {Datos}")

            
cuenta()

    

