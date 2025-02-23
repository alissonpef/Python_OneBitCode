from Conta_Bancaria import ContaBancaria
from Conta_Corrente import ContaCorrente
import Sistema_Bancario

choice = "-1"

while choice != "0":
    print(
        "\n\nDigite o que você deseja fazer: \n1- Abrir uma conta. \n2- Depositar. \n3- Sacar. \n4- Visualizar extrato bancário. \n5- Listar contas. \n0- Sair."
    )
    choice = input(">")

    if choice == "1":
        numero = int(input("Digite o número da conta: "))
        saldo = 0
        titular = input("Digite o nome do titular da conta: ")
        tipo_conta = input("Digite o tipo de conta (corrente/poupança): ").lower()

        if tipo_conta == "corrente":
            limite = float(input("Digite o limite do cheque especial: "))
            tarifa = float(input("Digite a tarifa mensal: "))
            conta = ContaCorrente(numero, saldo, titular, limite, tarifa)
        else:
            conta = ContaBancaria(numero, saldo, titular)

        Sistema_Bancario.contasDict[numero] = conta
        print(f"Conta {numero} criada com sucesso!")

    elif choice == "2":
        numero = int(input("Digite o número da conta para depósito: "))
        valor = float(input("Digite o valor do depósito: "))
        if numero in Sistema_Bancario.contasDict:
            conta = Sistema_Bancario.contasDict[numero]
            conta.deposito(valor)
            print(f"Depósito de {valor} realizado com sucesso!")
        else:
            print("Conta não encontrada!")

    elif choice == "3":
        numero = int(input("Digite o número da conta para saque: "))
        valor = float(input("Digite o valor do saque: "))
        if numero in Sistema_Bancario.contasDict:
            conta = Sistema_Bancario.contasDict[numero]
            conta.retirada(valor)
            print(f"Saque de {valor} realizado com sucesso!")
        else:
            print("Conta não encontrada!")

    elif choice == "4":
        numero = int(input("Digite o número da conta para extrato: "))
        if numero in Sistema_Bancario.contasDict:
            conta = Sistema_Bancario.contasDict[numero]
            conta.extrato()
        else:
            print("Conta não encontrada!")

    elif choice == "5":
        Sistema_Bancario.showDict()

    elif choice == "0":
        print("Você saiu do programa!")
        break

    else:
        print("Opção inválida!")
