"""
Exercício Final:
* Gerenciamento de Jogadores e Times:
-> Escreva um programa em python que realize o gerenciamento de jogadores.
Ele deve atender aos seguintes requisitos:
1 - A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2 - A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3 - A opção de remover um time deve pedir um índice específico do time que foi cadastrado para fazer a sua exclusão.
4 - A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5 - A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador do time.
6 - A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.
"""

times = {}
choice = -1


def newTime():
    name = input("Digite o nome do time: ")
    index = len(times)
    times[index] = {"índice": index, "nome": name, "jogadores": []}
    print(f"Time '{name}' adicionado com sucesso!")


def removeTime():
    print(times)
    index = int(input("Digite o índice do time que deseja remover: "))
    if index in times:
        name = times[index]
        del times[index]
        print(f"Time {name['nome']} removido com sucesso!")
    else:
        print("Índice inválido! Não há time com esse índice.")


def newPlayer():
    print(times)
    index = int(input("Digite o índice do time que deseja adicionar o jogador: "))
    if index in times:
        name = input("Digite o nome do jogador: ")
        times[index]["jogadores"].append(name)
        print(f"Jogador '{name}' adicionado com sucesso!")
    else:
        print("Índice inválido! Não há time com esse índice.")


def removePlayer():
    print(times)
    index = int(input("Digite o índice do time que deseja remover o jogador: "))
    if index in times:
        print(times[index]["jogadores"])
        name = input("Digite o nome do jogador que deseja remover: ")
        if name in times[index]["jogadores"]:
            times[index]["jogadores"].remove(name)
            print(f"Jogador {name} removido com sucesso!")
        else:
            print("Jogador não encontrado no time!")
    else:
        print("Índice inválido! Não há time com esse índice.")


while choice != 0:
    choice = int(
        input(
            "\nDigite a opção desejada: \n1 - Listar os times. \n2 - Adicionar um time. \n3 - Remover um time."
            "\n4 - Adicionar um jogador. \n5 - Remover um jogador. \n6 - Listar jogadores. \n0 - Sair!\n> "
        )
    )
    if choice == 1:
        if len(times) == 0:
            print("Não há times cadastrados!")
        else:
            for i in range(len(times)):
                if len(times[i]["jogadores"]) != 0:
                    print(
                        f" {i} - Time: {times[i]['nome']} \nNúmero de jogadores: {len(times[i]['jogadores'])}"
                    )
                else:
                    print(f" {i} - Time: {times[i]['nome']} \nNúmero de jogadores: 0")
    elif choice == 2:
        newTime()
    elif choice == 3:
        removeTime()
    elif choice == 4:
        newPlayer()
    elif choice == 5:
        removePlayer()
    elif choice == 6:
        print(times)
        index = int(input("Digite o índice do time que deseja ver os jogadores: "))
        if index in times:
            print(times[index]["jogadores"])
        else:
            print("Índice inválido! Não há time com esse índice.")
    elif choice == 0:
        print("Encerrando o programa!")
    else:
        print("Opção inválida!")
