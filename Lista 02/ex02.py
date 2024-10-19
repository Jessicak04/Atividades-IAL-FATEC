#Nos exercícios A e B, crie o quadro resumo, diagrama 
# de Blocos, Algoritmo Descritivo e o código fonte: 
# Distância de um Raio:  Distância = Tempo x 340   
#(340 = velocidade do som no ar em metros por segundo)

tempo = float(input("Qual o tempo em segundos?" ))
VELOCIDADE_DO_SOM = 340 #Velocidade do som no ar em m/s
distancia = tempo * VELOCIDADE_DO_SOM
print("A distância percorrida foi: ", distancia)