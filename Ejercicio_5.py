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
            radio = int(input("Ingrese radio de la cilindro:\n"))
            altura = int(input("Ingresa la altura del cilindro:\n"))
            if radio > 0 and altura>0:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")

    # Valida que la letra este dentro del rango
    return radio,altura

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
def area(radio,altura, pi):
    """
    Funcion que calcula el area de una cilindro

    Parametro
    --------------------------------------------------
    Radio,altura y la contante pi 


    Retorna
    --------------------------------------------------
    area de un cilindro
    """
    # calculamos y devolvemos el resultado

    return 2*pi*radio*(radio+altura)

if __name__ == "__main__":
    # Declaracion de variables
    radio=0
    altura=0
    #constante universal
    pi=3.1415
    areaR=0
    #repetir operacion
    while True:
        #ingresamos datos de usuario
        [radio,altura]=ingreso()
        #calculamos el area de un cilindro
        areaR=area(radio,altura,pi)
        print("El area del cilindro es {} ".format(areaR))
        #pregunta si repite si o no
        if hacerNuevamente():
            break
