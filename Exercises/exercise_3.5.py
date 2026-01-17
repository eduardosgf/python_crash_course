# Exercise 3.5

pessoas = ['Rebeca', 'José', 'Fabiana']
message = "Quer jantar comigo"

# Lista Original
print("Lista Original:", pessoas) 

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
print("Lista modificada:", pessoas)
print(f"{message} {pessoas[0].title()} ?")
print(f"{message} {pessoas[1].title()} ?")
print(f"{message} {pessoas[2]} ?")

