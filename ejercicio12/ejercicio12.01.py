def cuadrados_perfectos(limite):
  cuadrados = []
  i = 0
  while i**2 <= limite:  #bucle iterativo
    cuadrados.append(i**2)
    i += 1
  return cuadrados





if __name__ == "__main__":
  limite = int(input("Introduzca un límite: "))
  lista_cuadrados = cuadrados_perfectos(limite)
  print("La lista de cuadrados perfectos es", lista_cuadrados)