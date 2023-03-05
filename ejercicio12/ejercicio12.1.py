def cuadrados_perfectos(limite):
  cuadrados = []
  for i in range(limite):
    if i**2 < limite:
      cuadrados.append(i**2)  #Añadir los cuadrados
    else:
      return cuadrados


if __name__ == "__main__":
  limite = input("Introduzca un límite: ")
  try:
    limite = int(limite)
    lista_cuadrados = cuadrados_perfectos(limite)
    print("La lista de cuadrados perfectos es", lista_cuadrados)
  except:
    print("Incorrecto")