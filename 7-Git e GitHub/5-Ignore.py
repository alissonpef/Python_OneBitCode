"""
*Usando .gitignore no Git*

1. Criar um arquivo .gitignore na raiz do projeto:
   touch .gitignore

2. Adicionar arquivos ou pastas para serem ignorados:
   Exemplo de conteúdo do .gitignore:

   # Ignorar arquivos temporários do sistema
   *.log
   *.tmp

   # Ignorar arquivos do editor de código
   .vscode/
   .idea/

   # Ignorar dependências comuns
   node_modules/
   vendor/

   # Ignorar arquivos de build
   dist/
   build/

3. Aplicar as configurações do .gitignore:
   git rm -r --cached .
   git add .
   git commit -m "Atualizando .gitignore"

   > O comando 'git rm -r --cached .' remove arquivos ignorados do staging sem deletá-los do projeto.

4. Gerar um .gitignore padrão automaticamente:
   > Para projetos específicos, use:
   curl -L -o .gitignore https://www.toptal.com/developers/gitignore/api/python,java,node
"""
