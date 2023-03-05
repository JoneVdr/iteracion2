def algoritmo_suma_resta(n1, n2):
  while n1 != n2:
    if n1 > n2:
      n1 = n1 - n2
    else:
      n2 = n2 - n1
  return n1


numero = algoritmo_suma_resta(122, 138)
print(numero)
