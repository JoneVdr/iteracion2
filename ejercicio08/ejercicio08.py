def analizar_cadena(cadena, separador):
  subcadenas = []
  subcadena_actual = ""
  for i in cadena:
    '''
        Si el caracter actual es el separador, se guarda la subcadena
        actual y se inicializa una nueva cadena vacía para construir la siguiente subcadena
        '''
    if i == separador:
      subcadenas.append(subcadena_actual)
      subcadena_actual = ""
    # Si el caracter actual no es el separador, se agrega a la subcadena actual
    else:
      subcadena_actual += i
  subcadenas.append(subcadena_actual)

  return subcadenas


cadena = "Este es un:ejemplo :de cadena a analizar"
separador = ":"
resultado = analizar_cadena(cadena, separador)
print(resultado)
