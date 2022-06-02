import random
import statistics


def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)


def particion(arreglo, izquierda, derecha):
    indPivote = encuentraPivote(arreglo,izquierda, derecha)
    pivote = arreglo[indPivote]
    # pivote = arreglo[izquierda]

    while True:
        """
            Mientras cada elemento desde la izquierda esté en orden (sea menor que el
            pivote) continúa avanzando el índice
        """
        while arreglo[izquierda] < pivote:
            izquierda += 1

        """
            Mientras cada elemento desde la derecha esté en orden (sea mayor que el
            pivote) continúa disminuyendo el índice
        """
        while arreglo[derecha] > pivote:
            derecha -= 1

        """
                Si la izquierda es mayor o igual que la derecha significa que no
                necesitamos hacer ningún intercambio
                de variables, pues los elementos ya están en orden (al menos en esta
                iteración)
        """
        if izquierda >= derecha:
            """
                Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
                y ordenar los demás elementos
            """
            return derecha

        """
            Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
            alcanzó a la derecha)
            significa que se detuvieron porque encontraron un valor que no estaba
            en orden, así que lo intercambiamos
        """
        arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
        """
            Ya intercambiamos, pero seguimos avanzando los índices
        """
        izquierda += 1
        derecha -= 1

# Metodo encargado de encontrar el pivote sacando la mediana de tres numeros aleatorios en el subarreglo 
def encuentraPivote(arreglo, izq, der):
    ind1 = random.randint(izq, der)
    ind2 = random.randint(izq, der)
    ind3 = random.randint(izq, der)
    listaNumAleatorios = [arreglo[ind1], arreglo[ind2], arreglo[ind3]]
    indexPivote = int(statistics.median(listaNumAleatorios))

    return indexPivote
