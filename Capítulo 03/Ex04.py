#4. Faça um programa que solicite ao usuário 2 valores, utilize uma condição 
# ternária para escrever qual o maior valor: o primeiro ou o segundo 
# (caso os valores sejam iguais, considere o segundo).

primeiro_valor = int( input("Digite o primeiro valor: "))
segundo_valor = int( input("Digite o segundo valor: "))
if primeiro_valor > segundo_valor:
    print("Primeiro valor é maior")
else: 
    print("Segundo valor é maior")