#2. Faça um programa que inicialize uma lista com os valores de 1 até 10 e 
# depois exiba apenas os números pares utilizando while.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0
while posicao < len(numeros):
    numero = numeros[posicao]
    if numero % 2 == 0:
        print(numero)
    posicao+=1