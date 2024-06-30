frase = input("Digite uma frase: ")

def revers_phrase_order(frase):     #resultado = " ".join(frase.split()[::-1])
    particao = frase.split()
    resultado = particao[::-1]

    reverso = " ".join(resultado)
    print(reverso)


def reverse_phrase(frase):
    resultado = frase[::-1]
    print(resultado)

revers_phrase_order(frase)
reverse_phrase(frase)


