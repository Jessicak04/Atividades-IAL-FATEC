#Nos exercícios A e B, crie o quadro resumo, diagrama 
# de Blocos, Algoritmo Descritivo e o código fonte: 
# Distância de um Raio:  Distância = Tempo x 340   
#(340 = velocidade do som no ar em metros por segundo)

#*Quadro Resumo
#Variáveis: tempo (float) e distancia (float)
#Constantes: VELOCIDADE_DO_SOM
#Entrada: tempo (digitado pelo usuário)
#saída: distância percorrida

#*Algoritmo Descritivo
#Iniciar
#Soliciar ao usuário que insira o valor do tempo
#Ler o valor do tempo
#Definir a constante VELOCIDADE_DO_SOM
#Calcular a distância usando a fórmula: distancia = tempo * VELOCIDADE_DO_SOM
#Exibir o valor da distância.
#Finalizar.

#*Código Fonte
tempo = float(input("Qual o tempo em segundos?" ))
VELOCIDADE_DO_SOM = 340 #Velocidade do som no ar em m/s
distancia = tempo * VELOCIDADE_DO_SOM
print("A distância percorrida foi: ", distancia)