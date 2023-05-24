
def nfloat(msg):
    while True:
        try:
            numerofloat = str(input(msg)).replace(',', '.')
            numerofloat = float(numerofloat)
        except(ValueError, TypeError):
            print('POR FAVOR, Digite um número válido!!')
        except KeyboardInterrupt:
            print('O usuário preferio não digitar.')
        else:
            return numerofloat
    

def nInt(msg):
    while True:
        try:
            numeroint = int(input(msg))
        except(ValueError, TypeError):
            print('POR FAVOR, Digite um número válido!!')
        except KeyboardInterrupt:
            print('O usuário preferio não digitar.')
        else:
            return numeroint
    