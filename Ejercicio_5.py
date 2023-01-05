# Definimos la constante del denominador
constDenominador = 2


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
            numX = int(input("Ingrese un numero:\n"))
            expo = int(input("Ingrese un exponente:\n"))
            if type(numX) == int and type(expo) == int:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return numX, expo

def calcular(numX, expo):
    """
    Funcion que permite calcular la ecuacion planteada

    Parametros
    -------------------------------------------------------
    Necesitamos un numero y un exponente


    Retornamos
    ------------------------------------------------------
    Calculamos la ecuacion y devolvemos el resultado

    """
    # realizamos la ecuacio  y devolvemos el resultados
    return (numX**expo)/constDenominador


if __name__ == "__main__":
    # declaramos variables
    numX = 0
    expo = 0
    result = 0
    # Datos ingresados por el usuario
    [numX, expo] = ingreso()
    # resulato de la operacion
    result=calcular(numX,expo)
    print("El resultado de la operacion es ",result)
