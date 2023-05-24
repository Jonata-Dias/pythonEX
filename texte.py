    
def converter(numero, tipo):
    resultado = ''
    if tipo == "bin":
            while numero > 0:
                resto = numero % 2               
                resultado = str(resto) + resultado
                print(resultado)
                numero //= 2
                
            return resultado

converter(10, 'bin')