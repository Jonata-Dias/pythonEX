# Faça um programa que leia um número de 0 a 9999 e mostre
# Na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# milhar: 1

unidades = ['unidades', 'dezenas', 'centenas', 'milhar', 'dezena de milhar', 'centena de milhar']
decimal = ['', '0', '00', '000', '0000', '00000']
nstring = []
nreverse = []


def isnun():   
    while True:
        try:
            n = str(input('Digite um número: '))
            if n.strip() == '':
                raise ValueError
            newn = int(n)
        except ValueError:
            print('Por favor, digite um número inteiro válido!')
        except TypeError:
            print('O tipo da entrada deve ser um número inteiro válido!')
        except KeyboardInterrupt:
            print('O USUÁRIO NÃO DIGITOU!')
        else:
            return newn
        
n = isnun()            

for index, value in enumerate(str(n)):
    nstring.append(value[:])

nstring.reverse()

for index, value in enumerate(nstring):    
    """ print(f' {unidades[index]:-<15}', end='')
        print(f' {value}{decimal[index]}')"""
    nreverse.append([unidades[index], value, decimal[index]])

nreverse.reverse() 
print(f'Seu número: {n}')
for index, value in enumerate(nreverse):       
    print(f'{value[0]:-<20} {value[1]}{value[2]}')
        
        