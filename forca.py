# atualização de commit

import random

def forca(palavra):
    erro = 0
    nivel = ['',
             '________        ',
             '|               ',
             '|       |       ',
             '|       0       ',
             '|      /|\      ',
             '|      / \      ',
             '|               '
             ]
    restante = list(palavra)
    tabuleiro = ['__'] * len(palavra)
    win = False
    print('Bem vindo à forca!')
    while erro < len(nivel) - 1:
        print('\n')
        msg = 'Adivinhe uma letra: '
        letra = input(msg)
        if letra in restante:
            while letra in restante:
                cind = restante.index(letra)
                tabuleiro[cind]  = letra
                restante[cind] = '$'
        else:
            erro += 1
        print(' '.join(tabuleiro))
        e = erro + 1
        print('\n'.join(nivel[0: e]))
        if '__' not in tabuleiro:
            print('Você venceu!')
            print(' '.join(tabuleiro))
            win = True
            break
    if not win:
        print('\n'.join(nivel[0: erro]))
        print(f'Você perdeu! A palavra era {palavra}.')

palavras = [
    "abacaxi", "bola", "cachorro", "dado", "elefante", "faca", "gato", "hospital", "igreja", "janela",
    "kiwi", "limao", "macaco", "navio", "ovo", "peteca", "queijo", "rato", "sapato", "tatu",
    "uva", "vela", "waffle", "xadrez", "yamaha", "zebra", "amor", "bicicleta", "casa", "dente",
    "estrela", "fogo", "gelo", "helicoptero", "ilha", "jardim", "koala", "lua", "mesa", "nuvem",
    "ouro", "ponte", "quadro", "rio", "sol", "telefone", "urso", "vulcao", "web", "xicara",
    "yakult", "zero", "anel", "bola", "ceu", "diamante", "escada", "foguete", "girafa", "homem",
    "inseto", "janela", "kombat", "lapis", "mochila", "navio", "olho", "pato", "quebra", "roda",
    "sino", "trem", "universo", "vassoura", "whisky", "xenon", "yoga", "zoologico", "arte", "banco",
    "computador", "dados", "espelho", "festa", "garfo", "horta", "ima", "jornal", "kiwi", "livro",
    "marmita", "nuvem", "onda", "papel", "queijo", "relogio", "sorvete", "tijolo", "unha", "vidro"
]

sorteio = random.choice(palavras)
forca(sorteio)