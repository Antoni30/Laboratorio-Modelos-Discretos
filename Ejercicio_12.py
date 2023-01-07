def ingresar():
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
            centimetros=int(input("Ingresa los centimetros a transformar:\n"))
            if centimetros>0:
                break
            else:
                print("datos esta fuera de los rangos establecidos")
            # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        # Retorna los datos ya ingresados por el usuario
    return centimetros

def trasformarMetros(centimetros):
    """
    Funcion que transfoma de cm a m

    Parametros
    ----------------------------------------------------------
    centimetros

    Retorna
    -----------------------------------------------------------
    la transformacion
    """
    #Operacion a transformar y el valor
    return centimetros/100

def trasformarKilometros(centimetros):
    """
    Funcion que transfoma de cm a Km

    Parametros
    ----------------------------------------------------------
    centimetros

    Retorna
    -----------------------------------------------------------
    la transformacion
    """
    #Operacion a transformar y el valor
    return centimetros/10000


def mostrar(centimetros,metros,kilometros):
    """
    Funcion que muestra los resultados obtenidos

    Parametro
    ---------------------------------------------------------
    Centimentros

    Retorna
    ---------------------------------------------------------
    no retorna
    """
    print("{}cm es {}m".format(centimetros,metros))
    print("{}cm es {}km".format(centimetros,kilometros))

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
    centimetros=0
    metros=0
    kilometros=0
    while True:
        #ingreso de datos
        centimetros=ingresar()
        #transformacion de cm a m
        metros=trasformarMetros(centimetros)
        #tranformacion de cm a km
        kilometros=trasformarKilometros(centimetros)
        #mostrar los resultados
        mostrar(centimetros,metros,kilometros)
        if hacerNuevamente():
            break