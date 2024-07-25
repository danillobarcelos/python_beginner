#Based on Python Tutorial for Beginners' lesson 16 by freeCodeCamp.org

import sys
import random
from enum import Enum

def rps(nome="Jogador"):
    contador = 0
    j_ganhou = 0
    p_ganhou = 0

    def jogar():
        nonlocal nome, j_ganhou, p_ganhou

        class RPS(Enum):
            PEDRA = 1
            PAPEL = 2
            TESOURA = 3

        escolha_j = input(f"{nome}, por favor digite: \n1 para Pedra, \n2 para Papel ou \n3 para Tesoura\n\n")

        if escolha_j not in ["1", "2", "3"]:
            print(f"Por favor, {nome}, escolha entre 1, 2 ou 3")
            return jogar()
        
        escolha_p = random.choice("123")

        jogador = int(escolha_j)
        python = int(escolha_p)

        print(f"{nome}, você escolheu {str(RPS(jogador)).replace('RPS.', '').title()} e Python escolheu {str(RPS(python)).replace('RPS.','').title()}")

        def campeao(jogador, python):
            nonlocal nome, j_ganhou, p_ganhou

            if jogador == 1 and python == 3:
                j_ganhou += 1
                return f"Parabéns, {nome}, você ganhou!"
            elif jogador == 2 and python == 1:
                j_ganhou += 1
                return f"Parabéns, {nome}, você ganhou!"
            elif jogador == 3 and python == 2:
                j_ganhou += 1
                return f"Parabéns, {nome}, você ganhou!"
            elif jogador == python:
                return "Empate!"
            else: 
                p_ganhou += 1
                return "Python ganhou!"
            
        resultado_jogo = campeao(jogador, python)
            
        print(resultado_jogo)

        nonlocal contador
        contador += 1

        print(f"\nRodadas: {contador}")
        print(f"Rodadas vencidas por {nome}: {j_ganhou}")
        print(f"Rodadas vencidas pelo Python: {p_ganhou}\n")

        print(f"{nome}, deseja jogar novamente? \n")

        while True:
            jogar_dnv = input(f"S para sim e N para não\n")
            if jogar_dnv.lower() not in ['s', 'n']:
                continue
            else: 
                break

        if jogar_dnv.lower() == "s":
            return jogar()
        elif jogar_dnv.lower() == "n":
            sys.exit("Obrigado(a) por jogar! Até a próxima")
        else:
            return

    return jogar


#teste = rps("Dan")
#print(teste())

#testando modulo argparse

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pedra, papel ou tesoura!")
    parser.add_argument('-n', "--nome", required=True, help="Nome do jogador")

    args = parser.parse_args()

    ppt = rps(args.nome)
    ppt()
