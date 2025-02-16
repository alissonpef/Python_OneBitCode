"""
Exercicio 2:
* Agenda de Contatos:
-> Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve seguir as especificidades:
1. Criar o arquivo Agenda contendo quatro métodos: 
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para remover contatos.
2. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos 
desenvolvidos de acordo com a opção escolhida.
"""

from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete all contacts")
        print("0. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

main()