def fibonacci():
    numero = int(input("Quantos números de Fibonacci você gostaria de gerar? "))
    fib = []
    n = 1

    if numero == 0:
        fib = []
    elif numero == 1:
        fib = [1]
    elif numero == 2:
        fib = [1,1]
    elif numero > 2:
        fib = [1,1]

        while n < (numero - 1):
            fib.append(fib[n] + fib[n-1])
            n += 1
    return fib

print(fibonacci())
