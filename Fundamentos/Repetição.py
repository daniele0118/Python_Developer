# Estruturas de repetição são utilizadas para repetir um trecho de código um determinado número de vezes
#Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

# Utilizando range(start, stop, step)

for numero in range(0, 11):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")


# While

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Scar\n[2] Extrato \n[0] Sair:\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else: 
    print("Obrigada por utilizar nosso sistema bancário, até logo!")

# Break

while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(numero)

    for numero in range(100):

        if numero == 12:
            break
        
        print(numero, end=" ")