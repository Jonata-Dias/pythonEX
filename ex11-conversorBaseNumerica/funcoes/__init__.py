# converssor usando matematica básica
def converter(numero, tipo):
    resultado = ""
    if tipo == "bin":
        while numero > 0:
            resto = numero % 2
            resultado = str(resto) + resultado
            numero //= 2
        return resultado
    elif tipo == "oct":
        while numero > 0:
            resto = numero % 8
            resultado = str(resto) + resultado
            numero //= 8
        return resultado
    elif tipo == "hex":
        while numero > 0:
            resto = numero % 16
            if resto < 10:
                resultado = str(resto) + resultado
            else:
                resultado = chr(resto + 55) + resultado
            numero //= 16
        return resultado
    else:
        return "Tipo de conversão inválido!"
    

def cabecalho(msg):
    print('-' * 40)
    print(f'{msg}'.center(40))
    print('-' * 40)


def get_int(msg):
    while True:
        try:
            n = int(input(msg).strip().replace(' ', ''))
        except(ValueError, TypeError):
            print('Digite um número inteiro válido.')  
        else:
            return n      
        

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for index, item in enumerate(lista):
        print(f'{index + 1} - {item}')
    opc = get_int('SUA OPÇÃO: ')
    return opc
