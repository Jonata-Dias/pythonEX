"""
    Crie um pequeno sistema modularizado que permita cadastrar
    pessoas pelo seu nome e idade em um arquivo de textos simples.
    O sistema só vai ter duas opções: cadastrar uma nova pessoa
    e listar todas as pessoas cadastradas.
"""
from tools.uteis import *
from tools.sistema import *

arq = 'listanome.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)

while True:
   resp = menu(['VER PESSOAS CADASTRADAS', 'ADICIONAR NOVA PESSOA', 'SAIR DO SISTEMA'])
   if resp == 1:
      lerArquivo(arq)
   elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
   elif resp == 3:
      cabeçalho('Saindo do sistema!!!')
      break
   else:
      print('Opção inválida digite novamente!!!') 
