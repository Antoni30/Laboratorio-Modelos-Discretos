def ingresar():
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
            #ingreso de datos por teclado
            print("Si no conoce el dato coloque 0")
            distancia = int(input("Ingresar distancia:\n"))
            tiempo = int(input("Ingresa el tiempo:\n"))
            velocidad = int(input("Ingresar la velocidad:\n"))
            #rangos establecidos de las variables
            if distancia >= 0 and tiempo >= 0 and velocidad >= 0:
                break
            else:
                print("Alguno de los datos esta fuera de los rangos establecidos")
            # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        # Retorna los datos ya ingresados por el usuario
    return distancia, tiempo, velocidad


def calcularVelocidad(distancia, tiempo):
    """
    Funcion para calcular la Velocidad

    Parametro
    -----------------------------------------------
    Distancia y Tiempo

    Retorna
    -------------------------------------------------
    Calculo de la velocidad
    """

    return distancia / tiempo


def calcularDistancia(velocidad, tiempo):
    """
    Funcion para calcular la distancia

    Parametro
    -----------------------------------------------
    velocidad y Tiempo

    Retorna
    -------------------------------------------------
    Calculo de la distancia
    """
    # Calculo del la distancia
    return velocidad * tiempo


def calcularTiempo(distancia, velocidad):
    """
    Funcion para calcular el tiempo

    Parametro
    -----------------------------------------------
    distancia y velocidad

    Retorna
    -------------------------------------------------
    Calculo del tiempo
    """
    # Calculo del la distancia
    return distancia / velocidad


def calcular(distancia, tiempo, velocidad):
    """
    Funcion que calcula las variables desconocidos

    Parametros
    -------------------------------------------------------
    distancia, tiempo y la velocidad

    Retorna
    ------------------------------------------------------
    No retorna nada
    """
    # operacion
    if distancia == 0:
        print("La distancia es ",calcularDistancia(velocidad, tiempo))
    elif tiempo == 0:
        print("El  tiempo es ",calcularTiempo(distancia, velocidad))
    elif velocidad == 0:
        print("La velocidad es",calcularVelocidad(distancia, tiempo))
    else:
        print("Existe todos los datos, o tenemos datos insuficientes para el calculo")


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
    # Definimos variables
    distancia = 0
    tiempo = 0
    velocidad = 0
    #repetir la operacion
    while True:
        # ingreso de datos
        [distancia, tiempo, velocidad] = ingresar()
        #calculo de datos faltantes
        calcular(distancia,tiempo,velocidad)
        #pregunta si se repite o no
        if hacerNuevamente():
            break
