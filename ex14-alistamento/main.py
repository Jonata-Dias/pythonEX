# Faça um progrma que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar.
# -Se é a hora de se alistar.
# -Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou
# que passou do prazo.
from datetime import date

def get_int():
    valid = False
    while True:
        n = 0
        try:
            while not valid:
                n = int(input('Digite o ano em que nasceu: ').strip().replace(' ', ''))
                valid = len(str(n)) != 4 or n >= 1920 and n <= date.today().year
                if not valid:
                    raise TypeError              
        except ValueError:
            print('Digite o ano que você nasceu com quatro números!')
        except TypeError:
            print(f'O ano de {n} não é uma data válida')
        else:
            return n


def get_nome():
    while True:
        try:
            nome = str(input('Digite seu nome: ')).strip().capitalize().replace(' ', '')
            if nome == '' or not nome.isalpha():
                raise ValueError
        except ValueError:
            print('Digite apenas seu nome sem números ou caracteres especiais.')
        else:
            return nome    


while True:
    nome = get_nome()
    while True:
        sexo = str(input('Digite seu sexo [ M/F ]: ')).upper().strip()[0]
        if sexo not in 'MF':
            print('Digite a penas M para sexo masculino e F para feminino.')
        else:
            break
    if sexo == 'F':
        print(f'olá {nome} voce não é obriga a se alistar.')
    else:
        print(f'olá {nome} você é obrgado a se alistar.')
        nasc = get_int() 
        ano_atual = date.today().year 
        idade = ano_atual - nasc   
        if idade < 18:
            saldo = 18 - idade    
            print(f'Com sua idade de {idade} anos você precisa se alistar daqui {saldo} anos. No ano de {ano_atual + saldo}.')
        elif idade == 18:
            print('Este é seu ano de alistamento procure o quartel mais proximo.')
        else:
            saldo = idade - 18
            print(f'Com sua idade de {idade} anos você deveria ter se alistado a {saldo} anos. No ano de {ano_atual - saldo}.')
    while True:
        continuar = str(input('Deseja verificar outro nome? [ S/N ]')).strip().upper()[0] 
        if continuar not in 'SN':
            print('Digite apenas S para continuar e N para parar o programa.') 
        else:
            break      
    if continuar == 'N':
        break    
print('FIM DO PROGRAMA!')    
