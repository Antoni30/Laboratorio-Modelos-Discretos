def ingreso(varA,varB,varC):
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
        print("Si no conoce algun cateto o la hipotenusa colocar 0")
        # permite capturar errores
        try:
            # Pedimos por teclado cada uno de  los catetos
            varA = int(
                input("Ingresar el Cateto A:\n"))
            varB= int(
                input("Ingresar el Cateto B:\n"))
            varC = int(
                input("Ingresa la Hipotenusa:\n"))
            #validamos la hipotenusa
            if varC!=0:
                #vali que todos los lados sean mayor a los numeros indicados
                if varA>-1 and varB>-1  and varC>-1:
                    #hipotenusa debe ser mayor a los catetos
                    if varC>varA and varC>varB:
                        break
                    else:
                        #caso contrario pediremos nuevos datos
                        print("La hipotenusa es menor a los catetos")
            else:
                #vali que todos los lados sean mayor a los numeros indicados
                if varA>-1 and varB>-1  and varC>-1:
                    break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    # Valida que la letra este dentro del rango
    return varA,varB,varC
def calcularHipotenusa(catetoA,catetoB):
    """
    Funcion que permite calcular la hipotenusa de un triangulo

    Parametro
    -----------------------------------------------------------
    Necesitamos 2 catetos 

    Retorna
    -----------------------------------------------------------
    El valor de la hipotenusa
    """
    #calculamos y devolvemos la hipotenusa
    return ((catetoA)**2+(catetoB)**2)**(1/2)

def calculoCateto(hipotenusa,cateto):
    """
    Funcion Que permite calcular un cateto 

    Parametro
    ---------------------------------------------------------------
    necesitamos una hipotenusa y un cateto

    Retorna
    ----------------------------------------------------------------
    Devolvemos el resultado de un Cateto
    """
    #Calculamos y devolvemos un cateto
    return ((hipotenusa)**2 - (cateto)**2)**(1/2)

def ladoFantante(catetoA,catetoB,hipotenusa):
    """
    Funcion para buscar un lado faltante de un triangulo rectangulo

    Parametros
    --------------------------------------------------------------
    Lados de un triangulo rectangulo como el cateto A, B y la hipotenusa
    
    Retorna
    --------------------------------------------------------------
    Lado o hipotenusa faltante
    """
    if catetoA!=0 and catetoB!=0:
        #retornamos el valor de la hipotenusa
        return "La hipotenusa es: "+str(calcularHipotenusa(catetoA,catetoB))
    else:
        if catetoA == 0:
            #retornamos el valor del Cateto faltante
            return "El cateto A es "+str(calculoCateto(hipotenusa,catetoB))
        else:
            #retornamos el valor del Cateto faltante
            return "El cateto B es "+str(calculoCateto(hipotenusa,catetoA))

if __name__ == "__main__":
   #declaracion de variables
   varA=0
   varB=0
   varC=0
   #ingreso de datos deseados por el usuario
   [varA,varB,varC]=ingreso(varA,varB,varC)
   #Buscamos el lado faltante y lo mostramos
   print(ladoFantante(varA,varB,varC))

            
