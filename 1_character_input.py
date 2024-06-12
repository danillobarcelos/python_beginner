ano_atual = 2024

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

ano_cem = ano_atual - idade + 100

msg = (f"Olá, {nome}, você tem {idade} anos. Você irá completar 100 anos em {ano_cem}\n")

n_vezes = int(input("Quantas vezes deseja imprimir a resposta? "))

print(n_vezes * msg)