from Conta_Bancaria import ContaBancaria

contasDict = {}

def showDict():
    if contasDict:
        for numero, conta in contasDict.items():
            print(f"Conta {numero}: Titular: {conta.titular} - Saldo: {conta.getSaldo()}")
    else:
        print("Não há contas cadastradas!")

def addDict():
    numero = int(input("Digite o número da conta: "))
    saldo = 0
    titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(numero, saldo, titular)
    contasDict[numero] = conta

def delDict():
    print("Digite o número da conta que deseja excluir: ")
    showDict()
    numero = int(input(">"))
    if numero in contasDict:
        del contasDict[numero]
        print("Conta excluída com sucesso!")
    else:
        print("Conta inválida!")

def editDict():
    print("Digite o número da conta que deseja editar: ")
    showDict()
    numero = int(input(">"))
    if numero in contasDict:
        conta_obj = contasDict[numero]
        choice = ""
        while choice != "0":
            print("Digite o que deseja fazer: \n1- Depositar saldo \n2- Sacar saldo \n0- Sair")
            choice = input(">")
            if choice == "1":
                valor = float(input("Digite quanto deseja depositar: "))
                conta_obj.deposito(valor)
                print(f"Depósito realizado com sucesso! Novo saldo: {conta_obj.getSaldo()}")
            elif choice == "2":
                valor = float(input("Digite quanto deseja retirar: "))
                conta_obj.retirada(valor)
                print(f"Saque realizado com sucesso! Novo saldo: {conta_obj.getSaldo()}")
            elif choice == "0":
                print("Você saiu do programa!")
                break
            else:
                print("Opção inválida!")
    else:
        print("Conta inválida!")

def showNum():
    numero = int(input("Digite o número da conta que deseja procurar: "))
    if numero in contasDict:
        conta = contasDict[numero]
        print(f"A conta de número {numero} existe!\nTitular: {conta.titular}\nSaldo: {conta.getSaldo()}")
    else:
        print("Conta não encontrada!")
