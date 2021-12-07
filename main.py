from menus import *
from cadastusuario import *
from loginx import *
from meuusuario import *
from buscarusuario import *
from editarusuario import *
from recuperasenha import *



msg_opcaoerrada = 'Opção inválida! Tente uma das [opções] do menu!'
_ = True
while _:  # Inicio do programa
    escolha = MenuInicial()  # Menu Inicial
    if int(escolha) == 1:
        usuario_logado = login_user()  # Login retorna o usuario
        print(f'Olá {usuario_logado.nusuario}, seja bem-vindo!')
        while _:
            print('\n'*150)
            botao_menu = menu_1(usuario_logado.nomeclass)
            if usuario_logado.nomeclass == 'Administrador':  # Menu Administrador
                print('\n'*150)
                if not botao_menu in '123':
                    print('\n'*150)
                    print(msg_opcaoerrada)
                    continue
                if botao_menu == '1':  # opção atualizar meus dados
                    usuario_logado = atualizardados(usuario_logado)
                    if not usuario_logado:
                        continue
                elif botao_menu == '2':  # opção usuario
                    while _:
                        print('\n'*150)
                        botao_busca_usuario = menudeusuarios(usuario_logado)
                        if not botao_busca_usuario:
                            break
                        elif botao_busca_usuario == '1':  # opção buscar usuario
                            usuario_selecionado = buscar_usuario(vcon, consql, usuario_logado)
                            if not usuario_selecionado:
                                continue
                            while _:
                                botao_editar = input('Deseja modificar este usuário? [s/n] ')
                                if not botao_editar in 'SsNn':
                                    print('Digite S ou N.')
                                    continue
                                elif botao_editar in 'Ss':
                                    usuario_selecionado = editar(usuario_logado, usuario_selecionado)
                                    break
                                elif botao_editar in 'Nn':
                                    break

                        elif botao_busca_usuario == '2':
                            break
                elif botao_menu == '3':
                    print('\n' * 150)
                    break
            elif usuario_logado.nomeclass == 'Usuario':  # menu usuario
                conti = True
                if botao_menu not in '12':
                    print(msg_opcaoerrada)
                elif botao_menu == '1':
                    usuario_logado = atualizardados(usuario_logado)
                elif botao_menu == '2':
                    print('\n' * 150)
                    break
                continue


    elif int(escolha) == 2:
        cadastro()

    elif int(escolha) == 3:
        while _:
            verificarec(vcon)
            break



    else:
        print('\n'*150)
        print('Escolha uma opção do menu!')
        continue




