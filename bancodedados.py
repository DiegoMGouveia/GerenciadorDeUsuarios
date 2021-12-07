import sqlite3
from sqlite3 import Error
from usuarios import *

criar_tabela = False


def ConexaoBanco():
    caminho = "/media/diego/EA00FB8D00FB5F4F1/python3 projetos/programa/basededadosdb.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()  # variavel de conexão com o banco de dados

# variavel para criar a tabela do banco de dados
tabclient = '''CREATE TABLE usuariosdb(
                    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    LOGIN VARCHAR,
                    SENHA VARCHAR,
                    NUSUARIO VARCHAR,
                    EMAIL VARCHAR,
                    NOMECLASS VARCHAR
                );'''

# variavel para consulta no banco de dados para efetuar o login
consql = 'SELECT * FROM usuariosdb'


# função para criar a tabela
def CriarTabela(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela de usuários criada!')
    except Error as ex:
        print(ex)


# função para inserir dados de novos usuarios
def insert(conexao,args):
    usersql = f"""INSERT INTO usuariosdb
                     (LOGIN,SENHA,NUSUARIO,EMAIL,NOMECLASS)
              VALUES('{args.login}', '{args.senha}', '{args.nusuario}', '{args.email}', '{args.nomeclass}'
                    )"""
    try:
        c = conexao.cursor()
        c.execute(usersql)
        conexao.commit()
        print('Usuário cadastrado com sucesso!')
    except Error as ex:
        print(ex)


# função para consultar se o login e senha estão corretos, se estiver retornará o usuario.
def login_consulta(conexao, sql, entrada):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    login_ok = False  # se essa variavel estiver falsa, retornará um erro de senha
    for i, l, s, n, e, p in resultado:
        if l == entrada.login and s == entrada.senha:
            login_ok = True
            usuario_login = Usuario()
            usuario_login.logando_usuario(id=i, login=l, senha=s, nome=n, email=e, poder=p)
            return usuario_login
    if not login_ok:
        print('Senha não confere.')


def salvar_usuario(conexao, usuario, opcao):
    if opcao == '1':
        atualizar = 'LOGIN'
        op_atualizar = usuario.login
    elif opcao == '2':
        atualizar = 'SENHA'
        op_atualizar = usuario.senha
    elif opcao == '3':
        atualizar = 'NUSUARIO'
        op_atualizar = usuario.nusuario
    elif opcao == '4':
        atualizar = 'EMAIL'
        op_atualizar = usuario.email
    elif opcao == '5':
        atualizar = 'NOMECLASS'
        op_atualizar = usuario.nomeclass

    c = conexao.cursor()
    updatesql = f'UPDATE usuariosdb SET "{atualizar}" = "{op_atualizar}" WHERE ID = "{usuario.id}"'
    c.execute(updatesql)
    conexao.commit()



# Se esta variavel for verdadeira, tentará criar um banco de dados sempre que iniciar (linha 5)
if criar_tabela:
    CriarTabela(vcon, tabclient)

# vcon.close()