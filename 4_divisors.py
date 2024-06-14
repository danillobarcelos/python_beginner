entrada = int(input("Digite um número: "))
lista = []

for i in list(range(1, entrada +1)):
    if entrada%i== 0:
        lista.append(i)

print(f"Os números divisores de {entrada} são {lista}")