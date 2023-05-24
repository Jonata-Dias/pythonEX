# Crie um programa que leia duas notas de um aluno e
# calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# -Média abaixo de 5: REPROVADO
# -Média entre 5 e 6.9: RECUPERAÇÃO
# -Média 7 ou superior: APROVADO
import re

print('\033[32mMÉDIA ESCOLAR\033[m'.center(40))

notas = []

def get_name():
     while True:
        try:
            nome = input('DIGITE O NOME DO ALUNO: ').strip().split()
            for palavra in nome:
                if not re.match(r'^[a-zA-Z]+$', palavra):
                    raise ValueError('Digite um nome válido contendo apenas letras.')
            return ' '.join(nome).capitalize()
        except ValueError as e:
            print(str(e))


def get_float(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',', '.'))
        except(ValueError, TypeError):
            print('DIGITE UM NÚMERO REAL VÁLIDO!')
        else:
            return n        


while True:
    nome = get_name()
    nota1 = get_float('PRIMEIRA NOTA: ')
    nota2 = get_float('SEGUNDA NOTA: ')
    media = (nota1 + nota2) / 2
    notas.append([nome, media])
    
    while True:
        stop = str(input('DESEJA CONTINUAR? [ S/N ] ')).upper().strip()[0]
        if stop not in 'SN':
            print('DIGITE APENAS S OU N.')
        else:
            break
    if stop == 'N':
        break    

for index, value in enumerate(notas):
    print(f'{value[0]} ')
    if value[1] < 5:
        print(f'Sua média foi {value[1]} e você foi reprovado.\n') 
    elif value[1] < 7:
        print(f'Sua média foi {value[1]} e você está de recuperação.\n')
    else:
        print(f'PARABÉNS! Sua média foi {value[1]} e você foi aprovado.\n')          