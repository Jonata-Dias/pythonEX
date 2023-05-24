# Desenvolva uma lógica que leia o peso e altura de uma
# pessoa, calcule seu IMC e mostre seu status, de acordo
# com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do Peso.
# -Entre 18.5 e 25: Peso ideal.
# -25 até 30: Sobrepeso.
# -30 até 40: Obesidade
# -Acima de 40: Obesidade mórbida.

def get_float(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',', '.'))
            
            if n <= 0:
                raise ValueError
        except(ValueError, TypeError):
            print('Digite um número REAL e POSITIVO válido.')    
        else:
            return n
        

def get_imc(imc):
    if imc < 18.5:
        return f'Você tem um IMC de {imc:.2f} e está abaixo do peso recomendado par sua altura.'
    elif imc < 25:
        return f'Você tem um IMC de {imc:.2f} e está com peso ideal recomendado par sua altura.'
    elif imc < 30:
        return f'Você tem um IMC de {imc:.2f} e está com sobrepeso.'
    elif imc < 40:
        return f'Você tem um IMC de {imc:.2f} e está OBESO.'
    else:
        return f'Você tem um IMC de {imc:.2f} e está com OBESIDADE MÓRBIDA.'
    

while True:
    peso = get_float('Digite quantos quilos você pesa: ')
    alt = get_float('Digite sua altura em centímetros: ')
    if alt.is_integer(): # verificaçao para ver se é um numero inteiro e passando para centimetros
        alt = alt / 100
    print(alt)
    imc = peso / alt ** 2
    resp = get_imc(imc)
    print(resp)

    while True:
        stop = str(input('Deseja fazer novo calcúlo? [ S/N ] ')).strip().upper()[0]
        if stop not in 'SN':
            print('Digite apensa S para fazer novo calcúlo ou N para sair do programa.')
        else:
            break
    if stop == 'N':
        break

print('\nFIM DO PROGRAMA!\n')