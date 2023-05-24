# Escreva um programa que leia dois números inteiros
# e compare-os, mostrando na tela uma mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais

def get_int(msg):
    while True:
        try:
            n = int(input(msg).strip().replace(' ', ''))
        except(ValueError, TypeError):
            print('Digite um número inteiro válido!')
        else:
            return n


def comp_numeros(n1, n2):
    if n1 > n2:
        return f"O 1º valor é maior, sendo eles 1º: {n1} e 2º: {n2}."
    elif n2 > n1:
        return f"O 2º valor é maior, sendo eles 1º: {n1} e 2º: {n2}."   
    else:
        return f'Os números comparados são iguais, sendo eles 1º: {n1} e 2º: {n2}.' 


while True:
    n1 = get_int('Digite o 1º número: ')
    n2 = get_int('Digite o 2º número: ')
    resp = comp_numeros(n1, n2)                
    print(resp)
    while True:
        stop = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if stop not in 'SN':
            print('Por favor, digite apenas S ou N!')
        else:
            break
    if stop in 'N':
        break        
print('SISTEMA ENCERRADO, VOLTE SEMPRE!')    