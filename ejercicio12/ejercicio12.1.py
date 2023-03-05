def cuadrados_perfectos(limite):
  cuadrados = []
  i = 0
  while i**2 <= limite:  #bucle iterativo
    cuadrados.append(i**2)
    i += 1
  return cuadrados


def raices(numero):  #r^2 ≤ n < (r + 1)^2
  i = 0
  while i**2 <= numero:
    i += 1
    if i**2 == numero:
      return i


if __name__ == "__main__":
  limite = int(input("Introduzca un límite: "))
  lista_cuadrados = cuadrados_perfectos(limite)
  print("La lista de cuadrados perfectos es", lista_cuadrados)
  numero = int(
    input("Introduzca un numero entero para hacer la raiz cuadrada entera: "))
  if numero >= 0:
    raiz = raices(numero)
    print("La raiz entera es", raiz)
  else:
    print("Invalido")