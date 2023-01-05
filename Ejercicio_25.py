def ingreso(raiz,numero):
    """
    Funcion que permite pedir al usuario datos que usaremos en nuestro programa

    Parametros
    --------------------------------------------------------------------------
    necesitamos el numero de la raiz que vamos y el numero que vamos a sacar esa raiz

    Retorna
    --------------------------------------------------------------------------
    Retornamos las variables con los datos respectivos

    """
    #Valida hasta que el numero sea correcto
    while True:
        #permite captuirara errores
        try:
            #pedimos el exponente de la raiz 
            raiz=int(input("Ingrese la raiz que desea sacar:\n"))
            #pedimos el numero de la raiz
            numero=int(input("Ingrese el numero:\n"))
        #si salta un error mandamos una respuesta
        except:
            #Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        #comprobamos si la raiz el positiva caso contrario regresa a pedir el valor
        if raiz<0:
            print("Las raices no pueden ser negativas ingresa un numero positivo")
        #cuando cumplan que sea numero para el bucle y retorno los valores 
        elif raiz >= 1  and numero!=0:
            break 
    #Retorna los datos ya ingresados por el usuario           
    return raiz, numero

def raizN(numero,raiz):
    """
    Funcion que calcula la n raiz de cualquier n numero

    Parametro
    --------------------------------------------------------------
    Necesitamos un numero y el numero de la raiz que vamos a sacar

    Retorna
    ---------------------------------------------------------------
    Retornamos la operacion
    """
    #retornamos el resultado de la operacion
    return numero ** (1/raiz)

if __name__=="__main__":
    #Declaramos varibales y las inicializamos
    raiz=0
    numero=0
    result=0
    #Usamos la funcion de ingreso y obtenemos los datos
    [raiz, numero]=ingreso(raiz,numero)
    #Usamos la Funcion de raizN para sacar la raiz n de cualquier numero
    result=raizN(numero,raiz)
    #mostramos resultados
    print("La raiz {} de {} es {}".format(raiz,numero,result))