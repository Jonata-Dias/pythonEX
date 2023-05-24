print('-' * 40)
print('\033[32mDIGITE TRÊS RETAS E DESCUBRA SE FORMA UM TRIÂNGULO!\033[m]'.center(40))
print('-' * 40)
def is_int():
    while True:
        try:
            n = int(input('Digite um número inteiro: ').strip())
            if n <= 0:
                raise ValueError
        except (ValueError, TypeError, KeyboardInterrupt):
            print('Por favor, digite um número inteiro válido!')
        else:
            return n


def form_triangle(sides):
    if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
        return True
    else:
        return False


while True:
    medidas = []
    count = 1
    while count <= 3:
        reta = is_int()
        medidas.append(reta)
        if reta <= 0:
            print("As medidas informadas devem ser maiores que zero. Tente novamente.")
        else:
            count += 1

    if form_triangle(medidas):
        print("As retas informadas formam um triângulo.")
    else:
        print("As retas informadas não formam um triângulo. Tente novamente.")
    while True:
        stop = str(input('Deseja continuar? [ S/N ]')).upper().strip()[0]
        if stop in 'SN':
            break
        else:
            print('Opção inválida. Por favor digite SIM ou NÃO!')
    if stop == 'N':
        break        
print()  
print('\033[32mFim do programa!!\033[m') 
print() 