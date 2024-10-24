#4. Faça um programa que exiba um menu para o usuário selecionar uma das três opções:

#•	1 - Olá mundo
#•	2 - Eu programo em Python
#•	3 - Laços de repetição

#O programa deve solicitar ao usuário uma das 3 opções, caso o usuário digite um 
# valor diferente das opções (1, 2 ou 3), o programa deve apresentar novamente o 
# menu de opções até que uma delas seja escolhida. Por fim, o programa deve exibir 
# uma mensagem diferente para cada opção.

opcao = 0
opcoes = [1, 2, 3]
while opcao not in opcoes:
    print("Selecione uma das opções abaixo: ")
    print("1 - Olá mundo ")
    print("2 - Eu programo em Python ")
    print("3 - Laços de repetição ")
    opcao = int ( input ("Selecione a opção: ") )

if opcao == 1:
    print("Olá mundo!")
elif opcao == 2:
    print("Já estou na minha sexta lição de Python!")
else:
    print("Nesta lição estou estudando o laço de repetição While")

