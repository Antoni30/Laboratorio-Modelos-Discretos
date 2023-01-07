def ingreso(base, altura):
    """
    Funcion que permite pedir al usuario datos que usaremos en nuestro programa

    Parametros
    --------------------------------------------------------------------------
    Necesitamos variables para guardar mis datos como es la base y altura de un triangulo

    Retorna
    --------------------------------------------------------------------------
    Retornamos las variables con los datos respectivos

    """
    # Valida hasta que el numero sea correcto
    while True:
        # permite capturamos errores
        try:
            #Pedimos por teclado el dato de base
            base = float(input("Ingresa la base del triangulo:\n"))
            #Pedimos por teclado el dato de la altura
            altura = float(input("Ingrese la altura del triangulo:\n"))
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        # comprobamos si la base y la area es mayor o igual a 0
        if base>0 and altura>0:
            break
        else:
            print("Ingrese valores mayores a 0")
    # Retorna los datos ya ingresados por el usuario
    return base, altura

def calcularArea(base,altura):
    """
    Funcion que calcula el area de cualquier triangulo rectangulo

    Parametros
    -----------------------------------------------------
    Base y altura del triangulo


    Retorna
    ------------------------------------------------------
    retornamos el resultado de la operacion
    """
    return (base*altura)/2
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

if __name__ == "__main__":
    # declaramos variables
    base = 0
    altura = 0
    area = 0
    while True:
        #Usamos la funcion de ingreso para recuperar datos ingresados por el usuario
        [base,altura]=ingreso(base,altura)
        #calculamos el area con la funcion calcularArea
        area=calcularArea(base,altura)
        #mostramos el resultado
        print("El area del Triangulo Rectangulo es: ",area)
        if hacerNuevamente():
            break

