#4. Faça um programa que tenha uma lista com 5 de pessoas, onde cada pessoa tem seu nome e sobrenome armazenado em um dicionário, depois disso, exiba todos os nomes e sobrenomes. Para complicar um pouco as coisas, vamos simular que estes dados foram obtidos da web e com isso recebemos algumas inconsistências. Duas das cinco pessoas possuem o dicionário onde as chaves estão em maiúsculo e os outros três em minúsculo.
#pessoas = [
#    {"nome": "Joãozinho", "sobrenome": "da Silva" },
#    {"NOME": "Mariazinha", "SOBRENOME": "de Souza" }, 
#    {"nome": "Gabriel", "sobrenome": "Schade" },
#    {"NOME": "Joana", "SOBRENOME": "da Silva" },
#    {"nome": "Everton", "sobrenome": "Schmit" },
#]

#for pessoa in pessoas:
#    nome = pessoa.get("nome", None)
#    sobrenome = pessoa.get("sobrenome", None)
#    if not nome:
#        nome = pessoa.get("NOME", None)
#    if not sobrenome:
#        sobrenome = pessoa.get("SOBRENOME", None)

#    print(nome, sobrenome)

pessoas = [
    {"nome": "Joãozinho", "sobrenome": "da Silva" },
    {"NOME": "Mariazinha", "SOBRENOME": "de Souza" }, 
    {"nome": "Gabriel", "sobrenome": "Schade" },
    {"NOME": "Joana", "SOBRENOME": "da Silva" },
    {"nome": "Everton", "sobrenome": "Schmit" },
]

for pessoa in pessoas:
    nome = pessoa.get("nome", None)
    sobrenome = pessoa.get("sobrenome", None)
    if not nome:
        nome = pessoa.get("NOME", None)
    if not sobrenome:
        sobrenome = pessoa.get("SOBRENOME", None)

    print(nome, sobrenome)
