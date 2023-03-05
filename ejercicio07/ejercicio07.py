def algoritmo_representacion_base(numero, base):
  if base > 36:
    resultado = ""
    while numero > 0:  # Mientras el número sea mayor que cero
      resto = numero % base
      resultado = str(resto) + "." + resultado
      numero = numero // base  # División entera
    print(resultado)  # Elimina el último punto
  else:
    print("La base debe ser mayor que 36")


convertir = algoritmo_representacion_base(3000, 256)
print(convertir)
