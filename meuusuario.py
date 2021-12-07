from bancodedados import *


def meu_usuario(usuario):
    _ = True
    while _:
        print('---------------------------------------')
        usuario.info()
        print('---------------------------------------')
        botao = input('''
| [1] Editar Usuario |
| [2] Editar Senha   |
| [3] Editar Nome    |
| [4] Editar e-mail  |
| [5] Voltar         |
 --------------------
Escolha uma [opção] do menu: ''')
        if botao not in '12345':
            print('\n' * 150)
            print('Opção inválida! Digite uma das [opções] do menu!')
            continue
        else:
            return botao


def novousuario(usuario):
    _ = True
    while _:
        novo_login = input('Digite seu novo Usuario: ')
        if not checauser(novo_login):
            print(errouser)
            continue
        elif checauser(novo_login):
            usuario.login = novo_login
            salvar_usuario(vcon, usuario, '1')
            print('\n' * 150)
            print('Usuario alterado com sucesso!')
            return usuario


def novasenha(usuario):
    _ = True
    while _:
        old_pwd = input('Digite sua senha atual: ')
        novo_pwd = input('Digite seu nova senha: ')
        if old_pwd == usuario.senha:
            if not checapwd(novo_pwd):
                continue
            elif checapwd(novo_pwd):
                usuario.senha = novo_pwd
                salvar_usuario(vcon, usuario, '2')
                print('\n' * 150)
                print('Senha alterada com sucesso!')
                return usuario
        else:
            print('Senha incorreta! Digite sua senha ATUAL para altera-la.')
            continue


def forcenovasenha(usuario):
    _ = True
    while _:
        print('\n' * 150)
        novo_pwd = input('Digite seu nova senha: ')
        if not checapwd(novo_pwd):
            continue
        elif checapwd(novo_pwd):
            usuario.senha = novo_pwd
            salvar_usuario(vcon, usuario, '2')
            print('\n' * 150)
            print('Senha alterada com sucesso!')
            return usuario


def novonome(usuario):
    _ = True
    while _:
        novo_nome = input('Digite seu novo Nome: ')
        if checanome(novo_nome):
            usuario.nusuario = novo_nome
            salvar_usuario(vcon, usuario, '3')
            print('\n' * 150)
            print('Nome alterado com sucesso!')
            return usuario
        else:
            print('\n' * 150)
            continue


def novoemail(usuario):
    _ = True
    while _:
        novo_email = input('Digite seu novo e-mail: ')
        if verificaemail(novo_email):
            usuario.email = novo_email
            salvar_usuario(vcon, usuario, '4')
            print('\n' * 150)
            print('E-mail alterado com sucesso!')
            return usuario
        continue


def atualizardados(usuario):
    _ = True
    while _:
        usuario_atualizado = usuario
        bot_menu_m_usr = meu_usuario(usuario_atualizado)
        if bot_menu_m_usr == '1':
            usuario_atualizado = novousuario(usuario_atualizado)
        elif bot_menu_m_usr == '2':
            usuario_atualizado = novasenha(usuario_atualizado)
        elif bot_menu_m_usr == '3':
            usuario_atualizado = novonome(usuario_atualizado)
        elif bot_menu_m_usr == '4':
            usuario_atualizado = novoemail(usuario_atualizado)
        elif bot_menu_m_usr == '5':
            return usuario_atualizado
