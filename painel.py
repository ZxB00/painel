def clear():
    from os import system, name
    system('cls' if name == 'nt' else 'clear')

def logo():
    clear();print('Github: \033[1;31mhttps://github.com/ZxB00');print("""\033[1;32m         _____     
        |__  /_  __
          / /\ \/ /
         / /_ >  < 
        /____/_/\_\ """)

def linha():
    print('\033[1;36m=' * 35)

def volta():
    from os import execl, executable, argv
    execl(executable, executable, *argv)

def continuar():
    input('pressione ENTER para voltar');volta()

def cpf():
    import requests
    clear()
    cpf = input('Digite o CPF (*somente números*)>>')
    recv = requests.get('http://api-onlyfalopas.herokuapp.com/cpf/?cpf={}'.format(cpf)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    #valor 'pessoa' pega valor recv['pessoa']['valor']
    print('CPF:', recv['id'],'\nNome:', recv['pessoa']['nome'], '\nNome da Mãe:', recv['nomeMae'],'\nData de Nascimento:', recv['dataNascimento'] '\nSexo:', recv['sexo'], '\nCidade:', recv['pessoa']['nomeMunicipio'], '\nBairro', recv['pessoa']['descricaoComplemento'], '\nRua:', recv['pessoa']['nomeLogradouro'], '\nCep:', recv['pessoa']['numeroCep'])
    linha();continuar()

def ip():
    import requests
    clear()
    ip = input('\033[1;93m Digite o IP (exemplo = 192.168.0.1):')
    recv = requests.get('http://ip-api.com/json/{}'.format(ip)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('IP:', recv['query'], '\nPAÍS:', recv['country'], '\nCIDADE:', recv['city'], '\nSigla Região:', recv['region'],'\nESTADO:', recv['regionName'], '\nProvedor:', recv['isp'], '\nORGANIZAÇÂO:', recv['org'])
    linha();continuar()
   
def cep():
    import requests
    clear()
    cep = input('\033[1;93m Digite o CEP (*Obs apenas números):')
    recv = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('Cep:', recv['cep'], '\nlogradouro:', recv['logradouro'], '\nComplemento:', recv['complemento'], '\nBairro:', recv['bairro'], '\ncidade:', recv['localidade'], '\nIbge:', recv['ibge'], '\nEstado:', recv['uf'], '\nDDD:', recv['ddd'])
    linha();continuar()
  
def cnpj():
    import requests
    clear()
    cnpj = input('Digite o CNPJ(*Obs apenas números):')
    recv = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('\nCNPJ:', recv['cnpj'], '\nnome:', recv['nome'], '\nUF:', recv['uf'], '\ntelefone:', recv['telefone'], '\nemail:', recv['email'], '\nsituacao:', recv['situacao'], '\nbairro:', recv['bairro'], '\nlogradouro:', recv['logradouro'], '\nN°:', recv['numero'], '\ncep:', recv['cep'], '\nmunicipio:', recv['municipio'], '\nporte:', recv['porte'], '\ndata de abertura:', recv['abertura'],)
    linha();continuar()

logo()
print('''\033[1;37m\n
[1] - Consulta CPF
[2] - Consulta IP
[3] - Consulta CEP
[4] - Consulta CNPJ
[0] - Para Sair do Painel''');print('')
consulta = int(input('\033[1;93mDigite uma das opções >>'))

if consulta == 1:
    cpf()
elif consulta == 2:
    ip()
elif consulta == 3:
    cep()
elif consulta == 4:
    cnpj()
elif consulta == 0:
    exit()
