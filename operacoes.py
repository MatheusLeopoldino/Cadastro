import mysql.connector
import ConexaoBD #Classe que faz a conexão com o banco de dados

db_connection = ConexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, login, senha , dataDeNascimento):
    try:
        sql = "insert into pessoa(codigo, nome, login, senha, dataDeNascimento) values('', '{}', '{}','{}', '{}')".format(nome, login, senha, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit()#Inserção de dados no BD
        print("{} Inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)

def consultar():
    try:
        sql = 'select * from pessoa'
        con.execute(sql)

        for(codigo, nome, login, senha, dataDeNascimento) in con:
            print('Código: {}, Nome: {}, Login: {}, Senha: {}, Data de Nascimento: {}'.format(codigo, nome, login, senha, dataDeNascimento))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizar(cod, campo, novoDado):
    try:
        sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(cod):
    try:
        sql = "delete from pessoa where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)