#6-Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão 
# contendo seu número de identificação e seu peso. Faça um programa que imprima a 
# identificação e o peso do boi mais gordo e do boi mais magro (supondo que não 
# haja empates).

# Algoritmo para encontrar o número e o peso do boi mais gordo e do boi mais magro

# Declaração de variáveis
num = 0
boigordo = 0
boimagro = 0
peso = 0.0
maiorpeso = 0.0
menorpeso = float('inf')  # Inicializa com um valor muito alto

# Função para garantir que o peso seja um número válido
def ler_peso():
    while True:
        try:
            return float(input("Entre com o peso do boi: "))
        except ValueError:
            print("Peso inválido. Por favor, insira um número.")

# Função para garantir que o número de identificação seja um inteiro válido
def ler_numero():
    while True:
        try:
            return int(input("Entre com o número de identificação do boi: "))
        except ValueError:
            print("Número inválido. Por favor, insira um número inteiro.")

# Lê os dados do primeiro boi
num = ler_numero()
peso = ler_peso()

# Inicializa as variáveis que conterão o resultado
boigordo = num
boimagro = num
maiorpeso = peso
menorpeso = peso

# Compara os pesos para encontrar o boi mais gordo e o boi mais magro
for j in range(2, 91):  # De 2 até 90
    num = ler_numero()
    peso = ler_peso()

    # Compara o peso lido com o maior peso até então
    if peso > maiorpeso:
        maiorpeso = peso
        boigordo = num
    elif peso < menorpeso:
        menorpeso = peso
        boimagro = num

# Escreve o número e o peso do boi mais gordo e do boi mais magro
print(f"O número do boi mais gordo é: {boigordo}")
print(f"O peso do boi mais gordo é: {maiorpeso:.2f} kg")
print(f"O número do boi mais magro é: {boimagro}")
print(f"O peso do boi mais magro é: {menorpeso:.2f} kg")
