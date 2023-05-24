# Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar
# um triângulo.
print('-' * 40)
print('\033[32mDIGITE TRÊS RETAS E DESCUBRA SE FORMA UM TRIÂNGULO!\033[m]'.center(40))
print('-' * 40)

def isint(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            if n == '':
                raise ValueError
            n = int(n)
        except (ValueError, TypeError):
            print('Por favor, digite um número inteiro válido!')
        except KeyboardInterrupt:
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
    while True:
        while True:
            reta = isint(f'Digite a {count}ª reta do triângulo: ')     
            if reta <= 0:
                print("As medidas informadas devem ser maiores que zero. Tente novamente.")
            else:
                count += 1
                medidas.append(reta)
                break    
        if count > 3:
            break       
    if form_triangle(medidas):
        print("As retas informadas formam um triângulo.\n")   
    else:
        print("As retas informadas não formam um triângulo. Tente novamente.\n")
    while True:
        stop = str(input('Deseja continuar? [ S/N ]')).upper().strip()[0]
        if stop in 'SN':
            break
        else:
            print('Opção inválida. Por favor digite SIM ou NÃO!')
    if stop == 'N':
        break        
print()  
print('\033[32mFim do programa!!\033[m]') 
print() 