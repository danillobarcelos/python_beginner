entrada = int(input("Por favor, digite um número: "))

if entrada%4 == 0:
    print("Este número é multiplo de 4")
    if entrada % 2 == 0:
        print("Este número é par!")
else:
    print("Esté número é impar!")

num = int(input("Agora digite um númerador: "))
div = int(input("E digite também um divisor: "))

if num%div ==0:
    print("Que legal! Os números se dividem sem deixar nenhum resto")
else: 
    print("Poxa, essa não é uma divisão inteira :(")


