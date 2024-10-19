#Nos exercícios C e D, crie o quadro resumo, algoritmo 
# descritivo e o código fonte. 

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