
unidades = ['unidades', 'dezenas', 'centenas', 'milhar', 'dezena de milhar', 'centena de milhar']
decimal = ['', '0', '00', '000', '0000', '00000']

while True:
    try:
        n = int(input('Digite um número: '))
        break
    except ValueError:
        print('Digite um número válido!!')

nstring = [value for value in str(n)[::-1]]

nreverse = [[unidades[index], value, decimal[index]] for index, value in enumerate(nstring)]

print(f'Seu número: {"".join(nstring[::-1])}')
for value in nreverse[::-1]:       
    print(f'{value[0]:-<20} {value[1]}{value[2]}')
