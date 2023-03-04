from lib.interface import cabeçalho
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt = leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = gravação de arquivo texto (+ é o que cria o arquivo)
        a.close()
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome , 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())