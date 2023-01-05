
# Definimos las constantes de las ecuaciones
constC = 32
const = 9/5


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
            grado = int(input("Ingresar los grados:\n"))
            if type(grado)==int:
                break
        # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
    #Valida que la letra este dentro del rango
    while True:
        tipo = input(
            "Ingresa F si es Grado Fahrenheit o C si es Celcius:\n").upper()
        if tipo == 'C' or tipo == 'F':
            break
        else:
            print("No es ninguna de las letras, Ingrese nuevamente")
    # Retorna los datos ya ingresados por el usuario
    return grado,tipo

def celciusFahrenheit(grado):
    """
    Funcion para convertir de grados  Celcius a Fahrenheit 
    
    Parametros
    ------------------------------------------------------
    el grado a transformar

    Retorna
    ----------------------------------------------------
    retorna la opeacion de transformacion
    """
    #Transfroma de grado Celcius a Fahrenheit y lo devuelve
    return (grado-constC)/const
    
def fahrenheitCelcius(grado):
    """
    Funcion para convertir de grados Fahrenheit a Celcius 
    
    Parametros
    ------------------------------------------------------
    el grado a transformar

    Retorna
    ----------------------------------------------------
    retorna la opeacion de transformacion
    """
    #Transfroma de grado Fahrenheit a Celcius y lo devuelve
    return(const*grado)+32
def transformar(grado,tipo):
    """
    Funcion que Transformar los grados de un tipo a otro

    Parametros
    --------------------------------------------------------- 
    Necesitamos el grado y el tipo que tenemos

    Retorna
    ---------------------------------------------------------
    Retorna  la transformacion de un tipo a otro

    """
    #comprueba el tipo de dato a transformar
    if tipo=='C':
        #retorna grados Fahrenheit 
        return str(celciusFahrenheit(grado))+'F'
    elif tipo=='F':
        #retorna grados Celcius
        return str(fahrenheitCelcius(grado))+'C'

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
    # Definimos las variables
    grados = 0
    tipo = ''
    resul = ''
    while True:
        #Ingreso de datos por el usuario
        [grados,tipo]=ingreso()
        #transformamos de tipo de dato a otro 
        resul=transformar(grados,tipo)
        #mostramos los datos de la transformacion
        print("La transformacion de {}{} es {}".format(grados,tipo,resul))
        if hacerNuevamente():
            break
