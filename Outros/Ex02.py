#2.	Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus 
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por 
# cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve 
# vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou 
# seja, um total de $470. Escreva um programa (usando um array de contadores) que 
# determine quantos vendedores receberam salários nos seguintes intervalos de 
# valores:
#a.	$200 - $299
#b.	$300 - $399
#c.	$400 - $499
#d.	$500 - $599
#e.	$600 - $699
#f.	$700 - $799
#g.	$800 - $899
#h.	$900 - $999
#i.	$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem 
# fazer vários ifs aninhados.


num_vendedores = int(input('Quantos vendedores a loja tem? '))

salarios = []
classe = []
for vendedor in range(1,num_vendedores+1):
    vendas = float(input('\nQuanto o vendedor '+str(vendedor)+' arrecadou essa semana? '))
    salarios.append(200+(vendas*0.09))

dicionario = {'1':[range(200,299),0],
              '2':[range(300,399),0],
              '3':[range(400,499),0],
              '4':[range(500,599),0],
              '5':[range(600,699),0],
              '7':[range(700,799),0],
              '8':[range(800,899),0],
              '9':[range(900,999),0]}  


for salario in salarios:
    for idx in dicionario.keys():
        if salario in dicionario[idx][0]:
            classe.append(idx)
            dicionario[idx][1] += 1     

print("\nClassificação dos salários:")
for key, value in dicionario.items():
    print(f"Classe {key}: {value[1]} vendedor(es)")

