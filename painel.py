import requests
import os
from sys import argv, executable 

def clear():
    os.system('cls | clear')

def logo():
    clear();print("""\033[1;32m         _____     
        |__  /_  __
          / /\ \/ /
         / /_ >  < 
        /____/_/\_\ """)

def linha():
    print('\033[1;36m=' * 35)

def volta():
    os.execl(executable, executable, *argv)

def continuar():
    input('pressione ENTER para voltar');volta()

def ip():
    clear()
    ip = str(input('\033[1;93m Digite o IP (exemplo = 192.168.0.1):')).strip().upper()
    recv = requests.get('http://ip-api.com/json/{}'.format(ip)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('IP:', recv['query']);print('PAÍS:', recv['country']);print('CIDADE:', recv['city']);print('Sigla Região:', recv['region']);print('ESTADO:', recv['regionName']);print('Provedor:', recv['isp']);print('ORGANIZAÇÂO:', recv['org'])
    linha();continuar()
   
def cep():
    clear()
    cep = str(input('\033[1;93m Digite o CEP (*Obs apenas números):'))
    recv = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('cep:', recv['cep']);print('logradouro:', recv['logradouro']);print('complemento:', recv['complemento']);print('bairro:', recv['bairro']);print('cidade:', recv['localidade']);print('ibge:', recv['ibge']);print('Estado:', recv['uf']);print('ddd:', recv['ddd'])
    linha();continuar()
  
def cnpj():
    clear()
    cnpj = input('Digite o CNPJ(*Obs apenas números):')
    recv = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('CNPJ:', recv['cnpj']);print('nome:', recv['nome']);print('UF:', recv['uf']);print('telefone:', recv['telefone']);print('email:', recv['email']);print('situacao:', recv['situacao']);print('bairro:', recv['bairro']);print('logradouro:', recv['logradouro']);print('N°:', recv['numero']);print('cep:', recv['cep']);print('municipio:', recv['municipio']);print('porte:', recv['porte']);print('data de abertura:', recv['abertura']);print('Data Roubo/Furto:', recv['dataAtualizacaoRouboFurto'])
    linha();continuar()

def placa():
    clear()
    placa = input('Digite a placa do veículo:')
    recv = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa), verify=False).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('Ano:', recv['ano']);print('Ano Modelo:', recv['anoModelo']);print('Modelo:', recv['modelo']);print('Cor:', recv['cor']);print('Marca:', recv['marca']);print('Chassi:', recv['chassi']);print('Municipio', recv['municipio']);print('COD Retorno:', recv['codigoRetorno']);print('COD Situação:', recv['codigoSituacao']);print('Data:', recv['data'])
    linha();continuar()

def covid():
    clear()
    covid = input('Digite a sigla do estado(exemplo SP, GO, RJ:')
    recv = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{}'.format(covid)).json()
    clear();linha();print('\033[1;92m#RESULTADO#')
    print('UF:', recv['uf']);print('Estado:', recv['state']);print('Casos:', recv['cases']);print('Mortes:', recv['deaths']);print('Suspeitos:', recv['suspects']);print('Recusados:', recv['refuses']);print('Data:', recv['datetime'])
    linha();continuar()

logo()
print('''\033[1;37m\n
[1] - Consulta IP
[2] - Consulta CEP
[3] - Consulta CNPJ
[4] - Consulta Placa
[5] - Consulta Covid
[0] - Para Sair do Painel''');print('')
consulta = int(input('\033[1;93mDigite uma das opções >>'))

#=============Codiçoes==================#

if consulta == 1:
    ip()
elif consulta == 2:
    cep()
elif consulta == 3:
    cnpj()
elif consulta == 4:
    placa()
elif consulta == 5:
    covid()
elif consulta == 0:
    exit()
