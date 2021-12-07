from meuusuario import *
from bancodedados import salvar_usuario


def novopoder(usuario, usuario2):
    _ = True
    while _:
        novo_poder = input('Digite seu novo poder [Administrador] ou [Usuario] : ')
        if verificapoder(novo_poder):
            if usuario2 == 'Administrador':
                usuario.nomeclass = novo_poder
                salvar_usuario(vcon, usuario, '5')
                print('\n' * 150)
                print('poder alterado com sucesso!')
                return usuario
            else:
                print('Acesso negado!')
        continue


def deletar(conexao, usuario, usuario2):
    if usuario2.nomeclass == "Administrador":
        c=conexao.cursor()
        c.execute(f'DELETE FROM usuariosdb WHERE ID = "{usuario.id}"')
        conexao.commit()
        print('\n' * 150)
        print('Usuário deletado com sucesso!')
    else:
        print('Acesso negado!')


def editar(usuario, usuario2):
    if usuario.nomeclass == 'Administrador':
        usuario_modificado = usuario2
        _ = True
        while _:
            botao_editar_admin = input('''
            | [1] Editar Usuario |
            | [2] Editar Senha   |
            | [3] Editar Nome    |
            | [4] Editar e-mail  |
            | [5] Editar poder   |
            | [6] Deletar usuario|
            | [7] Voltar         |
             --------------------
            Escolha uma [opção] do menu: ''')
            if botao_editar_admin not in '123456':
                print('Opção inválida! Tente novamente.')
                continue
            elif botao_editar_admin == '1':
                usuario_modificado = novousuario(usuario_modificado)
                return usuario_modificado
            elif botao_editar_admin == '2':
                usuario_modificado = forcenovasenha(usuario_modificado, usuario)
                return usuario_modificado
            elif botao_editar_admin == '3':
                usuario_modificado = novonome(usuario_modificado)
                return usuario_modificado
            elif botao_editar_admin == '4':
                usuario_modificado = novoemail(usuario_modificado)
                return usuario_modificado
            elif botao_editar_admin == '5':
                usuario_modificado = novopoder(usuario_modificado, usuario.nomeclass)
                return usuario_modificado
            elif botao_editar_admin == '6':
                deletar(vcon, usuario_modificado, usuario)
                break
            elif botao_editar_admin == '7':
                return usuario_modificado
    else:
        print('Acesso negado!')

