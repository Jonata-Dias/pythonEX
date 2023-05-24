# Leia o nome de 4 alunos e mostre a ordem sorteada.
from random import shuffle

nomes = list() 

def isnome(msg): 
     
    while True:
        nome = str(input(msg)).capitalize().strip()
        if nome.isalpha():
            return nome
        else:
            print('Por favor digite seu nome!!')
        


print('-' * 40)
print('SORTEIE QUEM COMEÇA'.center(40))
print('-' * 40)

for count in range(0, 4):
    nome = isnome(f'Digite o {count + 1} nome: ')   
    nomes.append(nome[:])
    
print(nomes)  
shuffle(nomes)  
print(f'A ordem sorteada foi {nomes}')
