# Faça um programa que leia o comprimento do cateto oposto e do cateto
# Adjacente de um triãngulo retângulo, calcule e mostre o
# Comprimento da hipotenusa.

from math import hypot

def isfloat(msg):
    while True:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            if n == '':
                raise ValueError
            n = float(n)
        except(TypeError, ValueError):
            print('Digite um número REAL válido!!')
        except KeyboardInterrupt:
            print('O usuário preferrio não digitar!')
        else:
            return n
    

catetooposto = isfloat('Cateto oposto: ')
catetoadj = isfloat('Cateto adjacente: ')
# Formula matematica
# hipotenusa = (catetooposto ** 2 + catetoadj ** 2) ** (1/2)
# biblioteca MATH
hipotenusa = hypot(catetooposto, catetoadj)
print(f'O valor da hipotenusa é de {hipotenusa:.2f}')
