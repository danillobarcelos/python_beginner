import random 

chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
numbers = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']

def senha_fraca(): #8-10 letras aleatórias
    num_char = random.randint(8,10)
    resultado = []

    for _ in range(num_char):
        resultado.append(random.choice(chars))
    
    return "".join(resultado)

def senha_media():
    num_char = random.randint(11, 16)
    resultado = []

    for _ in range(num_char):
        resultado.append(random.choice(chars + numbers))
    
    return "".join(resultado)

def senha_forte():
    num_char = random.randint(17, 25)
    resultado = []

    for _ in range(num_char):
        resultado.append(random.choice(chars + numbers + symbols))
    
    return "".join(resultado)
        
def escolha_senha():
    try:
        dificuldade = input("Digite o nível da senha que gostaria entre as opções: \n Fraca \n Média \n Forte \n").lower()

        if dificuldade == "fraca":
            print(senha_fraca())
        elif dificuldade == "média" or dificuldade == "media":
            print(senha_media())
        elif dificuldade == "forte":
            print(senha_forte())
        else:
            raise ValueError("Opção inválida...")
    except Exception as e: 
        print(f'Ah não... Ocorreu um erro de {e}. Por favor, escolha uma opção válida')
        escolha_senha()


escolha_senha()