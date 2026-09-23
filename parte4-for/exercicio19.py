numero = int(input("Digite um número: "))

fatorial = 1

for valor in range(1, numero + 1):
    fatorial = fatorial * valor

print("Fatorial:", fatorial)