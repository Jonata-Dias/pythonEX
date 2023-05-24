# Refaça o desafio 35 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais
# -Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('\033[32mDIGITE TRÊS RETAS E DESCUBRA SE FORMA UM TRIÂNGULO!\033[m]'.center(40))

def get_int(msg):
    while True:
        try:
            n = int(input(msg).strip())
            if n <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print('DIGITE UM NÚMERO POSITIVO INTEIRO VÁLIDO!')
        else:
            return n    
        

def get_triangulo(sides):
    if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
        if sides[0] == sides[1] == sides[2]:
            return 'Triângulo EQUILÁTERO.\n'
        elif sides[0] != sides[1] != sides[2] != sides[0]:
            return 'Triângulo ESCALENO.\n'
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return 'Triângulo ISÓCELES.\n'
    else:
        return 'NÃO FORMA UM TRIÂNGULO.\n'    
    

while True:
    medidas = []
    count = 1
    while True:
        retas = get_int(f'Digite a {count}ª reta: ')   
        medidas.append(retas) 
        count += 1    
        if count > 3:
            break
    print()    
    resp = get_triangulo(medidas)
    print(resp)    
    while True:
        stop = str(input('Deseja continuar? [ S/N ] ')).upper().strip()[0]
        if stop in 'SN':
            break
        else:
            print('\nOpção inválida. Por favor digite SIM ou NÃO!\n')
    if stop == 'N':
        break 

print('\nFIM DO PROGRAMA!!!!\n'.center(40))    