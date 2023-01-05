#definimos el constante denominador de la ecuacion
constDenominador=2

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
            # Pedimos por teclado la base mayor, base menor y la altura
            baseM = int(
                input("Ingresar Base Mayor del  trapezoide:\n"))
            baseMe = int(
                input("Ingresar Base Menor del trapezoide:\n"))
            altura = int(
                input("Ingresar la altura del trapezoide:\n"))

            if baseM > 0 and baseMe > 0 and altura > 0:
                break
            else:
                print(
                    "Algunos de los datos ingresados son menores a 0. Ingrese nuevamente los valores ")
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    # Valida que la letra este dentro del rango
    return baseM, baseMe, altura


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

def calculoDeArea(baseM,baseMe,altura):
    """
    Funcion que alcual el area de un trapezoide

    Parametros
    -------------------------------------------------------
    Base Mayor, Base Menor y la altura de un trapezoide

    Retorna
    --------------------------------------------------------
    Retorna el area del trapezoide

    """
    #Calculo de area del trapezoide y retorno del resultado
    return ((baseM+baseMe)*altura)/constDenominador

if __name__ == "__main__":
    # Declaracion de variables
    baseM = 0
    baseMe = 0
    altura = 0
    resultArea = 0
    while True:
        #ingreso de datos por teclado
        [baseM,baseMe,altura]=ingreso()
        #calculo de area del trapezoide
        resultArea=calculoDeArea(baseM,baseMe,altura)
        #Muestra el area del trapezoide
        print("El area del Trapezoide es {}".format(resultArea))
        if hacerNuevamente():
            break



