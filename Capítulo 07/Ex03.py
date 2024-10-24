#3. Faça um programa que inicialize uma lista vazia, solicite ao usuário 10 números 
# ímpares diferentes, um por vez. Caso o número digitado seja par, solicite novamente 
# um número, até que o valor seja um número ímpar. Depois disso, exiba os 10 números 
# digitados.

numeros = []
numero = 0
quantidade_sobrando = 10
while quantidade_sobrando > 0:
    numero = 0
    while numero % 2 == 0:
        numero = int( input("Digite um número ímpar: ") )

    numeros.append(numero)
    quantidade_sobrando -= 1

posicao = 0

while posicao < len(numeros):
    print(numeros[posicao])
    posicao += 1