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
            expoR = int(input("Ingrese el exponente de la Raiz:\n"))
            expo = int(input("Ingrese el exponente:\n"))
            vara = int(input("Ingrese el valor de A:\n"))
            varb = int(input("Ingrese el valor de B:\n"))
            varc = int(input("Ingrese el valor de C:\n"))
            if ((varb**expo)+varc)>0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return expoR,expo,vara,varb,varc

def calcular(expoR,expo,vara,varb,varc):
    """
    Funcion que calcula la operacion

    Parametro
    ---------------------------------------------
    El exponente de la raiz, de la variable b, variable A , variable B y varible C:

    Retorna
    -----------------------------------------------
    el resultado de la operacion
    """
    return ((-varb+((varb)**expo)+varc)**expoR)/expo*vara
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
    expoR=0
    varb=0
    varc=0
    vara=0
    resul=0
    #repetir la operacion
    while True:
        #ingreso de datos por usuario
        [expoR,expo,vara,varb,varc]=ingreso()
        #calculo de operaciones
        resul=calcular(expoR,expo,vara,varb,varc)
        #mostramos por pantalla
        print("El resultado de la operacion es {}".format(resul))
        #preuntar si se repite la operacion
        if hacerNuevamente():
            break
