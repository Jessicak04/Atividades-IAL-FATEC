#A) QUADRO RESUMO (RQ): Para montar o QR, vamos considerar
# o cálculo da ÁREA de um círculo e responder as 4 
# questões a seguir com base na análise da fórmula a 
# seguir:

#Fórmula em Evidência: ÁREA = RAIO * RAIO * 3.14

#1) Quais são as variáveis e constantes e seus valores 
#iniciais da fórmula em evidência ? ÁREA = 0, RAIO = 0, 
#PI = 3.14 (Deve-se dar nomes às constantes)

raio = 0
area = 0
pi = 3.14

#1) Quais as variáveis que deverão ser digitadas, 
# isto é, Variáveis de Leitura ?

raio = int(input("Digite o raio do circulo: "))

#13 1) Qual(is) a(s) fórmula (s) do programa em 
# sequência e ordem correta?
#ÁREA = RAIO * RAIO * PI

area = raio * raio * pi

#1) Qual (is) as variáveis de resultado, isto é, de 
# Saída que serão exibidas ou impressas no video ?

print("A área do circulo é:", area)