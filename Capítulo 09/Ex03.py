#3. Faça um programa que solicite dois números ao usuário e exiba a multiplicação 
# deles. A multiplicação deve ser calculada em uma função.

def multiplicar(numero, numero2):
    return numero * numero2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = multiplicar(numero, numero2)
print(resultado)