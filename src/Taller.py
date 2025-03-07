def iniciar_taller():
    bienvenida = """
                Bienvenido al sistema de recoleccion de datos de la compañia
                 moto al cien """
    print(bienvenida)

    almacen = ["italika","vento","yamaha", "mv agusta"]

    seguir = True

    while seguir == True:    
        menu = """
                a) Agregar moto
                b) Eliminar moto
                c) Actualizar moto
                d) Mostrar el alamcen
                e) Salir 
                :"""
        opc = input(menu).lower().strip()   

        if opc == "a":
            Nueva_moto = input("que moto deseas agregar al almacen? ").lower().strip()  
            almacen.append(Nueva_moto)
            print(almacen)
        elif opc == "b":
            moto_eliminada = input("¿Que moto desea eliminar? ").lower().strip()  
            if moto_eliminada in almacen:
                almacen.remove(moto_eliminada)
                print(almacen)
            else:
                print("la moto que se desea eliminar no esta dentro de los registros del almacen")

        elif opc == "c":
            Actualizacion = input("¿Que moto deseas actualizar? ").lower().strip()  
            if Actualizacion in almacen:
                index = almacen.index(Actualizacion)
                almacen.pop(index)
                nuevo_dato = input("Introduzca el nuevo dato de la actualizacion: ").lower().strip()  
                almacen.insert(index, nuevo_dato)
                print(almacen)
            else:
                print("el elemento a acutalizar no existe dentro del almacen")

        elif opc == "d":
            i = 0
            while i < len(almacen):
                print(almacen[i])
                i = i+1
        elif opc == "e":
            seguir = False
        else:
            print("el valor introducido no coincide con las opciones dadas")







    