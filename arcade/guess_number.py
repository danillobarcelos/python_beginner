#Based on Python Tutorial for Beginners' lesson 16 by freeCodeCamp.org

# cria def adivinha numero
# cria def onde jogador irá inputar numero + verificaçao de condição
# cria def decidindo ganhador
# imprime resultado - n° rodadas e repetir jogo
# cria loop para jogar novamente
# cria argparse 

import sys
import random

def advinha_numero(nome="Jogador"):
    contador = 0
    vitorias = 0

    def jogador_adivinha():
        nonlocal nome, vitorias

        escolha_jogador = input(f"{nome}, insira um número entre 1, 2 ou 3\n")

        if escolha_jogador not in ["1", "2", "3"]:
            print(f"Por favor, {nome}, insira um número entre 1, 2, ou 3!")
            return jogador_adivinha()
        
        escolha_computador = random.choice("123")

        print(f"{nome} escolheu {escolha_jogador} e Computador escolheu {escolha_computador}")

        jogador = int(escolha_jogador)
        computador = int(escolha_computador)

        def ganhador(jogador, computador):
            nonlocal nome, vitorias

            if jogador == computador:
                vitorias +=1
                return f"Parabéns, {nome}, você venceu!"
            else:
                return f"Poxa, não foi dessa vez {nome}"
        
        resultado = ganhador(jogador, computador)

        print(resultado)

        nonlocal contador
        contador +=1 

        print(f"\nNúmero de jogadas: {contador}")
        print(f"Número de vitórias: {vitorias}")
        print(f"Porcentagem de vitórias: {vitorias/contador:.2%}\n")
        
        print(f"Deseja jogar novamente, {nome}?")

        while True:
            jogar_dnv = input(f"Digite S para sim e N para não... \n")
            if jogar_dnv.lower() not in ['s', 'n']:
                continue
            else:
                break

        if jogar_dnv.lower() == 's':
            return jogador_adivinha()
        elif jogar_dnv == 'n':
            sys.exit(f"Obrigado por jogar, {nome}. Até a próxima...")
        else:
            return
    
    return jogador_adivinha


#teste = advinha_numero("Dan")
#print(teste())

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Adivinhe o número!")
    parser.add_argument('-n', '--nome', required=True, help="Insira o nome do jogador da rodada.")

    args = parser.parse_args()

    guess_number = advinha_numero(args.nome)
    guess_number()
