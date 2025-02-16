"""
* Projeto: Sistema de Gerenciamento de Conta Bancária

Descrição:
    Desenvolva um sistema para gerenciar contas bancárias, permitindo o cadastro de contas,
    operações de depósito, saque, transferência entre contas e geração de relatórios de transações.
    O sistema deve armazenar os dados em arquivos CSV ou TXT para persistência.

O que vamos utilizar?
    - Métodos de Strings: Para formatação de saídas, como relatórios de transações.
    - Listas: Para armazenar coleções de contas bancárias.
    - Dicionários Aninhados: Para organizar informações das contas, como número, saldo e titular.
    - Funções: Para operações como cadastro, edição e exclusão de contas.
    - Classes e Instâncias: Para modelar as contas bancárias e o sistema bancário.
    - Encapsulamento (getters e setters): Para proteger e manipular atributos sensíveis das contas.
    - Herança: Para diferenciar tipos de conta, como conta corrente e poupança.
    - Polimorfismo: Para personalizar métodos de exibição e operações bancárias.
    - Manipulação de Arquivos (TXT ou CSV): Para salvar e recuperar dados das contas bancárias.

Especificações do Programa:

1. Criar a classe `ContaBancaria` contendo:
    - Atributos: `numero`, `saldo`, `titular`.
    - Métodos getters e setters para manipular os dados com segurança.
    - Métodos para depósito, saque e exibição de saldo.

2. Criar a classe `SistemaBancario` contendo:
    - Uma lista de contas bancárias armazenadas como dicionários aninhados.
    - Métodos para adicionar, editar e remover contas bancárias.
    - Métodos para transferência entre contas, busca de contas pelo número ou titular.
    - Método para listar todas as contas disponíveis.

3. Criar a classe `ContaCorrente` que herda de `ContaBancaria` e inclui:
    - Atributos extras: `limite_cheque_especial`, `tarifa_mensal`.
    - Método para exibir o extrato.

4. Criar um arquivo principal `main.py` que:
    - Instancia as classes e permite a interação do usuário via menu.
    - Executa operações como abrir conta, depositar, sacar, transferir entre contas e gerar relatórios de transações em um arquivo CSV ou TXT.
"""