# Crie um programa que leia um número Real qualquer e mostre sua
# Porçao inteira. Ex: número: 6.124 inteiro 6.

def isreal(number):
    while True:
        try:
            n = str(input(number)).replace(',', '.').strip()
            n = float(n)
        except(TypeError, ValueError):
            print('Digite um número real válido!')
        except KeyboardInterrupt:
            print('O usuário decidiuo não digitar!')
        else:
            return n

numberReal = isreal('Digite um número REAL: ')
print(f'O valor digitado foi {numberReal} e a sua' 
      f'porção inteira é {int(numberReal)}')
