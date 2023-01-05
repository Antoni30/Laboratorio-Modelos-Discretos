#constante hora de trabajo
constHora=10.5

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
           horasTrabajadas=int(input("Ingrese las horas trabajadas:\n"))
           if horasTrabajadas>0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return horasTrabajadas

def tamUsuarios():
    """
    Funcion que mide el tamanio de usuario que necesita saber su ganacia

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
            numUsuario=int(input("Ingrese el numero de usuarios que desea saber su coste de Trabajo:\n"))
            if numUsuario>0:
                break
        except:
        # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    return numUsuario

def calcular(horasUsuarios):
    """
    Funcion para calcular las horas de trabajo de un usuario

    Parametros
    -------------------------------------------------------------
    Horas trabajadas de usuarios

    Retorna
    -----------------------------------------------------------
    la cantidad de dinero que gana por hora un usuario
    """
    #calculo de la operacion y retornamos el valor de cuanto gana 
    return constHora*horasTrabajadas

if __name__=="__main__":
    #declaramos variables
    numUsuario=0
    horasTrabajadas=0
    result=0
    #ingreson de datos por usuario
    numUsuario = tamUsuarios()
    #El numero de usuario que desean saber cuanto ganan 
    for i in range(0,numUsuario):
        #muestra en que usuario esta
        print("Usuario ",i+1)
        #pide las horas tranbajadas del usuario
        horasTrabajadas=ingreso()
        #calcula cuanto gana
        result=calcular(horasTrabajadas)
        #muestra en pantalla cuanto gana el usuario
        print("Tu sueldo ganado por tus horas trabajadas es $",result)


    
