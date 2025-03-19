"""
*Configuração Inicial
1. Configure seu nome e e-mail (necessário para commits):

   git config --global user.name "Name"
   git config --global user.email "email"

2. Inicialize o repositório Git na pasta do projeto:
   git init


3. Adicione o repositório remoto (se já existir):
   git remote add origin https://github.com/usuario/repositorio.git

3.1 Para remover:
   git remote remove origin   


4. Baixe as alterações remotas, se houver (para evitar conflitos):
   git pull origin main --rebase

5. Crie um novo branch chamado main e mude para ele:
   git rebase --continue

6. Altere o nome da branch principal para main:
   git branch -m master main
   
----------------------------------------------------------------------------------------------------------------------------
*Fazendo o Primeiro Commit

1. Atualize seu repositório local com as mudanças remotas (opcional, mas recomendado):
   git pull origin main --rebase

2. Adicione os arquivos que deseja rastrear:
   git add .
   > Isso adicionará todos os arquivos ao "staging area". Use git add <nome_do_arquivo> para adicionar arquivos específicos.

3. Crie o commit com uma mensagem descritiva:
   git commit -m "Description"

4. Envie as alterações para o repositório remoto:
   git push -u origin main
"""