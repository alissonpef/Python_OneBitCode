"""
pg_dump -U _nome_usuario -F c -b -v -f "/caminho/do/arquivo.backup" nome_do_banco
pg_restore -U nome_usuario -d nome_banco --create -v ~/caminho/do/arquivo.backup

# Faz um backup completo do banco "exercise2_sql"
pg_dump -U postgres -F c -b -v -f "C:\Users\Alisson Pereira\Documents\backup\exercise2_sql.backup" exercise2_sql

# Restaura o backup do banco "exercise2_sql"
pg_restore -U nome_usuario -d nome_banco --create -v ~/caminho/do/arquivo.backup
pg_restore -U postgres -d exercise2_sql --create -v "C:\Users\Alisson Pereira\Documents\backup\exercise2_sql.backup"]

# Restaura o backup dentro de um banco já existente (exercicio2_sql), Não recria o banco, apenas restaura os dados 
e estrutura dentro dele
pg_restore -d exercise2_sql -v "C:\Users\Alisson Pereira\Documents\backup\exercicio2_sql.backup"

# Faz um backup apenas da tabela "filmes"
pg_dump -v -F c -f "C:\Users\Alisson Pereira\Documents\backup\tabela_filmes.backup" -t filmes exercise2_sql

# Restaura apenas os dados da tabela "filmes", sem recriar a estrutura
pg_restore -t filmes --data-only "C:\Users\Alisson Pereira\Documents\backup\tabela_filmes.backup"
"""