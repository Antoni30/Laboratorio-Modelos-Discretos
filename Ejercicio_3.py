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
            ladoMenor=int(input("Ingrese el lado menor del Rectangulo:\n"))
            ladoMayor=int(input("Ingrese el lado mayor del Rectangulo:\n"))
            if ladoMayor>0 and ladoMenor>0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return ladoMayor,ladoMenor

def areaR(ladoMayor,ladoMenor):
    """
    Funcion que calcula el area de un rectangulo

    Parametros
    -----------------------------------------------------------
    base mayor y base menor del rectangulo

    Retorna
    ----------------------------------------------------------
    Area de un rectangulo
    """
    #calculo del area de un rectangulo
   
    return (ladoMenor*ladoMayor)

def perimetroR(ladoMayor, ladoMenor):
    """
    Funcion que calcula el perimetro de un rectangulo

    Parametros
    -----------------------------------------------------------
    base mayor y base menor del rectangulo

    Retorna
    ----------------------------------------------------------
    Perimetro de un rectangulo
    """
    #calculo del perimetro de un rectangulo
    return 2*(ladoMenor+ladoMayor)

def calcular(ladoMayor,ladoMenor):
    """
    Funcion que realizara las operaciones deseadas

    Parametros
    -----------------------------------------------
    base mayor y base menor del rectangulo

    Retorna
    ----------------------------------------------
    el resultado de la operacion de area y perimetro
    """
    resultArea=areaR(ladoMayor,ladoMenor)
    resultPerimetro=perimetroR(ladoMayor,ladoMenor)
    return resultArea, resultPerimetro

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
    #Pedimos datos que nos servira ver que opcion quiere hacer
    opc=input("Ingresar otros Datos?\n 1.-Si\n Cualquier Tecla.-No\n")
    #comprobamos las opciones
    if opc=='1':
        #retornamos un falso si desea repetir
        return False
    #retornamos un verdadero si no desea repetir
    return True

if __name__=="__main__":
    #Declaracion de variables
    ladoMenor=0
    ladoMayor=0
    area=0
    perimetro=0
    #bucle para repetir operacion
    while True:
        #ingreso de datos por usuario
        [ladoMayor,ladoMenor]=ingreso()
        #calculo de area y perimetro
        [area,perimetro]=calcular(ladoMayor,ladoMenor)
        print("El area del rectangulo es {} y el perimetro {}".format(area,perimetro))
        #repite la operacion
        if hacerNuevamente():
            #sale del bucle
            break


