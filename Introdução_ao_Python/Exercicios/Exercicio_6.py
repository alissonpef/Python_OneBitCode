"""
* Gerenciamento de Jogadores e Times
-> Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:
- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time

1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.
"""

# Estrutura para armazenar os times e jogadores
teams = {} 
done = False

# Função para listar todos os times
def print_teams():
    print("Times listados:")
    for i, (name, team) in enumerate(teams.items()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# Função para listar os jogadores de um time específico
def print_team_players(team):
    print(f"Jogadores do {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

# Loop principal para interação com o usuário
while not done:
    # Exibir opções para o usuário
    print("\nO que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    # Captura a escolha do usuário
    choice = input("> ")

    # Adicionar um time
    if choice == "1":
        team_name = input("Digite o nome do time: ")
        if team_name in teams:
            print("Time já existe.")
        else:
            teams[team_name] = {'name': team_name, 'players': []}
            print("Time adicionado.")
        
    # Remover um time
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o número do time para remover: "))
        if 1 <= team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            del teams[team_name]
            print("Time removido.")
        else:
            print("Número de time inválido.")
    
    # Listar times
    elif choice == "3":
        print_teams()
    
    # Adicionar jogador em um time
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o número do time para adicionar um jogador: "))
        if 1 <= team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            player_name = input("Informe o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado ao time.")
        else:
            print("Número do time inválido.")
    
    # Remover jogador de um time
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o número do time para remover um jogador: "))
        if 1 <= team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador para remover: "))
            if 1 <= player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num-1]
                print("Jogador removido do time.")
            else:
                print("Número do jogador inválido.")
        else:
            print("Número do time inválido.")
    
    # Listar jogadores de um time
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o número do time para listar jogadores: "))
        if 1 <= team_num <= len(teams):
            team_name = list(teams.keys())[team_num-1]
            print_team_players(teams[team_name])
        else:
            print("Número do time inválido.")
    
    # Sair do programa
    elif choice == "7":
        done = True
    
    # Opção inválida
    else:
        print("Opção inválida.")
