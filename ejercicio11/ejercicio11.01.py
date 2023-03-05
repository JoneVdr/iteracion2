def algortimo_euclides(n1, n2):
  resto = 0
  if n1 >= n2:
    while n1 % n2 != 0:
      resto = n1 % n2
      n1 = n2
      n2 = resto
    return n2
  else:
    while n2 % n1 != 0:
      resto = n2 % n1
      n2 = n1
      n1 = resto
    return n1


numero = algortimo_euclides(12, 18)
print(numero)
