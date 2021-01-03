print('\nMenu Inicial')
erro_login = 'Dados incompátiveis'
sep = ('-----------------------------------')
sep_2 = ('*****')
a = 1
cont = 0

print(
    f'{sep}\nDeseja INICIAR: [1]\nDeseja SAIR: [2]\n{sep}\nCreated by: Lucas Aquino\n{sep}')
menu_1 = int(input('Comando: '))

if menu_1 == 2:
    print('\nSAIU.......\n')


def iniciate(menu_1):

    if menu_1 == 1:
        print(
            f'{sep}\nDeseja FAZER LOGIN: [1]\nDeseja CADASTRO: [2]\nDeseja FECHAR: [3]\n{sep}')
        menu_2 = int(input('Comando: '))

        if menu_2 == 1:
            login(menu_2)
        if menu_2 == 2:
            cadastro(menu_2)
        if menu_2 == 3:
            print('\nENCERRADO.....\n')
            exit


def cadastro(a):
    nome = input(f'{sep}\nInforme seu nome: ')
    idade = int(input('Informa sua idade: '))
    if idade >= 18:
        cad_login = input('Crie login: ')
        cad_login2 = input('Confirmação de Login: ')
        cad_senha = input('Crie sua Senha: ')
        cad_senha2 = input('Confirme sua Senha: ')
        print(sep)
        ID = 0
        with open('Banco_Dados_Rede.txt', 'r') as ask_id:
            palavra = 'ID'
            cont = 0
            for linha in ask_id:
                linha = linha.rstrip()
                if palavra in linha:
                    cont += 1
            ID = cont

        if cad_senha2 == cad_senha:

            if len(cad_senha) >= 8:

                if cad_login == cad_login2:
                    with open('Banco_Dados_Rede.txt', 'a') as key_login:
                        login_key = []
                        login_key.append(f'\nID {ID}\n')
                        login_key.append(f'{nome},')
                        login_key.append(f'{idade}\n')
                        login_key.append(f'{cad_login},')
                        login_key.append(f'{cad_senha}\n')
                        login_key.append('f\n')
                        key_login.writelines(login_key)
                        print('\nCadastro efetuado com sucesso!\n')
                        iniciate(menu_1)

                else:
                    print(erro_login)
                    iniciate(menu_1)
            else:
                print('Senha necessita ter 8 caracteres')
                cadastro(a)

        else:
            print(erro_login)
            iniciate(menu_1)
    else:
        print('Para efetuar cadastro é necessario ser maior de 18 anos')
        iniciate(menu_1)


def login(a):
    add_1 = 0
    global login_in
    login_in = input(f'{sep}\nDigite Login: ')
    global senha
    senha = input(f'Digite a Senha: ')
    print(sep)
    leitor_key(a)


def leitor_key(a):
    with open('Banco_Dados_Rede.txt', 'r') as key_entrace:
        if True:
            key_entrace.seek(cont)
            dados = []
            for linha in key_entrace:
                linha = linha.rstrip()

                if linha[:2] == 'ID':
                    for linha in key_entrace:
                        linha = linha.rstrip()
                        for i in range(len(linha)):
                            if linha[i] == ',':
                                linha_1 = linha[:i]
                                dados.append(linha_1)
                                linha_2 = linha[i + 1:]
                                dados.append(linha_2)
                                break
                        if linha == 'f':
                            password(dados)
        if True:
            print('Login não encontrado')
            iniciate(menu_1)


def password(dados):
    login_cad = dados[2]
    senha_cad = dados[3]

    if login_in == login_cad:
        if senha == senha_cad:
            print('\nAbrindo CARD....')
            print(f'\n{sep_2} Seu Card {dados[0]} {sep_2}\n')
            iniciate(menu_1)

        else:
            print('\nSenha Incorreta\n')
            iniciate(menu_1)

    else:
        dados = []
        global cont
        cont += 1
        leitor_key(a)


iniciate(menu_1)
