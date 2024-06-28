import random
import numpy as np

lista = np.random.randint(0, 100, 100)
new_list = []

def first_and_last(lista):
    new_list.append(lista[0])
    new_list.append(lista[-1])
    return new_list

print(first_and_last(lista))

print(f'Lista: {lista}')