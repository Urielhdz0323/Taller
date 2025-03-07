def iniciar_taller():
    bienvenida = """
                Bienvenido al sistema de recoleccion de datos de la compañia
                 moto al cien """
    print(bienvenida)

    almacen = ["italika"]
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
            almacen.index(moto_eliminada)
            print(moto_eliminada,"fue eliminada con existo")
        else:
            print("la moto que se desea eliminar no esta dentro de los registros del almacen")




