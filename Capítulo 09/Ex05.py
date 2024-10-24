#5. Faça um programa que inicialize uma lista vazia, depois disso solicite 5 nomes 
# diferentes ao usuário (utilize laço de repetição). Cada nome digitado deve ser 
# adicionado à lista e por fim, todos os nomes devem ser escritos no console. Utilize 
# uma função para solicitar e retornar o nome digitado, uma função para adicionar 
# o nome à lista (passando o nome e a lista por parâmetro) e outra função para 
# escrever todos os nomes no console.

def solicitar_nome():
    return str ( input("Digite um nome: ") )

def adicionar_nome_na_lista(lista, nome):
    lista.append(nome)

def escrever_nomes(lista):
    for nome in lista:
        print(nome)

nomes = []
for contador in range(0,5):
    nome = solicitar_nome()
    adicionar_nome_na_lista(nomes, nome)

escrever_nomes(nomes)