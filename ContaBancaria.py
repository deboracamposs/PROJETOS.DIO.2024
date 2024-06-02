cliente=input("Insira seu nome: ")
print(f"◘◘◘◘ Bem Vindo ao DIO Bank, {cliente} ◘◘◘◘ \nAqui temos o prazer em lhe atender. \n"
      " \nEscolha uma das opções abaixo:")

menu = """"
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 

Opção escolhida => """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES= 3

print(f"Seu saldo atual é de: {saldo:.2f}.")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
        else:
            print("Operação não realizada. O valor informado é inválido! ")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))


        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Operação falhou. Número máximo de saques excedidos!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n======== EXTRATO ========\n"
              "======= DIO BANK =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSeu saldo atual é de: R$ {saldo:.2f}")
        print("=========================")

    elif opcao == "q":
        print(f"Operação finalizada. Volte sempre, {cliente}")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")