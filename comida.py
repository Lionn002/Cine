op = 0
while op != 3:
    print("2.- Comida")
    print("3.- Salir")
    op = int(input("--Ingrese una opcion--> "))
    #iniciando el menu 
    if op == 2:
        while op != 4: #opciones del menu
            print("1.- Pizza")
            print("2.- Hamburguesa")
            print("3.- Palomitas")
            print("4.- Salir")
            op = int(input("Ingrese una opcion de comida: "))
            if op == 1:
               while op != 4: #menu de la pizza
                   print ("1.-Pizza Chica")
                   pc = 3500
                   print ("2.-Pizza Mediana")
                   print ("3.-Pizza Grande")
                   print ("4.-Salir")
                   op = int(input("Escoja el tamaño de la pizza: "))
                   if op == 1:
                       while op != 5: #el tamaño de la pizza 
                           print ("1.-Pizza Napolitana Chica")
                           pc1 = pc + 1500
                           print ("2.-Pizza Española Chica")
                           pc2 = pc + 1800
                           print ("3.-Pizza Vegetariana chica")
                           pc3 = pc + 1300
                           print ("4.-Cree su pizza chica")
                           print ("5.-Salir")
                           op = int(input("Ingrese la opcion deseada: "))
                           if op == 1:
                               print("El valor de su Pizza Napolitana: ", pc1)
                           elif op == 2:
                               print ("El valor de su Pizza Española: ",pc2) 
                           elif op == 3:
                               print ("El valor de su Pizza Vegetariana: ",pc3)
                           elif op == 4:
                               while op != 7:
                                   print ("1.-Choclo")
                                   print ("2.-Queso")
                                   print ("3.-Champiñon")
                                   print ("4.-Carne")
                                   print ("5.-Piña")
                                   print ("6.-pimenton")
                                   print ("7.-Salir")
                                   op = int(input("Ingrese sus ingredientes: "))
                                   
