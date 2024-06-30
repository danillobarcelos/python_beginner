import random
import numpy as np

random_list = np.random.randint(1,100, 100)

new_list = []

def removing_duplicates(random_list):
    for i in random_list:
        if i not in new_list:
            new_list.append(i)
    
    return "A nova lista sem itens duplicados é: \n" + str(new_list)

def removing_with_sets(random_list):
    new_list = list(set(random_list))
    return "A nova lista sem itens duplicados usando sets é: \n" + str(new_list)

print(f'A lista completa é: \n {random_list}')
print(removing_duplicates(random_list))
print(removing_with_sets(random_list))