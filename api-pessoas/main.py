import requests

def pula_linha():
    print("\n")

requisicao = requests.get("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())

pula_linha()

informacao = '{"Nome":"Joice"}','{"Sobrenome":"Saviam"}','{"Idade":30}'
requisicao = requests.post("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/.json", json=informacao)
print(requisicao)
print(requisicao.json())

pula_linha()

informacao2 = {"Nome":"João","Sobrenome":"Marcos","Idade":26}
requisicao2 = requests.patch("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/-Ny7pF86zkOcfXClXorX.json", json=informacao2)
print(requisicao2)
print(requisicao2.json())

pula_linha()

informacao3 = {"Nome":"Ana","Sobrenome":"Maria","Idade":4}
requisicao3 = requests.patch("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/-Ny7pTlugbxS3-aIaUaw.json", json=informacao3)
print(requisicao3)
print(requisicao3.json())

pula_linha()

requisicao4 = requests.delete("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/2.json")
print(requisicao4)
print(requisicao4.json())

pula_linha()

informacao5 = {"Nome":"Isadora","Sobrenome":"Silva","Idade":14}
requisicao5 = requests.patch("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/1.json", json=informacao5)
print(requisicao5)
print(requisicao5.json())

pula_linha()

requisicao = requests.get("https://cotacao-moeda-710fc-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())

pula_linha()
