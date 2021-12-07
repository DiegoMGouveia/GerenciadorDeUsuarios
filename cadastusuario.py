from usuarios import Usuario
from verificacao import *
from bancodedados import *


def cadastro():
    usu = Usuario()
    usu.cadastrar()
    insert(vcon, usu)







