# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint

itens_game = ['Pedra'.upper(), 'Papel'.upper(), 'Tesousa'.upper(), 'FINALIZAR']
color = ['\033[31m', '\033[32m', '\033[33m', '\033[m']

def paint(cor=0, msg='', endcor=3):
    return f'{color[cor]}{msg}{color[endcor]}'


def get_int():
    while True:
        try:
            n = int(input().strip())
            if n < 0:
                raise ValueError
        except ValueError:
            print('Digite um número inteiro e positivo válido.')
        else:
            return n
        

def menu(lista):
    print('-' * 40)
    print('JOKENPÔ GAME'.center(40))
    print('-' * 40)
    print('Escolha um opção de jogada.')
    for key, item in enumerate(lista):
        print(f'[ {key} ] - {item}')
    

while True:
    pc_move = randint(0, 2)
    menu(itens_game)
    print('Sua opção: ', end='')
    jogador = get_int()
    if jogador > 3:
        print('\033[31mJogada ínvalida, tente novamente.\n\033[m')
    elif jogador == 3:
        print('FIM DO JOGO')
        break    
    else:
        print(f'O computador jogou {paint(2, itens_game[pc_move])}.')  
        print(f'Você jogou {paint(2, itens_game[jogador])}.')

        if pc_move == 0:
            if jogador == 0:
                print(f'{paint(2, "EMPATE!")}')
            elif jogador == 1:
                print(f"{paint(1, 'VOCÊ VENCEU')}.")
            elif jogador == 2:
                print(f"{paint(0, 'VOCÊ PERDEU')}.")  
        elif pc_move == 1:
            if jogador == 0:
                print(f"{paint(0, 'VOCÊ PERDEU')}.")  
            elif jogador == 1:              
                print(f'{paint(2, "EMPATE!")}')
            elif jogador == 2:
                print(f"{paint(1, 'VOCÊ VENCEU')}.")         
        elif pc_move == 2:
            if jogador == 0:
                print(f"{paint(1, 'VOCÊ VENCEU')}.")
            elif jogador == 1:
                print(f"{paint(0, 'VOCÊ PERDEU')}.")  
            elif jogador == 2:                
                print(f'{paint(2, "EMPATE!")}') 
                
    