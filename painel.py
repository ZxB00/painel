import requests
import os
from sys import argv, executable 
while True:
    def logo():
        os.system('clear')
        print("""             _____     
            |__  /_  __
              / /\ \/ /
             / /_ >  < 
            /____/_/\_\ """)
    #---------------------------#
    def linha():
        print('\033[1;36m=' * 35)
    #---------------------------#
    logo()
    print("""\033[1;37m
    ==========================
    [1] - Consulta IP
    [2] - Consulta CEP
    [3] - Consulta CNPJ
    [0] - Para Sair do Painel
    ==========================
    """)

    def volta():
        os.execl(executable, executable, *argv)


    def continuar():
        input('pressione ENTER para continuar')
        volta()
    
    consulta = int(input('\033[1;93m Digite uma das opções >>'))
    
#====================Consulta de ip=================#
    def ip():
            os.system('clear')
            ip = str(input('\033[1;93m Digite o IP (exemplo = 192.168.0.1):')).strip().upper()
            recv = requests.get('http://ip-api.com/json/' + ip).json()
            os.system('clear')
            linha()
            print('\033[1;92mRESULTADO')
            print('IP:', recv['query']);print('PAÍS:', recv['country']);print('CIDADE:', recv['city']);print('Sigla Região:', recv['region']);print('ESTADO:', recv['regionName']);print('Provedor:', recv['isp']);print('ORGANIZAÇÂO:', recv['org'])
            linha()
            continuar()
            
#====================Consulta CEP====================#    
    def cep():
            os.system('clear')
            cep = str(input('\033[1;93m Digite o CEP (*Obs apenas números):'))
            recv = requests.get('https://viacep.com.br/ws/' + cep + '/json/').json()
            os.system('clear')
            linha()
            print('\033[1;92mRESULTADO')
            print('cep:', recv['cep']);print('logradouro:', recv['logradouro']);print('complemento:', recv['complemento']);print('bairro:', recv['bairro']);print('cidade:', recv['localidade']);print('ibge:', recv['ibge']);print('Estado:', recv['uf']);print('ddd:', recv['ddd'])
            linha()
            continuar()
 #===================Consulta de CNPJ====================#   
    def cnpj():
            os.system('clear')
            cnpj = input('Digite o CNPJ(*Obs apenas números):')
            recv = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj).json()
            os.system('clear')
            linha()
            print('\033[1;92mRESULTADO')
            print('CNPJ:', recv['cnpj']);print('nome:', recv['nome']);print('UF:', recv['uf']);print('telefone:', recv['telefone']);print('email:', recv['email']);print('situacao:', recv['situacao']);print('bairro:', recv['bairro']);print('logradouro:', recv['logradouro']);print('N°:', recv['numero']);print('cep:', recv['cep']);print('municipio:', recv['municipio']);print('porte:', recv['porte']);print('data de abertura:', recv['abertura'])
            linha()
            continuar()

    if consulta == 1:
        ip()
    elif consulta == 2:
        cep()
    elif consulta == 3:
        cnpj()
    elif consulta == 0:
        break
    elif consulta != 1 != 2 != 3 != 0:
        os.system('clear')
        print('\033[1;31mOpção Icorreta! Escolha novamente')
        continue