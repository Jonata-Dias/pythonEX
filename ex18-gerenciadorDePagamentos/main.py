# Elabore um programa qye calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condiçâo de pagamento:
# -À vista dinheiro \ cheque: 10% de desconto
# -À vista no cartâo: 5% de desconto
# -Em até 2X no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

lista_menu = ['À vista dinheiro / cheque: 10% de desconto', 
                'À vista no cartâo: 5% de desconto', 
                'Em até 2X no cartão: preço normal', 
                '3x ou mais no cartão: 20% de juros',
                'Sair do sistema']

def linha(simbolo='-', tam=40):
    print(f'{simbolo}' * tam)


def get_float(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',', '.'))
            if n <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print('Digite um número real positivo válido.')
        else:
            return n


def get_int(msg):
    while True:
        try:
            n = int(input(msg).strip())
            if n < 0:
                raise ValueError
        except (ValueError, TypeError):
            print('digite um numero inteiro posítivo válido')    
        else:
            return n


def menu(lista):
    print('FORMA DE PAGAMENTO'.center(40))
    for index, item in enumerate(lista):
        print(f'{index} - {item}')
    linha()   
    opcao = get_int('Sua escolha de pagamento: ')
    linha()
    return opcao


def juros(value, porcentagem=0):
    return value * (1 + porcentagem / 100)


def desconto(value, porcentagem=0):
    return value * (1 - porcentagem / 100)


while True: 
    linha()
    print('LOJA DIAS'.center(40))
    linha()
    valor = get_float('Valor a ser cobrado: ')
    linha()
    resp = menu(lista_menu)
    total = 0
    if resp < len(lista_menu):
        if resp == 0:
            total =  desconto(valor, 10)
        elif resp == 1:
            total = desconto(valor, 5)
        elif resp == 2:
            total = valor
            parcelas = valor / 2
            print(f'Sua compra será parcelada em 2X de {parcelas:.2f} sem juros.')
        elif resp == 3:
            total = juros(valor, 20)
            tot_parcelas = get_int('Digite em quantas vezes deseja dividir sua compra: ')
            parcelas = total / tot_parcelas
            print(f'Sua compra será parceladas em {tot_parcelas}X de R$ {parcelas:.2f} com juros.')
        elif resp == 4:
            break
        print(f'Sua compra de {valor:.2f} vai custar R$ {total:.2f} no final.')  
    else:
        print('Digite um opção válida!')    
    
linha()
print('Fim do atendimento. TENHA UM BOM DIA!!!')  
linha()    