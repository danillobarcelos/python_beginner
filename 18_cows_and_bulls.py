import random

def compare_guessing(original, guess):
    cows = bulls = 0
    o = list(str(original))
    g = list(str(guess))

    for i in range(len(o)):
        if o[i] == g[i]:
            cows += 1
            g[i] = o[i] = None

    for char in o:
        if char is not None and char in g:
            bulls += 1
            g[g.index(char)] = None
    
    resultado = [cows, bulls]
    return resultado


def main_game():
    original = random.randint(1000, 9999)
    tentativas = 0

    while True:        
        entrada = str(input("Digite um número de 4 digitos: "))
        if len(entrada) != 4:
            print("O número deve ter exatos 4 digitos")
        else:
            resultado = compare_guessing(original, entrada)
            cows = resultado[0]
            bulls = resultado[1]
        
        if cows != 4:
            if cows < 4:
                tentativas += 1
                print(f'Cows = {cows}. Bulls = {bulls}')
                print(f'Essa é a sua tentativa número {tentativas} \n')
            else:
                pass
        elif cows == 4:
            tentativas += 1
            print(f'Cows = {cows}. Bulls = {bulls}')
            print(f'Parabéns, você venceu! Foram necessárias {tentativas} tentativas. \n')
            break

if __name__ == "__main__":
    main_game()