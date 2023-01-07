def ingresar(posAnterior):
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
      #Posicion Actual
      actual = int(input("Ingrese el numero actual:\n"))
      #Posicion anterior
      if posAnterior == 0:
        posAnterior = int(input("Ingrese el elemento anterior:\n"))
      if posAnterior > 0 and actual > 0:
        break
      else:
        print("Datos fuera del rango")
      # si salta un error mandamos una respuesta
    except:
      # Mostramos informacion
      print("No es un numero alguno de los dos datos ingresados:")
      print("Vuelva a ingresar")
    # Retorna los datos ya ingresados por el usuario
  return actual, posAnterior


def calcular(posAc, posAt):
  """
  Funcion que calcula la suma actual  con el anterior

  Parametros
  -------------------------------------------------------
  posicion anterior y la posicion actual

  Retorna
  ------------------------------------------------------
  retorna la sumas
  """
  #operacion
  return posAt + posAc


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
  #Definimos variables
  posAc = 0
  posAt = 0
  valorR = 0
  #preguntamos el como 
  while True:
    #ingresa valores del usuario
    [posAc, posAt] = ingresar(posAt)
    #calcula la suma de valores
    valorR = calcular(posAc, posAt)
    #mostramos el resultado
    print(
      "La suma de posicion Anterior: {} + la posicion Actual: {} es {}".format(
        posAt, posAc, valorR))
    #guardamos el nuevo dato anterior 
    posAt = valorR
    #preguntamos si repetimos la operacion
    if hacerNuevamente():
      break
