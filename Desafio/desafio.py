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
        print("Saque")

    elif opcao == 3:
        print("Extrato")

    elif opcao == 4:
        break

    else:
        print("Operação inválida")