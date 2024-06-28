numero = int(input("Digite um número inteiro: "))

z = []

def numero_primo(numero):
    for i in range(1, numero+1):
        if numero%i == 0:
            z.append(i)
    
    if len(z) == 2:
        return "Este número é primo"
    else:
        return "Este número não é primo"
    
print(numero_primo(numero))


