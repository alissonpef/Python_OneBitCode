# Protetor de PDF

Aplicação web em Flask para adicionar um CPF personalizado em um arquivo PDF enviado pelo usuário, com a possibilidade de escolher posição e cor.

## Como executar

### Passo 1: Clonar o repositório

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/alissonpef/Python_OneBitCode/8-Docker/Projeto.git
```
cd 8-Docker/Projeto/
```

### Passo 2: Criar e ativar o ambiente virtual

```bash
python -m venv env
source env/Scripts/activate  # Para Windows, use 'env\Scripts\activate'
```

Se houver erro ao ativar, execute:

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

### Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Rodar a aplicação

```bash
python app.py
```

Acesse a aplicação em: `http://127.0.0.1:5000/`

## Estrutura do projeto

```
8-Docker/
  Projeto/
    ├── app.py              # Código principal da aplicação
    ├── pdf_modifier.py     # Função para modificar PDFs
    ├── requirements.txt    # Dependências do projeto
    ├── static/
    │   └── styles.css      # Arquivo de estilos
    ├── templates/
    │   └── index.html      # Template HTML
    └── uploads/            # Pasta onde os PDFs modificados são armazenados
```

## Dependências

- Flask
- Flask-WTF
- WTForms
- PyPDF2
- ReportLab

