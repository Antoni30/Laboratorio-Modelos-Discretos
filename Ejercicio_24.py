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
            # pedimos el exponente
            exponente = int(input("Ingrese el exponente:\n"))
            # pedimos el numero
            numero = int(input("Ingrese el numero:\n"))
            if exponente==0:
                return numero, exponente
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        if exponente!=0 and numero!=0:
            break
    # Retorna los datos ya ingresados por el usuario
    return numero, exponente

def evevadoA_N(varX,expo):
    """
    Funcion que calcula un numero elevado a n exponente

    Parametros
    ----------------------------------------------------------------
    necesitamos una variable x que representara al numero y un exponente al que se va a elevar

    Retorna
    -----------------------------------------------------------------
    El resultado de la operacion

    """
    #retornamos la operacion 
    return varX**expo
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
    #Declaramos Variables
    varX=0
    expo=0
    result=0
    while True:
        #Ingreso de datos  por el usuario
        [varX,expo]=ingreso()
        #Usamos la funcion que  realizara el calculo
        result=evevadoA_N(varX,expo)
        #imprimimos el resultado
        print("El numero {} elevado a {} es {}".format(varX,expo,result))
        if hacerNuevamente():
            break
    
