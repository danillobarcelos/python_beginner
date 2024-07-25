#Based on Python Tutorial for Beginners' lesson 16 by freeCodeCamp.org

#criar def principal 
# criar loop retorno ao menu principal
# input inicial
# selecionar opções
# implementar argparse

import sys
from rps import rps
from guess_number import advinha_numero

def jogar(nome="Jogador"):
    jogar_dnv = False

    while True:
        if jogar_dnv == True:
            print(f"Olá, {nome}, bem-vindo(a)(e) de volta ao menu principal!")
        
        escolha_jogador = input(f"Por favor, {nome}, escolha entre: \n1 - Pedra, Papel, Tesoura \n2 - Adivinhe o número \nX - Sair do jogo\n")

        if escolha_jogador.lower() not in ['1', '2', 'x']:
            print(f"Por favor, selecione entre 1, 2 ou X")
            return jogar(nome)

    
        jogar_dnv = True

        if escolha_jogador == '1':
            ppt = rps(nome)
            ppt()
        elif escolha_jogador == '2':
            guess_number = advinha_numero(nome)
            guess_number()
        else:
            sys.exit(f"Até a próxima, {nome}!")


#teste = jogar("Dan")
#print(teste())

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Este é o menu de jogos")
    parser.add_argument('-n', '--nome', required=True, help="O nome do jogador da rodada.")

    args = parser.parse_args()

    menu = jogar(args.nome)
    print(f"{args.nome}, bem-vindo(a)(e) ao Arcade!")
    menu()

