"""
    Faça um programa que leia três números e mostre qual é
    O maior e qual é o menor.
"""

def isnumber(msg=''):
    while True:
        try:
            n = str(input(msg))
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
      

menor = 0
maior = 0
for i in range(0, 3):
    number = isnumber(f'Digite {i + 1}º número: ')
    
    if i == 0:
        menor = maior = number
    else:
        if number > maior:  
            maior = number
        if number < menor:  
            menor = number    
print(f'O maior número foi {maior}')
print(f'O menor número foi: {menor}')  

                