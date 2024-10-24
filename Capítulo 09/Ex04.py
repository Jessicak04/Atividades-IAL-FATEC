#4. Faça um programa que solicite ao usuário três números diferentes e exiba o 
# dobro do maior número. Para fazer isso separe seu código em duas funções 
# diferentes: Uma função para retornar o maior dos três números e outra função para 
# dobrar o número.

def obter_maior(numero, numero2, numero3):
    maior = None
    if numero > numero2 and numero > numero3:
        maior = numero
    elif numero2 > numero and numero2 > numero3:
        maior = numero2
    else:
        maior = numero3
    return maior


def dobrar(numero):
    return numero * 2

numero = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = obter_maior(numero,numero2,numero3)
print(dobrar(maior))