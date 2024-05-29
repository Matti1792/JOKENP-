import os
from random import randint
import time
import random

# Definindo as opções do jogo
itens = ('Pedra', 'Papel', 'Tesoura')
intens = ('ROCK', 'PAPER', 'SCISSORS')

# Dicionário para as cores
c = {'limpar': '\033[m',
     'vermelho': '\033[31m',
     'verde': '\033[32m',
     'magenta': '\033[35m'
     }

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def lang() :
    print('''   LANG OPTIONS
    1. PT-BR
    2. EN-US''')
    la = int(input('Choose your language: '))
    if la == 1:
        jokenpo_pt()
    elif la == 2:
        jokenpo_en()
    else:
        print('{}Invalid option.{}'.format(c['vermelho'], c['limpar']))
        lang()


def jokenpo_pt():
    clear_screen()

    print('=-' * 11)
    print('       {}JOKENPÔ{}'.format(c['magenta'], c['limpar']))
    print('=-' * 11)

    print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
    
    jogador = int(input('Qual é a sua jogada? '))
    computador = randint(0, 2)

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

    again_pt() 
def again_pt():
    print('_' * 20)
    p = str(input('Quer jogar denovo? [Y/N] ')).strip()
    if p.upper() == 'Y':
        jokenpo_pt()
    elif p.upper() == 'N':
        print('Até a proxima')
    else:
        print('Opção inválida')
        again_pt()

#=================================================================================================================================================
        1
def jokenpo_en():
    clear_screen()
    print('=-' * 17)
    print('       {}ROCK PAPER SCISSORS{}'.format(c['magenta'], c['limpar']))
    print('=-' * 17)

    print('''Your options:
      [ 0 ] ROCK
      [ 1 ] PAPER
      [ 2 ] SCISSORS''')

    jogador = int(input('What is your move? '))
    computador = random.randint(0, 2)

    print('{}RO{}'.format(c['vermelho'], c['limpar'])) 
    time.sleep(1)
    print('{}CK{}'.format(c['vermelho'], c['limpar']))
    time.sleep(1)
    print('{}PAPER!!!{}'.format(c['vermelho'], c['limpar']))
    time.sleep(1)

    print('=-' * 12)
    print('The computer played {}'.format(intens[computador]))
    print('Player played {}'.format(intens[jogador]))
    print('=-' * 12)

    if computador == 0:  # ROCK
        if jogador == 0:
            print('{}DRAW{}'.format(c['verde'], c['limpar']))
        elif jogador == 1:
            print('{}PLAYER WINS{}'.format(c['verde'], c['limpar']))
        elif jogador == 2:
            print('{}COMPUTER WINS{}'.format(c['vermelho'], c['limpar']))
        else:
            print('{}INVALID MOVE{}'.format(c['vermelho'], c['limpar']))

    elif computador == 1:  # PAPER
        if jogador == 0:
            print('{}COMPUTER WINS{}'.format(c['vermelho'], c['limpar']))
        elif jogador == 1:
            print('{}DRAW{}'.format(c['verde'], c['limpar']))
        elif jogador == 2:
            print('{}PLAYER WINS{}'.format(c['verde'], c['limpar']))
        else:
            print('{}INVALID MOVE{}'.format(c['vermelho'], c['limpar']))

    elif computador == 2:  # SCISSORS
        if jogador == 0:
            print('{}PLAYER WINS{}'.format(c['verde'], c['limpar']))
        elif jogador == 1:
            print('{}COMPUTER WINS{}'.format(c['vermelho'], c['limpar']))
        elif jogador == 2:
            print('{}DRAW{}'.format(c['verde'], c['limpar']))
        else:
            print('{}INVALID MOVE{}'.format(c['vermelho'], c['limpar']))

    again_en()

def again_en():
    print('_' * 20)
    p = str(input('Do you want to play again? [Y/N] ')).strip()
    if p.upper() == 'Y':
        jokenpo_en()
    elif p.upper() == 'N':
        print('Goodbye')
    else:
        print('Invalid option')
        again_en()



lang()
