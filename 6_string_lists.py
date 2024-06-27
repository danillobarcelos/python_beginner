str = input("Digite uma palavra: ")

def palindrome(palavra):
    return palavra == palavra[::-1]


if palindrome(str):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

    