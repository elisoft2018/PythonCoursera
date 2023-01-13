def buscar_numero(numero, lista):
    """
    Busca el numero @numero en la lista @lista.
    Si lo encuentra devuelve la posición en la que se 
    encontró su primera aparición.
    Si no devuelve -1.
    """
    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    return  print("La posición es: ",indice," El valor es :" ,item)

buscar_numero(1,[9,4,6,7,1,5,6])
buscar_numero(1,[9,4,6,7,6])