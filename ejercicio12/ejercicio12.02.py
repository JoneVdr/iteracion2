def raices(numero):  #r^2 ≤ n < (r + 1)^2
  i = 0
  while i**2 <= numero:
    i += 1
    if i**2 == numero:
      return i
if __name__ == "__main__":
  numero = int(input("Introduzca un numero entero para hacer la raiz cuadrada entera: "))
  if numero >= 0:
    raiz = raices(numero)
    print("La raiz entera es", raiz)
  else:
    print("Invalido")