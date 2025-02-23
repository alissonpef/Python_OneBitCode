from Conta_Bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, saldo, titular, limite_cheque_especial, tarifa_mensal):
        super().__init__(numero, saldo, titular)
        self.limite_cheque_especial = limite_cheque_especial
        self.tarifa_mensal = tarifa_mensal

    def getTarifas(self):
        return self.__limite_cheque_especial, self.__tarifa_mensal

    def setTarifas(self, limite_cheque_especial, tarifa_mensal):
        self.__limite_cheque_especial = limite_cheque_especial
        self.__tarifa_mensal = tarifa_mensal

    def showTarifas(self):
        limite_cheque_especial, tarifa_mensal = self.getTarifas()
        print(f"A conta de {self.titular} tem limite de cheque especial: {limite_cheque_especial} e tarifa mensal: {tarifa_mensal}")

    def extrato(self):
        nome_arquivo = self.getNomeArquivo()
        print("\n-----EXTRATO DA CONTA-----\n")
        try:
            with open(nome_arquivo, "r", encoding="UTF-8") as file:
                for line in file:
                    print(line.rstrip())
        except FileNotFoundError:
            print("Nenhum extrato encontrado.")
