def ingreso():
    """
    Funcion que permite pedir al usuario datos que usaremos en nuestro programa

    Parametros
    --------------------------------------------------------------------------
    No necesitamos ningun parametro

    Retorna
    --------------------------------------------------------------------------
    Retornamos las variables con los datos respectivos

    """
    # Valida hasta que el numero sea correcto
    while True:
        # permite capturar errores
        try:
            radio = int(input("Ingrese radio de la circunferencia:\n"))
            if radio > 0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return radio


def area(radio, pi):
    """
    Funcion que calcula el area de una circunferencia

    Parametro
    --------------------------------------------------
    Radio y la contante pi 


    Retorna
    --------------------------------------------------
    area de un ciruculo
    """
    # calculamos y devolvemos el resultado

    return pi*(radio**2)


def hacerNuevamente():
    """
    Funcion que permite saber si repetimos o no las operaciones

    Parametros
    ----------------------------------------------------------
    no necesitamos ningun parametro

    Retorna
    ----------------------------------------------------------
    Retorna un False si  desea repetir y un True si no quiere repetir

    """
    # Pedimos datos que nos servira ver que opcion quiere hacer
    opc = input("Ingresar otros Datos?\n 1.-Si\n Cualquier Tecla.-No\n")
    # comprobamos las opciones
    if opc == '1':
        # retornamos un falso si desea repetir
        return False
    # retornamos un verdadero si no desea repetir
    return True


if __name__ == "__main__":
    # Declaracion de variables
    radio = 0
    pi = 3.1415
    result = 0
    #repetir operacion
    while True:
        #ingreso de datos por usuario
        radio = ingreso()
        #calculo de area 
        result = area(radio, pi)
        #mostrar por pantalla resultado
        print("El area de la circunferencia de radio {} es {}".format(radio, result))
        #pregunta si repite si o no
        if hacerNuevamente():
            break
