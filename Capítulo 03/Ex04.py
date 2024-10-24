#4. Faça um programa que solicite ao usuário 2 valores, utilize uma condição 
# ternária para escrever qual o maior valor: o primeiro ou o segundo 
# (caso os valores sejam iguais, considere o segundo).

primeiro_valor = int( input("Digite um valor: "))
segundo_valor = int( input("Digite um valor: "))
print( "Primeiro" if primeiro_valor > segundo_valor else "Segundo")