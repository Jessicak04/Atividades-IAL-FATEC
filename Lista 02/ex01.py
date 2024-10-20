#Nos exercícios A e B, crie o quadro resumo, diagrama 
# de Blocos, Algoritmo Descritivo e o código fonte: 
# a)Área do Triângulo: Área = Base  x  Altura / 2

#*Quadro Resumo
#Variáveis: base (float), altura (float) e area (float)
#Entrada: base (digitado pelo usuário), altura (digitada pelo usuário)
#Saída: area (calculada e exibida)

#*Algoritmo Descritivo
#Iniciar
#Solicitar ao usuário que insira o valor da base.
#Ler o valor da base.
#Solicitar ao usuário que insira o valor da altura.
#Ler o valor da altura
#Calcular a área usando a fórmula: area = base * altura / 2.
#Exibir o valor da área.
#Finalizar.

#*Código Fonte
base = float(input("Digite a Base do triângulo: "))
altura = float(input("Digite a Altura do triângulo: "))
area = base * altura / 2
print("O tamanho da Área do triângulo é: ", area)