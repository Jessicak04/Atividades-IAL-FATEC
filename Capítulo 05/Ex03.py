#3. Faça um programa que inicialize uma lista com vários números diferentes, depois 
# disso, solicite ao usuário um número, verifique se o número está ou não na lista e 
# exiba uma mensagem notificando o usuário do resultado.

numeros = [2,4,7,11,6,9]
numero_digitado = int(input("Digite um número: "))
if numero_digitado in numeros:
    print(f"O número {numero_digitado} está na lista")
else:
    print(f"O número {numero_digitado} não está na lista")