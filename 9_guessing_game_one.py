import random as rd

random_num = rd.randint(1,9)


print('Bem vindo(a). Caso deseje sair insira a palavra "exit"')
user_guess = input("Adivinhe um número inteiro entre 1-9: ")
counter = 0
tries = 0

while user_guess != "exit":
    try:
        if int(user_guess) > random_num and int(user_guess) < 10:
            print("Número escolhido é maior! Tente novamente. ")
        elif int(user_guess) < random_num and int(user_guess)> 0:
            print("Número escolhido é menor! Tente novamente. ")
        elif int(user_guess) == random_num:
            print("Número escolhido é igual, você acertou!!!")
            counter += 1
            random_num = rd.randint(1,9)
        else: 
            print("Escolha um número entre 1 e 9!!!")
    except:
        print("Digite um NÚMERO valido!")
    
    tries += 1
    user_guess = input("Adivinhe um número inteiro entre 1-9: ")

print(f'Obrigado por jogar! Seu placar foi de {counter} ponto(s) em {tries} tentativas')
    

    
