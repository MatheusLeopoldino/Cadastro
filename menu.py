import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = ""

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Atualizar Nome\n'                   +
          '4. Atualizar Lgin\n'               +
          '5. Atualizar CPF\n'               +
          '6. Atualizar Data de Nascimento\n'     +
          '7. Excluir\n'                          +
          '0.Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe seu nome: ')
            nome = input()
            print('Informe seu login: ')
            login = input()
            print('Informe seu senha: ')
            senha = input()
            print('Informe sua data de nascimento: ')
            dtNasc   = input()
            #Chamar o método inserir
            operacao().inserir(nome, login, senha, dtNasc)
        elif this.opcao == 2:
            operacao().consultar()
        elif this.opcao == 3:
            print("Informe o código que deseja atualizar")
            this.codigo=int(input())
            print("informe o novo nome: ")
            this.campo = input()
            operacao().atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe o novo login: ")
            this.campo = input()
            operacao().atualizar(this.codigo, 'login', this.campo)
        elif this.opcao == 5:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe o novo senha: ")
            this.campo = input()
            operacao().atualizar(this.codigo, 'senha', this.campo)
        elif this.opcao == 6:
            print("Informe o código que deseja atualizar")
            this.codigo = int(input())
            print("informe a nova data de nascimento: ")
            this.campo = input()
            operacao().atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))
        elif this.opcao == 7:
            print("Informe o código para a exclusão do dado")
            this.codigo = int(input())
            operacao().excluir(this.codigo)
        else:
            print('Opção escolhida não é válida!')