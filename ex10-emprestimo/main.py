# Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestaçao mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print('\033[32mCÁLCULO DE EMPRÉSTIMO!\033[m'.center(40))

def emprestimo(valor=.0, anos=0):
    prestacao = valor / (anos * 12)
    return round(prestacao, 2)


def isfloat(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',', '.').replace(' ', ''))
            if n <= 0:
                raise ValueError
        except(ValueError, TypeError):
             print('Por favor, digite um número real válido e positivo!')
        except KeyboardInterrupt:
            print('Por favor, digite um número real válido!')
        else:
            return n
        

def isint(msg):
    while True:
        try:
            n = int(input(msg).strip().replace(' ', ''))
            if n <= 0:
                raise ValueError
        except(ValueError, TypeError):
               print('Por favor, digite um número inteiro válido e positivo!')
        except KeyboardInterrupt:
            print('Por favor, digite um número inteiro válido!')
        else:
            return n
        

vcasa = isfloat('Digite o valor da casa R$: ')
anos = isint('Digite em quantos anos deseja pagar: ')
sal = isfloat('Digite seu salário R$:')
   
resp = emprestimo(vcasa, anos)

print(f'Para pagar uma casa de {locale.currency(vcasa, grouping=True)} em {anos} anos' 
      f'a prestação será de {locale.currency(resp, grouping=True)} com seu salário de {locale.currency(sal, grouping=True)}.')
if resp <= sal * 30 / 100:
    print('Seu empréstimo foi aporovado. PARABENS!!')
else:
    print('Seu empréstimo não foi aprovado! Que pena.')
