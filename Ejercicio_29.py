import sys

def materias():
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
            numMaterias=int(input("Ingrese el numero de materias:\n"))
            if numMaterias>0:
                break
            else:
                print("datos esta fuera de los rangos establecidos")
            # si salta un error mandamos una respuesta
        except:
            # Mostramos informacion
            print("No es un numero alguno de los dos datos ingresados:")
            print("Vuelva a ingresar")
        # Retorna los datos ya ingresados por el usuario
    return numMaterias

def notasMateria(numMaterias):
    """
    Funcion que permite ingresar notas de la materias 

    Parametro
    -----------------------------------------------
    numero de materias

    Retorna
    -----------------------------------------------
    el total de las notas 
    """
    #acumalador de notas
    acum=0
    #ingreso de nota de materia
    for i in range(0,numMaterias):
        #compueba si cumple que es un numero
        while True:
            #control de error
            try:
                #ingreso de datos
                nota=int(input("Ingrese la nota de la materia {}:\n".format(i+1)))
                #validacion de rango de nota
                if nota>0 and nota<=20:
                    break
                else:
                    print("Nota fuera de rango")
            except:
                print("No es un numero el dato ingresado")
        #suma de todas las notas 
        acum+=nota
    #retorna el total de la suma de notas
    return acum

def calPromedio(total,numMateria):
    """
    Funcion que calcula el promedio de materias 

    Parametro
    ---------------------------------------------------
    la suma total de las materias y el numero de materias

    Retorna
    --------------------------------------------------
    el promedio
    """
    #calculo y devuelve el promedio
    return total/numMateria

def calPorcentaje(promedio):
    """
    Funcion que calcula el porcentaje de materias 

    Parametro
    ---------------------------------------------------
    promedio que posee el estudiante

    Retorna
    --------------------------------------------------
    el porentaje que tiene
    """
    #calculo y devuelve el porcentaje
    return (promedio*100)/20

def mostrar(total,promedio,porcentaje):
    """
    Funcion para que muestre los resultados

    Parametros
    -----------------------------------------------
    el total de las notas, el promedio y el porcentaje

    Retorna
    --------------------------------------------------
    no retorna
    """
    print("La suma de todas las notas es {}, y el promedio es {} dando un porcentaje de {}%".format(total,promedio,porcentaje))

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
    numMaterias=0
    total=0
    promedio=0
    porcentaje=0
    #repetir operacion
    while True:
        #el numero de materias
        numMaterias=materias()
        #la suma de todas las notas
        total=notasMateria(numMaterias)
        #promedio
        promedio=calPromedio(total,numMaterias)
        #porcentaje que tiene el estudiante
        porcentaje=calPorcentaje(promedio)
        #muestra en pantalla los resultados
        mostrar(total,promedio,porcentaje)
        #preguntrar si repetir la operacion
        if hacerNuevamente():
            break
