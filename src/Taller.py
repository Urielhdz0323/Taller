def iniciar_taller():
    bienvenida = """
                Bienvenido al sistema de recoleccion de datos de la compañia
                 moto al cien """
    print(bienvenida)

    almacen = ["italika","vento"]
    menu = """
            a) Agregar moto
            b) Eliminar moto
            c) Actualizar moto
            d) Mostrar el alamcen 
            :"""
    opc = input(menu)   

    if opc == "a":
        Nueva_moto = input("que moto deseas agregar al almacen? ")
        almacen.append(Nueva_moto)
        print(almacen)
    elif opc == "b":
        moto_eliminada = input("¿Que moto desea eliminar? ")
        if moto_eliminada in almacen:
           indice = almacen.remove(moto_eliminada)
           print(almacen)
        else:
            print("la moto que se desea eliminar no esta dentro de los registros del almacen")
    elif opc == "c":
        Actualizacion = input("¿Que moto deseas actualizar? ")
        if Actualizacion in almacen:
            index = almacen.index(Actualizacion)
            almacen.pop(index)
            nuevo_dato = input("Introduzca el nuevo dato de la actualizacion: ")
            almacen.insert(index, nuevo_dato)
            print(almacen)
        else:
            print("el elemento a acutalizar no existe dentro del almacen")






    