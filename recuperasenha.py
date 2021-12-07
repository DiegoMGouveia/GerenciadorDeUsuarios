import smtplib
from random import randint
from email.mime.text import MIMEText
from bancodedados import *


class RecuperarSenha:
    def __init__(self):
        self.login = input('Digite seu Usuario: ')
        self.email = input('Digite seu email: ')
        self.codigo = str(randint(10000, 99999))
        self.mensagem = MIMEText(f'O codigo de recuperação da senha: {self.codigo}')

    def enviaremail(self):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("DIGITE_O_SEU_EMAIL_AQUI", "DIGITE_SUA_SENHA_AQUI")
        server.sendmail(
            "DIGITE_O_SEU_EMAIL_AQUI",  # email usado para enviar
            self.email,  # email que recebera o email
            self.mensagem.as_string())  # corpo ca mensagem
        server.quit()


def verificarec(conexao):
    dados = RecuperarSenha()
    c = conexao.cursor()
    c.execute(consql)
    resultado = c.fetchall()
    allok = False
    for i, l, s, n, e, p in resultado:
        if dados.login == l and e == dados.email:
            novasenha = Usuario()
            novasenha.logando_usuario(id=i, login=l, senha=s, nome=n, email=e, poder=p)
            dados.enviaremail()
            print('\n' * 150)
            print('''Verifique o codigo enviado para seu e-mail e digite-o aqui.
            Caso não encontre o e-mail, certifique-se que não se encontra na pasta spam ou lixo eletronico. ''')
            confirma = input('Digite o codigo enviado em seu e-mail aqui: ')
            if confirma == dados.codigo:
                _ = True
                while _:
                    novasenha.senha = input('Digite sua nova senha')
                    if checapwd(novasenha.senha):
                        salvar_usuario(vcon, novasenha, '2')
                        allok = True
                        break
            else:
                print('Código incorreto ou expirado, tente novamente.')

    if not allok:
        print('Este usuario não pertence a este e-mail ou esta incorreto. Tente novamente.')
        return allok



