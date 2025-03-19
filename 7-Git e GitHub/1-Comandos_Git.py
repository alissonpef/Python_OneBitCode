"""
*Comandos Básicos do Git

1. Inicializar um repositório:
   git init

2. Verificar o status do repositório:
   git status

3. Adicionar arquivos ao staging:
   git add <arquivo>
   git add .  # Adiciona todos os arquivos modificados

4. Remover arquivos do staging:
   git rm --cached <arquivo>

5. Criar um commit com uma mensagem descritiva:
   git commit -m "Mensagem do commit"

6. Ver histórico de commits:
   git log

7. Comparar alterações entre versões:
   git diff

8. Restaurar arquivo para a versão do último commit:
   git restore <arquivo>

----------------------------------------------------------------------------------------------------------------------------
*Fluxo de Trabalho com Git

1. Inicialize o repositório se ainda não estiver inicializado:
   git init

2. Adicione arquivos ao staging:
   git add .

3. Faça o commit das alterações:
   git commit -m "Descrição das mudanças"

4. Conecte ao repositório remoto (se necessário):
   git remote add origin https://github.com/usuario/repositorio.git

5. Envie as alterações para o repositório remoto:
   git push -u origin main
"""