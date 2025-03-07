def iniciar_taller():
    bienvenida = """
                Bienvenido al sistema de recoleccion de datos de la compañia
                 moto al cien """
    print(bienvenida)

    almacen = []
    menu = """"
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


