# Python usa a identação para separar blocos
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente, tenha um ótimo dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)

# A estrutura condicional permite o desvio de fluxo quando determinadas expressões lógicas são atendidas

saldo = 2000.0
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:
    print("Realizando saque")
else:
    print("Saldo insuficiente")

opcao = int(input("Informe uma opção: \n[1]Sacar \n[2]Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else: 
    sys.exit("Opção inválida")

# Estruturas de condição
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

# Exemplo 1
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")

# Exemplo 2
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

# Exemplo 3
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH.")

# Estruturas condicionais aninhadas

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 450
if conta_normal: 
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
elif conta_especial:
    print("Conta especial selecionada")
else:
    print("Sistema não reoconheceu esse tipo de conta, entre em contato com o seu gerente.")


# If ternário
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")