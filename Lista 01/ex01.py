#O exercício "Ex-for-1" pede que você crie um programa 
#em Python que faça o seguinte:

#Peça ao usuário que insira um número.
#Após receber esse número, o programa deve imprimir 
#odos os números a partir desse número até o número 50.
#A impressão deve ser feita em ordem crescente.
#Em resumo, o objetivo é começar no número que o usuário
# forneceu e listar os números subsequentes até alcançar
# o número 50, incluindo ambos os limites. A estrutura 
#de repetição for deve ser utilizada para realizar essa 
#tarefa de forma eficiente.
#ver coida do isnignt

first_number = int(input("Digite um número: "))
if first_number > 50:
    print("O número deve ser menor ou igual a 50.")
else:
    for number in range(first_number, 51):
        print(number)