#2. Faça um programa que solicite o nome do usuário e a idade do usuário, depois 
# disso exiba a mensagem: "{nome} possui {idade} anos.". Esta mensagem deve ser 
# escrita em uma função.

def escrever_nome_idade(nome, idade):
    print(nome, "possui",idade,"anos.")

nome_digitado = str(input("Digite seu nome: "))
idade_digitada = int(input("Digite sua idade: "))

escrever_nome_idade(nome_digitado, idade_digitada)