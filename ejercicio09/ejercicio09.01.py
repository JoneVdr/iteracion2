def buscar_palabras(diccionario, siguiente, letra):
    palabras = []
    i = diccionario.index(letra) # Busca la primera palabra que empieza con la letra dada.
    while i != 0: # Mientras no se llegue al final de la lista.
        palabras.append(diccionario[i]) # Añade la palabra a la lista.
        i = siguiente[i] # Avanza a la siguiente palabra.
    palabras.sort() # Ordena la lista.
    return palabras
