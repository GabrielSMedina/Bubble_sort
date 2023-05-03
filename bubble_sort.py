def bubble_sort(lista):
    continuar = False
    for c in range(len(lista)-1):
        if lista[c] > lista[c+1]:
            lista[c], lista[c+1] = lista[c+1], lista[c]
            continuar = True
    print(lista)
    if continuar:
        bubble_sort(lista)
    return lista

lista = [8, 9, 5, 2, 3]
lista_ordenada = bubble_sort(lista)
print(f'Lista ordenada: {lista_ordenada}')
