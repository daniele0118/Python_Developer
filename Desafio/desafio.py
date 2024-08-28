menu = """
    Bem vindo ao Sistema Bancário!
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

    =>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("Qual valor deseja depositar?\n")
        deposito = float(input("R$"))
        if deposito > 0:
            saldo += deposito
            print(f"\nSaldo atual: R${saldo:.2f}")
            extrato += f"Depósito no valor de R${saldo:.2f}\n"
        else:
            print("Operação de valor inválido")

    elif opcao == 2:
        if numero_saques < LIMITE_SAQUES:
            print("Qual valor deseja sacar?\n")
            saque = float(input("R$"))
            if saque < saldo:
                saldo -= saque
                print(f"\nSaldo atual: R${saldo:.2f}")
                extrato += f"Saque no valor de R${saldo:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente\n")
        else:
            print("Você chegou ao limite de número de saques!")

    elif opcao == 3:
        print(f"Extrato:\n{extrato}")
        
    elif opcao == 4:
        break

    else:
        print("Operação inválida")