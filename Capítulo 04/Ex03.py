#3. Faça um programa que solicite a idade do usuário, verifique se o texto 
# informado só contém números. Caso contenha somente números exiba a mensagem: 
# "Você tem {idade digitada} anos.", caso contrário exiba a mensagem: "Você digitou 
# uma idade inválida".

idade_str = input("Quantos anos você tem? ")

if idade_str.isdigit():
    idade = int(idade_str)
    print(f"Você tem {idade} anos.")
else:
    print("Você digitou uma idade inválida")