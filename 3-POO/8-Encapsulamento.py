class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # Define como privado
    
    def show(self):
        print(f"Nome: {self.name} Salário: {self.__salary}")
    
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.show()
sicrano.show()

fulano.name = "Fulano 2" # Publico
fulano.__salary = 40000 # Privado

fulano.show()
sicrano.show()
