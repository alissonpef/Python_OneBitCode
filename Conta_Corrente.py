from Conta_Bancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, numero, saldo, titular, limite_cheque_especial, tarifa_mensal):
        super().__init__(numero, saldo, titular)
        self.__limite_cheque_especial = limite_cheque_especial
        self.__tarifa_mensal = tarifa_mensal

    def getTarifas(self):
        return self.__limite_cheque_especial, self.__tarifa_mensal

    def setTarifas(self, limite_cheque_especial, tarifa_mensal):
        self.__limite_cheque_especial, self.__tarifa_mensal = (
            limite_cheque_especial,
            tarifa_mensal,
        )

    def showTarifas(self):
        limite_cheque_especial, tarifa_mensal = self.getTarifas()
        print(
            f"A conta {ContaBancaria.titular} tem um limite de cheque especial de: {limite_cheque_especial} e uma tarifa mensal de {tarifa_mensal}"
        )

    def extrato(self):
        name = ContaBancaria.getNomeArquivo()
        print("-----EXTRATO DA CONTA-----\n")
        with open(name, "r", encoding="UTF-8") as file:
            for line in file:
                print(f"{line.rstrip()}")
