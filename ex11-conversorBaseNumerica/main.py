# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
from funcoes import *

''' converssor usando função interna
def converter(numero, tipo):
    if tipo == "bin":
        return format(numero, "b")
    elif tipo == "oct":
        return format(numero, "o")
    elif tipo == "hex":
        return format(numero, "x")
    else:
        return "Tipo de conversão inválido!"
'''

while True:
    resp = menu(['BINÁRIO', 'OCTAL', 'HEXADECIMAL', 'FINALIZAR PROGRAMA'])
    if resp == 1:
        print('CONVERSOR BINARIO')
        bin = get_int('Digite seu número: ')
        print(converter(bin, "bin"))
    elif resp == 2:
        print('CONVERSOR OCTAL')
        oct = get_int('Digite seu número: ')
        print(converter(oct, "oct"))
    elif resp == 3:
        print('CONVERSOR EXADECIMAL')
        hex = get_int('Digite seu número: ')
        print(converter(hex, "hex"))                   
    elif resp == 4:
        print('Fim do programa.')
        break    
    else:
        print('Digite uma opção válida!')