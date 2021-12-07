from bancodedados import *


def login_user():
    while True:
        entrada_usuario = UsuarioLogin()
        if not login_consulta(vcon, consql, entrada_usuario):
            continue
        else:
            entrou_usuario = login_consulta(vcon, consql, entrada_usuario)
            print('\n'*150)
            print('login efetuado com sucesso!')
            return entrou_usuario



