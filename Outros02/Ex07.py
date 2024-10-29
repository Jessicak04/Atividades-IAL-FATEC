#7-Faça um programa que leia vários números inteiros e apresente o fatorial de 
# cada número. O algoritmo encerra quando se digita um número menor do que 1.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

while True:
    numero = int(input("Digite um número inteiro (menor que 1 para encerrar): "))
    
    if numero < 1:
        print("Programa encerrado.")
        break
    print(f"O fatorial de {numero} é {fatorial(numero)}")

