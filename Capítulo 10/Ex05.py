#5. Faça um programa que solicite dez números ao usuário, depois disso, exiba todos 
# números pares e só então exiba todos os números ímpares. Utilize a função filter 
# para fazer isso.

def escrever_array(array):
    for valor in array:
        print(valor)

numeros = []
for indice in range(0,10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

pares = filter(lambda numero: numero % 2 == 0, numeros)
impares = filter(lambda numero: numero % 2 == 1, numeros)
escrever_array(pares)
escrever_array(impares)