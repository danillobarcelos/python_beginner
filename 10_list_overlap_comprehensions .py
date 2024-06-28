import random as rd
import numpy as np

range_x = rd.randint(1,100)
range_y = rd.randint(1,100)



lista_x = np.random.randint(0, 100, (range_x))
lista_y = np.random.randint(0, 100, (range_y))

lista_z = []

for num in lista_x:
    if num in lista_y and num not in lista_z: #não imprime números repetidos
        lista_z.append(num)

print(f'Lista X: {lista_x}')
print(f'Lista Y: {lista_y}')
print(f'Lista Z: {lista_z}')

lista_w = [num for num in lista_x if num in lista_y] #imprime números repetidos

print(f'Lista W: {lista_w}')