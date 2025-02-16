class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome: {self.name} Salário: {self.__salary}")
    
    # Método para buscar os dados
    def get_salary(self):
        return self.__salary
    
    # Método para alterar atributo privado
    def set_salary(self, salary):
        self.__salary = salary
    
fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)

fulano.name = "Fulano 2"
fulano.set_salary(40000)

fulano.show()
sicrano.show()
