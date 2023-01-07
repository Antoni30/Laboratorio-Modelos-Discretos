def tamUsuarios():
    """
    Funcion que mide el tamanio de usuario a saludar

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
            numUsuario=int(input("Ingrese el numero de usuarios ha saludar :\n"))
            if numUsuario>0:
                break
        except:
        # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    return numUsuario
def ingresar():
    """
    Funcion que creara el nombre del usuario

    Parametro
    -------------------------------------------------------
    no tiene parametro

    Retorna
    ------------------------------------------------------
    nombre se usuario 
    """
    #creamos un usuario
    nombreU=input("Ingresa el nombre de Usuario:\n")
    return nombreU
def saludoCrear():
    """
    Funcion que permite crear un saludo

    Paramtero
    ------------------------------------------------
    No tienen parametros

    Retorna
    ------------------------------------------------
    Retorna un saludo
    """
    #creamos saludo
    saludo=input("Ingrese un saludo:\n")
    return saludo

def saludarUsuario(numU,saludo):
    """
    Funcion que permite saludar a n usuario

    Parametros
    -----------------------------------------------------
    numero de Usuario y el saludo

    Retorna 
    -----------------------------------------------------
    no retorna nada
    """
    #Declaramos las variables a usar 
    nombreU=""
    result=""
    #recorremos desde 0 hasata el numero de usuarios a saludar
    for i in range(0,numU):
        #pedimos nombre de un usuario
        nombreU=ingresar()
        #guardamos todos los nombres de usuarios y el saludo en una sola variable
        result=nombreU+", "+saludo+"; "+result
    print(result)




if __name__=="__main__":
    #Declaracion de variables
    numU=0
    saludo=""
    #buscamos el numero de Usuarios
    numU=tamUsuarios()
    saludo=saludoCrear()
    saludarUsuario(numU,saludo)

