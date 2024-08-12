nome = "Dani"
idade = 23
profissao = "Desenvolvedora"
linguagem = "Python"
saldo = 45.435

dados = {"nome":"Dani", "idade": 223}

print("Nome: %s Idade: %d" % (nome,idade))

print("Nome: {} Idade: {}" .format(nome,idade))

print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome))

print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} Nome: {name}" .format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")



