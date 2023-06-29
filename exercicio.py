from random import randint
computador = randint(1, 10)
print(f'{"="*44}\nO computador já escolheu um número de 1 a 10\n{"Tente adivinhar !":^44}\n{"="*44}')
jogador = int(input('\033[33mDigite seu palpite: '))
tentativas = 1
dica = ''
while jogador != computador:
    if jogador > computador:
        dica = 'menos'
    else:
        dica = 'mais'
    print(f'\033[31mErrou, é {dica} que {jogador}! tente mais uma vez!')
    jogador = int(input('\033[33mDigite seu palpite: '))
    tentativas += 1
print(f'\033[32mAcertou, parabens! Você precisou de \033[m{tentativas}\033[32m tentativas para acertar')
