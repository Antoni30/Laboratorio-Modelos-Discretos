def tamDatos():
    """
    Funcion que mide el tamanio de usuario que necesitamos

    Parametro
    --------------------------------------------------------------------
    No necesita parametros

    Retorna
    -------------------------------------------------------------------
    El numero de usuarios 
    """
    # Valida hasta que el numero sea correcto
    while True:
        try:
            #pedimos datos por usuarios
            numDatos=int(input("Ingrese el numero de datos:\n"))
            if numDatos>0:
                break
        except:
        # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    return numDatos

def calcular(numDatos):
    """
    Funcion que calcula la operaciones deseada

    Parametro
    --------------------------------------------------
    num de datos 

    Retrorna
    ----------------------------------------------------
    el resultado de la operacion
    """
    #un acumlador
    resul=0
    #ingresamos los n datos
    for i in range(0,numDatos):
        #comporbamos que sea un numero
        while True:
            #manejo de errores
            try:
                #ingreso de datos por el usuario
                var=int(input("Ingrese un numero:\n"))
                expo=int(input("Ingrese el exponente del numero:\n"))
                if type(var)==int:
                    break
            #salta la exepcion
            except:
                print("No es un numero lo ingresado")
        #sumamos los valores
        resul+=(var**expo)
    return resul/2.5

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

if __name__=="__main__":
    #definimos variables
    numDatos=0
    resul=0
    #reptimos los datos
    while True:
        #ingreso de datos
        numDatos=tamDatos()
        #calculo de la operacion
        resul=calcular(numDatos)
        #mostramos el resultado
        print("Resultado de la Operacion es {}".format(resul))
        if hacerNuevamente():
            break


