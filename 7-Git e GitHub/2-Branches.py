"""
*Trabalhando com Branches no Git*

1. Verificar as branches existentes no repositório:
   git branch

2. Criar uma nova branch:
   git branch nome-da-branch

3. Mudar para outra branch:
   git checkout nome-da-branch

4. Criar e mudar para uma nova branch ao mesmo tempo:
   git checkout -b nome-da-branch

5. Renomear uma branch:
   git branch -m nome-antigo nome-novo

6. Excluir uma branch local:
   git branch -d nome-da-branch
   > Use -D em vez de -d para forçar a exclusão.

7. Excluir uma branch remota:
   git push origin --delete nome-da-branch

8. Listar todas as branches, incluindo as remotas:
   git branch -a

9. Mesclar uma branch com a branch atual:
   git merge nome-da-branch

10. Resolver conflitos de merge:
    > Se houver conflitos, edite os arquivos manualmente e depois:
    git add .
    git commit -m "Resolvendo conflitos"

11. Atualizar a branch local com as alterações da remota:
    git pull origin nome-da-branch --rebase
"""
