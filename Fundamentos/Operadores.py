produto_1 = 10
produto_2 = 20

# Aritimeticos
print(produto_1 + produto_2 + 3.5)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10+5) * 4
y = 10 / 2 + (25 * 2) - (2 ** 2)
print(x)
print(y)
# Python segue a ordem de operações a serem executadas primeiro como na matemática


# Comparação
saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

# Atribuição
saldo = 500
print(saldo)

saldo = 200
print(saldo)

saldo += 10
print(saldo)

saldo -= 5
print(saldo)

saldo /= 2
print(saldo)

saldo //= 2
print(saldo)

saldo *= 10
print(saldo)

saldo %= 4
print(saldo)

saldo **= 2
print(saldo)

# Lógicos
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <= limite)

#Operador de negação

print(not 1000 > 1500)

# Lista vazia é considerada false
contatos_emergencia = []
print(not contatos_emergencia)

#String verdadeira (tem valor)
print(not "saque 1500;")

#String falsa (vazia)
print(not "")

#Parênteses servem para delimitar a precedência
saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
(saldo >= saque and saque <= limite) or ( conta_especial and saldo >= saque)

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

#Operadores

curso = "curso de Python"
nome_curso = curso
saldo, limite = 200, 200

#Is compara se ambos estão na mesma posição de memória
print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)

saldo = 1000
limite = 100

print(saldo is limite)
print(saldo is not limite)

#Associação
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

print("maçã" not in frutas)

print(200 in saques)
