numero = 1
quantidade = 0

while numero != 0:
    numero = int(input("Digite um número (0 para parar): "))

    if numero > 0:
        quantidade = quantidade + 1

print("Quantidade de números positivos:", quantidade)