import random as rd

possibilidades = {
    "pedra": {"pedra":"empatou", "papel":"perdeu", "tesoura":"ganhou"},
    "papel": {"pedra":"ganhou", "papel":"empatou", "tesoura":"perdeu"},
    "tesoura": {"pedra":"perdeu", "papel":"ganhou", "tesoura":"empatou"}
}

opcoes = ["pedra", "papel", "tesoura"]

nova_partida = 's'

def rock_paper_scissor():
    try:
        jogador = input('Escolha entre as opções "Pedra, papel e tesoura" ').lower()
        computador = rd.choice(opcoes)
        resultado = possibilidades[jogador][computador]

        print(f'Jogador escolheu {jogador} e o computador escolheu {computador}')
        print(f"Jogador {resultado}")          
    except:
        print("Digite uma entrada valida! ")
        rock_paper_scissor()

while nova_partida == 's':
    rock_paper_scissor()
    nova_partida = input("Deseja jogar novamente? (Digite 's' para SIM ou qualquer tecla para NÃO) ")
        




