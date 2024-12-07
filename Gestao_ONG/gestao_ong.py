import sqlite3
from datetime import datetime

# Conexão com o banco de dados
conn = sqlite3.connect('gestao_ong.db')
cursor = conn.cursor()

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS voluntarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL,
    disponibilidade TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    valor REAL NOT NULL,
    doador TEXT NOT NULL,
    finalidade TEXT NOT NULL
);
''')

conn.commit()

# Função para cadastrar um voluntário
def cadastrar_voluntario(nome, contato, disponibilidade):
    cursor.execute('''
    INSERT INTO voluntarios (nome, contato, disponibilidade)
    VALUES (?, ?, ?)
    ''', (nome, contato, disponibilidade))
    conn.commit()
    print(f"Voluntário '{nome}' cadastrado com sucesso!")

# Função para cadastrar uma doação
def cadastrar_doacao(data, valor, doador, finalidade):
    cursor.execute('''
    INSERT INTO doacoes (data, valor, doador, finalidade)
    VALUES (?, ?, ? ,?)
    ''', (data, valor, doador, finalidade))
    conn.commit()
    print(f"Doação de {valor} por '{doador}' cadastrada com sucesso!")

# Função para consultar voluntários
def consultar_voluntarios():
    cursor.execute('SELECT * FROM voluntarios')
    voluntarios = cursor.fetchall()
    for voluntario in voluntarios:
        print(voluntario)

# Função para consultar doações
def consultar_doacoes():
    cursor.execute('SELECT * FROM doacoes')
    doacoes = cursor.fetchall()
    for doacao in doacoes:
        print(doacao)

# Função para gerar relatório de doações
def gerar_relatorio():
    cursor.execute('SELECT SUM(valor) FROM doacoes')
    total = cursor.fetchone()[0]
    total = total if total else 0
    print(f"Total arrecadado: R$ {total:.2f}")
    cursor.execute('SELECT * FROM doacoes')
    doacoes = cursor.fetchall()
    for doacao in doacoes:
        print(doacao)

# Exemplo de uso
if __name__ == "__main__":
    # Cadastro de exemplos
    cadastrar_voluntario("João Silva", "joao@gmail.com", "Segunda a Sexta")
    cadastrar_doacao(datetime.now().strftime('%Y-%m-%d'), 100.0, "Maria Oliveira", "Compra de alimentos")
    
    # Consultas
    print("\n--- Voluntários ---")
    consultar_voluntarios()
    
    print("\n--- Doações ---")
    consultar_doacoes()
    
    # Relatório
    print("\n--- Relatório ---")
    gerar_relatorio()

# Fechar a conexão
conn.close()