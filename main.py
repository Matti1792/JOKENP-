from random import randint
import time


# Definindo as opções do jogo
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# Dicionário para as cores
c = {'limpar': '\033[m',
     'vermelho': '\033[31m',
     'verde': '\033[32m',
     'magenta': '\033[35m'
     }

def jokenpô():

    print('=-' * 11)
    print('       {}JOKENPÔ{}'.format(c['magenta'], c['limpar']))
    print('=-' * 11)

    print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
    
    jogador = int(input('Qual é a sua jogada? '))

    print('{}JO{}'.format(c['vermelho'], c['limpar']))
    time.sleep(1)
    print('{}KEN{}'.format(c['vermelho'], c['limpar']))
    time.sleep(1)
    print('{}PÔ!!!{}'.format(c['vermelho'], c['limpar']))
    time.sleep(1)

    print('=-' * 12)
    print('O computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('=-' * 12)

    if computador == 0: #PEDRA
        if jogador == 0:
            print('{}EMPATE{}'.format(c['verde'], c['limpar']))
        elif jogador == 1:
            print('{}JOGADOR VENCEU{}'.format(c['verde'], c['limpar']))
        elif jogador == 2:
            print('{}COMPUTADOR VENCE{}'.format(c['vermelho'], c['limpar']))
        else:
            print('{}JOGADA INVALIDA{}'.format(c['vermelho'], c['limpar']))


    if computador == 1: #PAPEL
        if jogador == 0:
            print('{}COMPUTADOR VENCE{}'.format(c['vermelho'], c['limpar']))
        elif jogador == 1:
            print('{}EMPATE{}'.format(c['verde'], c['limpar']))
        elif jogador == 2:
            print('{}JOGADOR VENCEU{}'.format(c['verde'], c['limpar']))
        else:
            print('{}JOGADA INVALIDA{}'.format(c['vermelho'], c['limpar']))


    if computador == 2: #TESOURA
        if jogador == 0:
            print('{}JOGADOR VENCE{}'.format(c['verde'], c['limpar']))
        elif jogador == 1:
            print('{}COMPUTADOR VENCE{}'.format(c['vermelho'], c['limpar']))
        elif jogador == 2:
            print('{}EMPATE{}'.format(c['verde'], c['limpar']))
        else:
            print('{}JOGADA INVALIDA{}'.format(c['vermelho'], c['limpar']))

    again() 
def again():
    print('_' * 20)
    p = str(input('Quer jogar denovo? [Y/N] ')).strip()
    if p.upper() == 'Y':
        jokenpô()
    elif p.upper() == 'N':
        print('Até a proxima')
    else:
        print('Opção inválida')
        again()



jokenpô()