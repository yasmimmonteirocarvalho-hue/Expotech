import mysql.connector
from mysql.connector import Error
from datetime import datetime


# ==========================
# CONEXÃO
# ==========================

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiago",
        database="escola_medio"
    )

    cursor = conexao.cursor()

    print("Conectado ao banco de dados!")

except Error as erro:
    print(f"Erro ao conectar ao MySQL: {erro}")
    exit()


# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ==========================
# TURMAS
# ==========================

def cadastrar_turma():
    nome = input("Nome da turma: ")
    serie = input("Série: ")
    turno = input("Turno: ")

    sql = """
    INSERT INTO turma (nome_turma, serie, turno)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, serie, turno))
    conexao.commit()

    print("Turma cadastrada com sucesso!")


def listar_turmas():
    cursor.execute("SELECT * FROM turma")

    resultados = cursor.fetchall()

    print("\n===== TURMAS =====")

    if not resultados:
        print("Nenhuma turma cadastrada.")
        return

    for turma in resultados:
        print(f"""
ID: {turma[0]}
Nome: {turma[1]}
Série: {turma[2]}
Turno: {turma[3]}
""")


def editar_turma():
    listar_turmas()

    id_turma = int(input("ID da turma: "))

    nome = input("Novo nome: ")
    serie = input("Nova série: ")
    turno = input("Novo turno: ")

    sql = """
    UPDATE turma
    SET nome_turma=%s,
        serie=%s,
        turno=%s
    WHERE id_turma=%s
    """

    cursor.execute(sql, (nome, serie, turno, id_turma))
    conexao.commit()

    print("Turma atualizada!")


def apagar_turma():
    listar_turmas()

    id_turma = int(input("ID da turma para apagar: "))

    cursor.execute(
        "DELETE FROM turma WHERE id_turma=%s",
        (id_turma,)
    )

    conexao.commit()

    print("Turma apagada!")


# ==========================
# ALUNOS
# ==========================

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    ra = input("RA: ")

    while True:
        nascimento = input("Nascimento (AAAA-MM-DD): ")

        if validar_data(nascimento):
            break

        print("Data inválida!")

    email = input("Email: ")

    listar_turmas()
    id_turma = int(input("ID da turma: "))

    sql = """
    INSERT INTO aluno
    (
        nome_al,
        RA_al,
        nascimento_al,
        email_al,
        id_turma
    )
    VALUES (%s,%s,%s,%s,%s)
    """

    valores = (
        nome,
        ra,
        nascimento,
        email,
        id_turma
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Aluno cadastrado!")


def listar_alunos():
    sql = """
    SELECT
        aluno.id_al,
        aluno.nome_al,
        aluno.RA_al,
        aluno.nascimento_al,
        aluno.email_al,
        turma.nome_turma
    FROM aluno
    JOIN turma
    ON aluno.id_turma = turma.id_turma
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n===== ALUNOS =====")

    if not resultados:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in resultados:
        print(f"""
ID: {aluno[0]}
Nome: {aluno[1]}
RA: {aluno[2]}
Nascimento: {aluno[3]}
Email: {aluno[4]}
Turma: {aluno[5]}
""")


def editar_aluno():
    listar_alunos()

    id_aluno = int(input("ID do aluno: "))

    nome = input("Novo nome: ")
    ra = input("Novo RA: ")

    while True:
        nascimento = input("Nascimento (AAAA-MM-DD): ")

        if validar_data(nascimento):
            break

        print("Data inválida!")

    email = input("Novo email: ")

    listar_turmas()

    id_turma = int(input("Novo ID da turma: "))

    sql = """
    UPDATE aluno
    SET
        nome_al=%s,
        RA_al=%s,
        nascimento_al=%s,
        email_al=%s,
        id_turma=%s
    WHERE id_al=%s
    """

    valores = (
        nome,
        ra,
        nascimento,
        email,
        id_turma,
        id_aluno
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Aluno atualizado!")


def apagar_aluno():
    listar_alunos()

    id_aluno = int(input("ID do aluno para apagar: "))

    cursor.execute(
        "DELETE FROM aluno WHERE id_al=%s",
        (id_aluno,)
    )

    conexao.commit()

    print("Aluno apagado!")


# ==========================
# MATÉRIAS
# ==========================

def cadastrar_materia():
    nome = input("Nome da matéria: ")

    listar_turmas()

    id_turma = int(input("ID da turma: "))

    sql = """
    INSERT INTO materia
    (
        nome_materia,
        id_turma
    )
    VALUES (%s,%s)
    """

    cursor.execute(sql, (nome, id_turma))
    conexao.commit()

    print("Matéria cadastrada!")


def listar_materias():
    sql = """
    SELECT
        materia.id_materia,
        materia.nome_materia,
        turma.nome_turma
    FROM materia
    JOIN turma
    ON materia.id_turma = turma.id_turma
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n===== MATÉRIAS =====")

    if not resultados:
        print("Nenhuma matéria cadastrada.")
        return

    for materia in resultados:
        print(f"""
ID: {materia[0]}
Matéria: {materia[1]}
Turma: {materia[2]}
""")


def editar_materia():
    listar_materias()

    id_materia = int(input("ID da matéria: "))

    nome = input("Novo nome da matéria: ")

    listar_turmas()

    id_turma = int(input("Novo ID da turma: "))

    sql = """
    UPDATE materia
    SET
        nome_materia=%s,
        id_turma=%s
    WHERE id_materia=%s
    """

    cursor.execute(
        sql,
        (nome, id_turma, id_materia)
    )

    conexao.commit()

    print("Matéria atualizada!")


def apagar_materia():
    listar_materias()

    id_materia = int(
        input("ID da matéria para apagar: ")
    )

    cursor.execute(
        "DELETE FROM materia WHERE id_materia=%s",
        (id_materia,)
    )

    conexao.commit()

    print("Matéria apagada!")


# ==========================
# MENU
# ==========================

while True:

    print("""
==================================
      SISTEMA ESCOLA MÉDIO
==================================

1  - Cadastrar turma
2  - Listar turmas
3  - Editar turma
4  - Apagar turma

5  - Cadastrar aluno
6  - Listar alunos
7  - Editar aluno
8  - Apagar aluno

9  - Cadastrar matéria
10 - Listar matérias
11 - Editar matéria
12 - Apagar matéria

0  - Sair
""")

    opcao = input("Escolha uma opção: ")

    try:

        if opcao == "1":
            cadastrar_turma()

        elif opcao == "2":
            listar_turmas()

        elif opcao == "3":
            editar_turma()

        elif opcao == "4":
            apagar_turma()

        elif opcao == "5":
            cadastrar_aluno()

        elif opcao == "6":
            listar_alunos()

        elif opcao == "7":
            editar_aluno()

        elif opcao == "8":
            apagar_aluno()

        elif opcao == "9":
            cadastrar_materia()

        elif opcao == "10":
            listar_materias()

        elif opcao == "11":
            editar_materia()

        elif opcao == "12":
            apagar_materia()

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")

    except Error as erro:
        print(f"Erro no banco de dados: {erro}")

    except ValueError:
        print("Digite um valor numérico válido!")

# ==========================
# FECHAMENTO
# ==========================

cursor.close()
conexao.close()
print("Conexão encerrada.")