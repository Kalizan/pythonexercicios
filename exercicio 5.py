def valida_int (pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criando com sucesso!\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except  FileNotFoundError:
        return  False
    else:
        return True

def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


def cadastrarjogo(nomeArquivo, nomejogo,nomevideogame):
    try:
        a= open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo,nomevideogame))
    finally:
        a.close()

#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - cadastrar novo item')
    print('2 - listar cadastro')
    print('3 - sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionado...\n')
        nomejogo = input('Nome do jogo: ')
        nomevideogame = input('Nome do videogame: ')
        cadastrarjogo(arquivo, nomejogo, nomevideogame)

    elif op == 2:
        print('Opção de listar selecionada...\n')
        listararquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break


