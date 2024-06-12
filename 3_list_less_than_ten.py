list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def lessthan():
    x = []

    for i in list:
        if i < 5:
            x.append(i)
    print(x)

def lessthanplus():
    x = []

    num = int(input("Informe um número para comparação: "))

    for i in list:
        if i < num:
            x.append(i)
    print(x)

def lessthaninteraction():
    i = 0
    final_list =[]
    list_size = int(input("Digite quantos elementos serão adicionados na sua lista: "))
    new_list = []

    while i < list_size:
        num = int(input("Insira um número na lista: "))
        i += 1
        final_list.append(num)
    print(f"A lista digitada é {final_list}")

    comp = int(input("Digite um número para realizar a comparação: "))
    
    for i in final_list:
        if i < comp:
            new_list.append(i)
    print(f"Os números da lista menores que o valor informado são: {new_list}")

    
    

lessthaninteraction()

lessthanplus()

lessthan()