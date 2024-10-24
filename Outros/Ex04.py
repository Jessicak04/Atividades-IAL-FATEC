#2. Faça um programa que inicialize que crie uma lista com os valores de 1 até 10 e 
# depois exiba apenas os números pares.

numeros = list(range(1,11))

for numero in numeros:
    if numero % 2 == 0:
        print(numero)