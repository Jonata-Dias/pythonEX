def linha(tam=40):
    print('-' * tam)


def cabeçalho(msg):
    linha()
    print(f'{msg}'.center(40))
    linha()    


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('POR FAVOR, digite um número inteiro válido!!')
        except KeyboardInterrupt:
            print('O usúario preferiu não digitar!')
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()  
    opc = leiaInt('SUA OPÇÃO: ')
    return opc    