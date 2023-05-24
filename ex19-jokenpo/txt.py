color = ['\033[31m', '\033[32m', '\033[33m', '\033[m']

def paint(cor=0, msg='', endcor=3):
    return f'{color[cor]}{msg}{color[endcor]}'

resp = paint(0, 'VENCEU!')
print(resp)