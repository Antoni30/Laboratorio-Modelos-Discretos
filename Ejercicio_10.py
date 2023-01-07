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
            numVariables = int(input("Ingrese el numero de variables existentes en la Operacion:\n"))
            if numVariables > 0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return numVariables


def nuevaOperacion():
    """
    Funcion que pedirar al usauario una operacion matematica que resolver 

    Parametro
    ------------------------------------------------------------
    Ningun parametro

    Retorna
    ---------------------------------------------------------
    una operacion 
    """
    #pedir al usuario por teclado la operacion
    operacion=input("Ingrese una operacion matematica a resolver:\n")

    #retornamos la operacion

    return operacion


def definirValores(numIcognitas):
    """
    Funcion que definine  valores a las incognitas

    Parametro
    ---------------------------------------------------
    numero de incognitas

    Retorna
    ---------------------------------------------------
    Diccionarion con incognitas y valores
    """
    #definimos variables
    incognitas={}
    incognita=""
    valor=0
    #recorrido para obtener las n ingnitas con sus valores
    for i in range(0,numIcognitas):
        #incognitas  que selecione el usuario
        incognita=input("Ingrese la incognita {}:\n".format(i+1))
        #si tiene  un error repite
        while True:
            #validacion de que sea un numero
            try:
                #valor de las incognitas 
                valor=int(input("Ingresa el valor de la incognita {}:\n".format(incognita)))
                if valor >0:
                    break
            except:
                print("No es un numero, Ingresa un Numero ")
        #guardar el valor en el el diccionario
        incognitas[incognita]=valor
    #Retornamos dicicionario
    return incognitas
    
def calcular(operacion, incognitas):
    """
    Funcion que permite calcular la operaciones

    Parametro
    ---------------------------------------------
    La operacion a tratar, las incognitas con su valor y en num de incognitas

    Retorna
    ------------------------------------------------
    retorna el valor 
    """
    nuevaOperacion=" "
    for clave in incognitas:
        nuevaOperacion = operacion.replace(clave,str(incognitas[clave]))
    #retorna el resultado de la operacion
    return eval(nuevaOperacion)

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
    #decleracion de variables
    numIncognitas=0
    operacion=""
    result=0
    incognitas={}
    #repetir  la operacion
    while True:
        #pedimos la Operacion
        operacion=nuevaOperacion()
        #numero de variables en la operacion
        numIncognitas=ingreso()
        #incognitas con los valores
        incognitas=definirValores(numIncognitas)
        #Calculo de las operaciones 
        result=calcular(operacion,incognitas)
        print("El resultado de la Operacion es {}".format(result))
        #pregunta si repite las operaciones
        if hacerNuevamente():
            break


    