from Algoritmo import quicksort
import random, time

tamArr = 10000
arreglo = random.sample(range(tamArr), tamArr)

# print(arreglo)

tiempo1 = time.time()
quicksort(arreglo, 0, len(arreglo) - 1)
tiempo2 = time.time()

print('\nHa tardado:', tiempo2 - tiempo1, 'segundos')
