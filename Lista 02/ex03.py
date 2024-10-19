#Nos exercícios C e D, crie o quadro resumo, algoritmo 
#descritivo e o código fonte. 

G = 9.8
Altura = 0.0
TQ = 0.0

Altura = float(input("Digite a altura: "))
from math import sqrt
TQ = sqrt(2*Altura)/G
print ("O valor é: ", TQ)