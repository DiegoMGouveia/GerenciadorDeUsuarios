from usuarios import *


def buscar_usuario(conexao, sql, usuario):
    procurar = input('Digite o ID do usuario a pesquisar: ')
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    identificado = False
    for i, l, s, n, e, p in resultado:
        if str(i) == procurar and usuario.nomeclass == 'Administrador':
            usuario_escolhido = Usuario()
            usuario_escolhido.logando_usuario(id=i, login=l, senha=s, nome=n, email=e, poder=p)
            usuario_escolhido.infoadm()
            return usuario_escolhido
    if not identificado:
        print('ID não encontrado.')
        return False





