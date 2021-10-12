import sqlite3
from sqlite3 import Error

# Conexão com o banco


def conexaobanco():
    con = None
    try:
        con = sqlite3.connect('empresa.db')
    except Error as ex:
        print(ex)
    return con


vcon = conexaobanco()

# manipulando registros


def dml(conexao, query):
    try:
        c = conexao.cursor()
        c.execute(query)
        conexao.commit()
    except Error as ex:
        print(ex)

# buscando registros


def busca(conexao, query):
    c = conexao.cursor()
    c.execute(query)
    resultado = c.fetchall()
    return resultado


# Querys do banco

vbusca = """
        SELECT nome, cpf, endereco, telefone  FROM clientes 
"""

vdelete = """
        DELETE * FROM clientes
        WHERE {} = {};
""".format('id', '20')
