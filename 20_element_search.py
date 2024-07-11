import random
import numpy as np

r = random.randint(0, 100)
lista = sorted(np.random.randint(0, 100, r))


def regular_search(lista, numero):
    for i in lista:
        if numero in lista:
            print(f'Sim, o número {numero} está na lista')
            break
        else:
            print(f'Não, o número {numero} não está na lista')
            numero = int(input("Digite um número inteiro: "))


def binary_search(lista, numero):
    if len(lista) == 0:
        print(f'Não, o número {numero} não está na lista')
        return False

    meio = len(lista)//2

    if numero == lista[meio]:
        print(f'Sim, o número {numero} está na lista!')
    elif numero > lista[meio]:
        return binary_search(lista[meio+1:], numero)
    elif numero < lista[meio]:
        return binary_search(lista[:meio], numero)
    else:
        print(f'Não, o número {numero} não está na lista') 
    



numero = int(input("Digite um número inteiro: "))
binary_search(lista, numero)
print("---------------------------------------")
regular_search(lista, numero)
print("---------------------------------------")
print(lista)