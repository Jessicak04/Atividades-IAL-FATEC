#Nos exercícios C e D, crie o quadro resumo, algoritmo 
# descritivo e o código fonte. 

#*Quadro Resumo
#Variáveis: perimetro (float), diametro (float), raio (float) e area (float).
#Constantes: PI (float)
#Entrada: perimetro (digitado pelo usuário)
#saída: Resultados de diametro, raio e area

#*Algoritmo Descritivo
#Iniciar
#Definir a constante PI
#Solicitar ao usuário que insira o valor de perimetro
#Ler perimetro
#Calcular o diâmetro peloa fórmula: diametro = perimetro/PI
#Calcular o raio pela fórmula: raio = diametro / 2
#Calcular a área pela fórmula: area = raio * raio * PI
#Exibir os resultados do diâmetro, raio e área
#Finalizar

#*Código Fonte
diametro = 0
perimetro = 0
raio = 0
area = 0
PI = 3.14

perimetro = float(input("Qual o perimetro? "))
diametro = perimetro / PI
raio = diametro/2
area = raio * raio * PI

print("Com base no perimetro, os resultados são: ", '\n' , 
      "Diametro: ", diametro , '\n' ,
      "Raio: ", raio , '\n',
      "Área: ", area)