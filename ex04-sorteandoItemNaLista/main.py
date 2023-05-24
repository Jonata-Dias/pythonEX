# Leia quatro nomes e sorteie um deles aleatoriamente.

import random
nomes = list()

print('-' * 40)
print('SORTEANDO UM NOME NA LISTA'.center(40))
print('-' * 40)

while True:
    nome = str(input('Digite um nome: '))
    nomes.append(nome[:])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break    
sorteio = random.choice(nomes)
print(nomes)   
print(f'O nome escolhido foi {sorteio}.') 
