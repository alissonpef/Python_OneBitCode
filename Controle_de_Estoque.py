"""
Projeto: Sistema de Gerenciamento de Estoque

Descricao:
    Desenvolva um sistema para gerenciar o estoque de uma loja, permitindo o cadastro de produtos,
    atualizacao de quantidades, remocao de itens e geracao de relatorios. O sistema tambem deve armazenar
    os dados em arquivos CSV ou TXT para persistencia.

O que vamos utilizar?
    - Metodos de Strings: Para formatar saidas, como descricoes de produtos e relatorios.
    - Listas: Para armazenar colecoes de produtos.
    - Dicionarios Aninhados: Para organizar informacoes dos produtos, como nome, preco e quantidade.
    - Funcoes: Para operacoes como cadastrar, editar e excluir produtos.
    - Classes e Instancias: Para modelar os produtos e o estoque.
    - Encapsulamento (getters e setters): Para proteger e manipular atributos.
    - Heranca: Para diferenciar produtos comuns e produtos pereciveis.
    - Polimorfismo: Para personalizar metodos de exibicao e atualizacao de produtos.
    - Manipulacao de Arquivos (TXT ou CSV): Para salvar e recuperar dados do estoque.

Especificacoes do Programa:

1. Criar a classe `Produto` contendo:
    - Atributos: `nome`, `preco`, `quantidade`, `categoria`.
    - Metodos getters e setters para manipular os dados com seguranca.
    - Metodo para exibir informacoes formatadas.

2. Criar a classe `Estoque` contendo:
    - Uma lista de produtos armazenados como dicionarios aninhados.
    - Metodos para adicionar, editar e remover produtos.
    - Metodo para atualizar a quantidade de um produto.
    - Metodo para buscar produtos pelo nome ou categoria.
    - Metodo para listar todos os produtos disponiveis.

3. Criar a classe `ProdutoPerecivel` que herda de `Produto` e inclui:
    - Atributo extra: `validade`.
    - Metodo sobrescrito para exibir a validade do produto.

4. Criar a classe `GerenciadorDeArquivos` contendo:
    - Metodo para salvar os produtos em um arquivo CSV ou TXT.
    - Metodo para carregar os produtos a partir do arquivo.
    - Metodo para excluir produtos do arquivo.

5. Criar um arquivo principal `main.py` que:
    - Instancia as classes e permite a interacao do usuario via menu.
    - Executa operacoes como adicionar, editar e remover produtos.
    - Gera relatorios de estoque em um arquivo CSV ou TXT.
"""
