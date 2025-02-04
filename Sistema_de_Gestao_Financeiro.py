"""
* Sistema de Gestão de Finanças Pessoais  
-> Desenvolva um sistema para gerenciar finanças pessoais utilizando Programação Orientada a Objetos (POO).  

* O que vamos utilizar?  
- Métodos de Strings: Para formatar saídas, como relatórios financeiros e exibição de transações.  
- Listas: Para armazenar múltiplas transações e contas.  
- Dicionários Aninhados: Para organizar transações por categoria ou por titular.  
- Funções: Métodos para registrar transações, calcular saldo e gerar relatórios.  
- Classes e Instâncias: Para modelar contas e transações.  
- Encapsulamento (getters e setters): Para proteger atributos sensíveis, como saldo.  
- Herança: Para criar diferentes tipos de conta (Conta Corrente e Conta Poupança).  
- Polimorfismo: Para sobrescrever métodos, como cálculo de saldo com taxas diferentes para cada tipo de conta.  

* Especificações do Programa:  
1. Criar a classe `Conta` com os atributos: `titular`, `saldo` e `tipo_conta`.  
2. Criar a classe `Transacao` com os atributos: `valor`, `tipo` (depósito/saque) e `data`.  
3. Criar a classe `Financeiro` contendo os seguintes métodos:  
   - Método para adicionar transações (depósito ou saque).  
   - Método para listar todas as transações registradas.  
   - Método para calcular o saldo disponível.  
   - Método para categorizar transações (ex: alimentação, lazer, moradia).  
   - Método para gerar um relatório financeiro detalhado.  
4. Criar subclasses de `Conta` para `ContaCorrente` e `ContaPoupanca`, implementando taxas diferenciadas.  
5. Criar um arquivo principal para instanciar as classes e chamar os métodos conforme a opção escolhida pelo usuário.  
"""