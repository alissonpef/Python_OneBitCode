"""
*Configurando SSH para o GitHub*

1. Verificar se já existe uma chave SSH configurada:
   ls -al ~/.ssh

2. Gerar uma nova chave SSH (substitua seu e-mail):
   ssh-keygen -t ed25519 -C "seu-email@example.com"

   > Pressione Enter para salvar no local padrão e defina uma senha opcional.

3. Adicionar a chave SSH ao agente SSH:
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519

4. Copiar a chave pública para adicionar ao GitHub:
   cat ~/.ssh/id_ed25519.pub

   > Copie a saída do comando acima.

5. Adicionar a chave SSH ao GitHub:
   - Acesse https://github.com/settings/keys
   - Clique em "New SSH Key"
   - Cole a chave copiada no campo "Key"
   - Salve a chave

6. Testar a conexão SSH com o GitHub:
   ssh -T git@github.com

   > Se configurado corretamente, verá a mensagem:
   > "Hi <seu-usuário>! You've successfully authenticated..."

7. Configurar o Git para usar o SSH no repositório:
   git remote set-url origin git@github.com:usuario/repositorio.git

8. Clonar repositórios usando SSH:
   git clone git@github.com:usuario/repositorio.git
"""
