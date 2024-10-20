#Nos exercícios C e D, crie o quadro resumo, algoritmo 
#descritivo e o código fonte. 

#*Quadro Resumo
#Variáveis: altura (float), TQ (float)
#Constantes: G (float)
#Entrada: altura (digitada pelo usuário)
#saída: TQ 

#*Algoritmo Descritivo
#Iniciar
#Definir a constante G
#Solicitar ao usuário que insira o valor da altura
#Ler altura
#Solicitar ao usuário que insira o valor de TQ
#Ler TQ
#Calcular TQ usando a fórmula: raiz(2*altura)/G
#Exibir o valor de TQ
#Finalizar

#*Código Fonte
G = 9.8
Altura = 0.0
TQ = 0.0

Altura = float(input("Digite a altura: "))
from math import sqrt
TQ = sqrt(2*Altura)/G
print ("O valor é: ", TQ)