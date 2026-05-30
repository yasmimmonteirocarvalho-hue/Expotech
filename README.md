# Sistema Escolar - Python + MySQL

## Descrição

Este projeto consiste em um sistema simples de gerenciamento escolar desenvolvido em Python e integrado ao banco de dados MySQL.

O sistema permite realizar operações de cadastro, consulta, edição e exclusão de:

- Turmas
- Alunos
- Matérias

Todas as operações são realizadas através de um menu interativo no terminal.

---

## Tecnologias Utilizadas

- Python 3
- MySQL
- MySQL Connector

---

## Dependências

Instale a biblioteca necessária:

```bash
pip install mysql-connector-python
```

---

## Banco de Dados

O sistema utiliza o banco de dados:

```sql
escola_medio
```

### Tabela Turma

```sql
CREATE TABLE turma (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma VARCHAR(100) NOT NULL,
    serie VARCHAR(20) NOT NULL,
    turno VARCHAR(20) NOT NULL
);
```

### Tabela Aluno

```sql
CREATE TABLE aluno (
    id_al INT AUTO_INCREMENT PRIMARY KEY,
    nome_al VARCHAR(100) NOT NULL,
    RA_al VARCHAR(20) NOT NULL,
    nascimento_al DATE NOT NULL,
    email_al VARCHAR(100),
    id_turma INT,
    FOREIGN KEY (id_turma)
        REFERENCES turma(id_turma)
);
```

### Tabela Matéria

```sql
CREATE TABLE materia (
    id_materia INT AUTO_INCREMENT PRIMARY KEY,
    nome_materia VARCHAR(100) NOT NULL,
    id_turma INT,
    FOREIGN KEY (id_turma)
        REFERENCES turma(id_turma)
);
```

---

## Configuração da Conexão

No início do código estão definidos os dados de acesso ao banco:

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiago",
    database="escola_medio"
)
```

Caso necessário, altere:

- host
- user
- password
- database

para corresponder às configurações do seu MySQL.

---

## Funcionalidades

### Turmas

- Cadastrar turma
- Listar turmas
- Editar turma
- Apagar turma

### Alunos

- Cadastrar aluno
- Listar alunos
- Editar aluno
- Apagar aluno

### Matérias

- Cadastrar matéria
- Listar matérias
- Editar matéria
- Apagar matéria

---

## Estrutura do Projeto

```text
projeto/
│
├── escolaMcomfunc.py
└── README.md
```

---

## Como Executar

1. Inicie o MySQL.
2. Crie o banco de dados e as tabelas.
3. Instale a dependência:

```bash
pip install mysql-connector-python
```

4. Execute o programa:

```bash
python escolaMcomfunc.py
```

---

## Menu Principal

```text
========= MENU =========

1 - Cadastrar turma
2 - Listar turmas
3 - Editar turma
4 - Apagar turma

5 - Cadastrar aluno
6 - Listar alunos
7 - Editar aluno
8 - Apagar aluno

9 - Cadastrar matéria
10 - Listar matérias
11 - Editar matéria
12 - Apagar matéria

0 - Sair
```

---

## Relacionamentos

O sistema possui os seguintes relacionamentos:

- Uma turma pode possuir vários alunos.
- Uma turma pode possuir várias matérias.
- Cada aluno pertence a uma única turma.
- Cada matéria pertence a uma única turma.
