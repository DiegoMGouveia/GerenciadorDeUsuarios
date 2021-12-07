def MenuInicial():
    print('''
     ---------------------
    | [1] Login           |
    | [2] Criar conta     |
    | [3] Esqueci a senha |
     ---------------------
    ''')
    while True:
        menu_escolha = input('Digite uma [opção] do menu: ')
        if menu_escolha.isnumeric():
            if int(menu_escolha) == 1 or int(menu_escolha) == 2 or int(menu_escolha) == 3:
                return menu_escolha
            else:
                print('Digite apenas as [opções] do menu!')
        else:
            print('Digite apenas as [opções] do menu!')


# menu usuario
def menu_1(usuario):
    if usuario == 'Administrador':
        botao = input('''
 --------------
| [1] Meu Usuario |
| [2] Usuarios    |
| [3] Voltar      |
 --------------
Digite uma [opção] do menu: ''')
        return botao
    elif usuario == 'Usuario':
        botao = input('''
 -----------------
| [1] Meu Usuario |
| [2] Voltar      |
 -----------------
Digite uma [opção] do menu: ''')
        return botao


# menu admin (parei aqui)
def menudeusuarios(usuario):
    _ = True
    while _:
        botao = input('''
 --------------------
| [1] Buscar Usuario |
| [2] Voltar         |
 --------------------
Digite uma [opção] do menu: ''')
        if botao not in '12':
            print('Digite uma das [opções] do menu.')
            continue
        elif '1' == usuario.nomeclass != 'Administrador':
            print('Acesso Negado!')
            return False
        return botao





