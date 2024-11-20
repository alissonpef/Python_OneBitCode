# 1. Criar um Ambiente Virtual
# --------------------------------
# Este comando cria um novo ambiente virtual no diretório atual.
# Um ambiente virtual permite isolar as dependências de um projeto Python,
# evitando conflitos com outras bibliotecas e versões instaladas globalmente.
# É especialmente útil para manter o ambiente de desenvolvimento limpo e controlado.

python -m venv .venv

# Explicação do comando:
# - `python`: Executa o interpretador Python instalado no sistema.
# - `-m venv`: Usa o módulo `venv` do Python para criar um novo ambiente virtual.
# - `.venv`: Nome e local onde o ambiente virtual será criado. 
#   `.venv` é uma convenção comum, mas você pode usar outro nome.

# 2. Ativar o Ambiente Virtual
# --------------------------------
# Após criar o ambiente virtual, é necessário ativá-lo para começar a usar.
# A ativação faz com que o terminal utilize os pacotes e bibliotecas instalados
# dentro desse ambiente específico, em vez dos instalados globalmente no sistema.

# Para ambientes Unix-like (Linux, macOS, Git Bash no Windows):
source .venv/Scripts/activate

# Explicação do comando:
# - `source`: Executa o script no ambiente atual do shell.
#   Isso é necessário para alterar as variáveis de ambiente do shell atual.
# - `.venv/Scripts/activate`: Caminho para o script de ativação que configura o ambiente virtual.
#   Esse script ajusta o PATH e outras variáveis para usar o ambiente virtual.

# Nota para usuários do Windows:
# --------------------------------
# Se estiver usando o Prompt de Comando (cmd) do Windows:
.\.venv\Scripts\activate

# Se estiver usando o PowerShell no Windows:
# Pode ser necessário ajustar a política de execução antes de ativar o ambiente virtual:
Set-ExecutionPolicy RemoteSigned
# Em seguida, ative o ambiente:
.\.venv\Scripts\Activate

# Após ativar, você verá o nome do ambiente (por exemplo, `.venv`) no início do prompt,
# indicando que o ambiente virtual está ativo.
