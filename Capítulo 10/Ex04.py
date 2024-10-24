#4. Faça um programa que solicite cinco números ao usuário, depois disso, exiba 
# apenas os números maiores do que 10. Utilize a função filter para fazer isso.

numeros = []
for indice in range(1,5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maiores = filter(lambda numero: numero > 10, numeros)
for maior in maiores:
    print(maior)