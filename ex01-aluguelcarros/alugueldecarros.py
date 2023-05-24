# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa r$60 por dia e r$0.15
# por Km rodado.

from funcoes import *   
    

km = nfloat('Digite a quantidade de Km percorridos: ')  
diasusado = nInt('Digite a quantidade de dias udados: ')

total = (km * 0.15) + (60 * diasusado)

print(f'O carro alugado foi usado por {diasusado} dias, {km:.1f}Km rodados com um valor total de R${total:.2f} a pagar.')

