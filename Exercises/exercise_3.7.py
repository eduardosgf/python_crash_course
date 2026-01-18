#Exercise 3.7

pessoas = ['Rebeca', 'José', 'Fabiana']
message = "Quer jantar comigo"

# Lista Original
print("Convite Original:", pessoas) 

# Convite para lista original
print(f"{message} {pessoas[0].title()} ?")
print(f"{message} {pessoas[1].title()} ?")
print(f"{message} {pessoas[2].title()} ?")

# Remove alguem
nao_vai = "Nao vai ir ao jantar"
desistiu = pessoas.pop()

print(f"{desistiu.title()} {nao_vai}")

# Adiciona uma pessoa
pessoas.insert(0, 'Brenda')

#Convite lista modificada
print("Convite modificada:", pessoas)
print(f"{message} {pessoas[0].title()} ?")
print(f"{message} {pessoas[1].title()} ?")
print(f"{message} {pessoas[2]} ?")

print("Encontramos uma mesa maior para o jantar")

p1 = pessoas.insert(0, 'Bruno')
pessoas.insert(2, 'Cleusita')
pessoas.append('Ovidio')

print("Convidados adicionado a lista:", pessoas)

for pessoa in pessoas:
    print(f"{message} {pessoa.title()} ?")

print("Mesa reduzida posso convidar apenas 2 pessoas")

print("Perdão por remove-lo", pessoas[0])
pessoas.pop(0)
print(pessoas)

print("Perdão por remove-lo", pessoas[0])
pessoas.pop(0)
print(pessoas)

print("Perdão por remove-lo", pessoas[0])
pessoas.pop(0)
print(pessoas)

print("Perdão por remove-lo", pessoas[2])
pessoas.pop(2)
print(pessoas)

print("Vocês ainda estão convidados", pessoas)
del pessoas[0]
del pessoas[0]
print(pessoas)


