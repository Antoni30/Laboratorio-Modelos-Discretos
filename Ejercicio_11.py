def tamDatos():
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
            #Datos ingresados por el usuario
            numDatos=int(input("Ingrese el numero datos:\n"))
            if type(numDatos)==int:
                break
            # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero")
            print("Vuelva a ingresar")
        # Retorna los datos ya ingresados por el usuario
    return numDatos

def ingresoDatos(numDatos):
    """
    Funcion que recoge datos

    Parametros
    --------------------------------------------------
    el numero de datos

    Retorna
    ----------------------------------------------
    Datos
    """
    datos=[]
    dato=0
    #pedimos los  n datos
    for i in range(0,numDatos):
        #validacion del dato
        while True:
            #captura de errores
            try:
                #ingreso del dato
                dato=int(input("Ingresa el dato {}\n".format(i+1)))
                #si es un entero salgo de la comprobacion
                if type(dato)==int:
                    break
            except:
                print("No es un numero")
        #agregamos al arreglo
        datos.append(dato)
    #retornamos los valores
    return datos

def calSuma(datos):
    """
    Funcion que calcula la suma de todos los datos

    Parametros
    -----------------------------------------------------
    el arreglo de datos

    Retorna
    ----------------------------------------------------
    la suma de datos 
    """
    #definimos un acumulador
    acum=0
    #recorremos nuestro arreglo
    for dato in datos:
        #sumamos los datos
        acum+=dato
    #retornamos la suma de los datos 
    return acum

def calResta(datos):
    """
    Funcion que calcula la resta de todos los datos

    Parametros
    -----------------------------------------------------
    el arreglo de datos

    Retorna
    ----------------------------------------------------
    la resta de datos 
    """
    #definimos un acumulador
    acum=datos[0]
    #recorremos nuestro arreglo
    for i in range(1,len(datos)):
        #resta los datos
        acum=acum-datos[i]
    #retornamos la resta de los datos 
    return acum

def calMul(datos):
    """
    Funcion que calcula la multiplicacion de todos los datos

    Parametros
    -----------------------------------------------------
    el arreglo de datos

    Retorna
    ----------------------------------------------------
    la multiplicacion de datos 
    """
    #definimos un acumulador
    acum=1
    #recorremos nuestro arreglo
    for dato in datos:
        #multiplicamos los datos
        acum*=dato
    #retornamos la suma de los datos 
    return acum
def calDiv(datos):
    """
    Funcion que calcula la divicion de todos los datos

    Parametros
    -----------------------------------------------------
    el arreglo de datos

    Retorna
    ----------------------------------------------------
    la divicion de datos 
    """
    #definimos un acumulador
    acum=datos[0]
    #recorremos nuestro arreglo
    for i in range(1,len(datos)):
        #divicion los datos
        acum/=datos[i]
    #retornamos la suma de los datos 
    return acum
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
    numDatos=0
    datos=[]
    suma=0
    resta=0
    multiplicacion=0
    divicion=0
    while True:
        #ingresos de numero de datos
        numDatos=tamDatos()
        #ingresos de datos
        datos=ingresoDatos(numDatos)
        #operacion Suma
        suma=calSuma(datos)
        #operacion resta
        resta=calResta(datos)
        #operacion multiplicacion
        multiplicacion=calMul(datos)
        #operacion divicion
        divicion=calDiv(datos)
        #Los prints muestan los operaciones
        print("Los datos son ",datos)
        print("La suma de datos es ",suma)
        print("La resta de datos es ",resta)
        print("La multiplicacion de datos es ",multiplicacion)
        print("La Divicion de datos es ",divicion)
        if hacerNuevamente():
            break

