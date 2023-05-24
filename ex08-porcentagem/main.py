# Escreva um programa que pergunte o salário de um funcionario
# E calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores pu iguais, o aumento é de 15%.
print('-' * 40)
print('\033[32mColoque seu salário e veja seu aumento!\033[m')
print('-' * 40)

def aumento(sal, porcentagem=0):
    return  sal * (1 + porcentagem / 100)
    

def isfloat(msg):
    while True:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            if n == '':
                raise ValueError
            n = float(n)
        except ValueError:
            print('Por favor Digite um número real válido!')
        except TypeError:
            print('O tipo da entrada deve ser um número real válido!')
        except KeyboardInterrupt:
            print('O usuário optou por não digitar!')
        else:
            return n


while True:
    sal = isfloat('Digite seu salário R$: ')
    if sal > 1250:
        newsal = aumento(sal, 10)
        print(f'Seu novo salário é de R${newsal:.2f} com 10% de aumento!')
    else:
        newsal = aumento(sal, 15)
        print(f'Seu novo salário é de R${newsal:.2f} com 15% de aumento!')
    
    while True:
        stop = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if stop in 'NS':
            break    
        else:
            print('Opção inválida. Digite apenas SIM ou NÃO!')
    if stop == 'N':
        break    
print('FIM do programa volte sempre!!')
