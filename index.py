from arquivos import *
from verifcacoes import *
from random import choice
import os


# Cria um índice invertido com as letras de uma palavra
def separarLetras(plv):
    indice = dict()

    for i, letra in enumerate(plv):
        if letra not in indice:
            indice[letra] = list()

        if letra in indice:
            indice[letra].append(i)

    return indice

# Verifica acertos, erros ou "quases"
def compararPalavras(indice_base, indice_chute, plv_chute):
    copia_palavra = list(plv_chute)
    for letra in indice_base:
        cont_acerto = 0
        acerto = False
 
        if letra in indice_chute:
            # Troca as letras que estão na posição certa por '1' (acerto)
            for indice in indice_base[letra]:
                if indice in indice_chute[letra]:
                    cont_acerto += 1
                    copia_palavra.insert(indice, '1')
                    copia_palavra.pop(indice+1)

            # Verifica se tal letra já foi acertada em todas as suas ocorrencias na palavra base
            if cont_acerto == len(indice_base[letra]):
                acerto = True

            # Troca as letras que estão na palavra mas não nas posições certas por '2' (quase)
            for indice in indice_chute[letra]:
                if indice not in indice_base[letra] and not acerto:
                    copia_palavra.insert(indice, '2')
                    copia_palavra.pop(indice+1)

    casos = ['0', '1', '2'] # Casos de acerto, "quase" ou erro
    # Substitui letras que não estão na palavra_base 
    # ou já foram totalmente acertadas por '0'
    for i, letra in enumerate(copia_palavra[:]):
        if letra not in casos:
            copia_palavra.insert(i, '0')
            copia_palavra.pop(i+1)

    return copia_palavra


# Colore a palavra chutada de acordo com acertos, erros ou "quases"
def colorirLetras(cods):
    palavras_coloridas = list()

    for cod in cods:
        plv_col = ''
        for i in range(5):
            if cod[0][i] == '0':
                plv_col += '\033[;43m {} \033[m'.format(cod[1][i].upper())
            
            elif cod[0][i] == '1':
                plv_col += '\033[;41m {} \033[m'.format(cod[1][i].upper())

            elif cod[0][i] == '2':
                plv_col += '\033[;44m {} \033[m'.format(cod[1][i].upper())

        palavras_coloridas.append(plv_col)

    return palavras_coloridas


# Verifica se o jogador excedeu o número máximo de rodadas (5)
def ganhouPerdeu(cods):
    if len(cods) >= 5:
        return False
    return True
    

# Sorteia uma palavra aleatória de 5 letras
def sortearPalavra():
    # palavras foram pegas daqui: https://www.ime.usp.br/~pf/dicios/br-utf8.txt
    with open('palavras5letras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.readlines()
        for i in range(len(palavras)):
            palavras[i] = palavras[i][:-1]

    return choice(palavras)


# Processa e colore as letras corretas e erradas da palavra informada pelo jogador
def processarJogada(pal, ind_chute, ind_base):
    cod_resultado = compararPalavras(ind_base, ind_chute, pal) #codigos de resultado
    guardarEmBinario(cod_resultado, pal)

    lista_palavras = list()
    recuperarDoBinario(lista_palavras)
    pal_coloridas = colorirLetras(lista_palavras)

    return pal_coloridas


# Verifica se o jogador acertou ou errou a palavra (depois de 5 tentativas)
def verificarAcerto(pal, pal_base, pal_coloridas):
    continuar_rodada = True
    if pal != pal_base:
        if not ganhouPerdeu(pal_coloridas):
            print('Você perdeu!\nPalavra sorteada: {}'.format(pal_base))
            continuar_rodada = False

    else:
        print('Você acertou a palavra!')
        continuar_rodada = False

    return continuar_rodada


def sobreCores():
    os.system('cls')

    print(f'{"SIGNIFICADO DAS CORES":^40}')
    print('\033[;43m   \033[m - LETRA NÃO EXISTE NA PALAVRA')
    print('\033[;44m   \033[m - LETRA EXISTE, MAS ESTÁ NA POSIÇÃO ERRADA ')
    print('\033[;41m   \033[m - LETRA EXISTE E ESTÁ NA POSIÇÃO CORRETA\n')


def ajuda():
    print('COMO JOGAR')
    print('1) Uma palavra de 5 letras será sorteada')
    print('2) O jogador deverá, em 5 tentativas, tentar acertar qual é essa palavra')
    print('3) A palavra que o jogador chutar terá, em cada letra, uma cor, com os respectivos significados:')

    sobreCores()


def jogar():
    limparBinario()
    palavra_base = sortearPalavra()

    os.system('cls')
    sobreCores()

    indice_base = separarLetras(palavra_base)
        
    continuar_rodada = True
    while continuar_rodada:
        palavra = input("Termo: ").lower()
        while len(palavra) != 5 or not verificarExistencia(palavra):
            palavra = input("Termo inválido! Informe uma palavra: ").lower()

        indice_chute = separarLetras(palavra)
        palavras_coloridas = processarJogada(palavra, indice_chute, indice_base)

        os.system('cls')
        sobreCores()

        for palavras in palavras_coloridas:
            print(palavras)
            print('')

        continuar_rodada = verificarAcerto(palavra, palavra_base, palavras_coloridas)
    

def menu():
    opc = 4
    while (opc != 3):
        print("\nTERMO")
        print("[1] - Jogar")
        print("[2] - Ajuda")
        print("[3] - Sair")
        opc = int(input("Informe o que deseja fazer: "))
        while opc not in [1, 2, 3]:
            opc = int(input("Entrada inválida! Informe o que deseja fazer: "))

        if (opc == 1):
            jogar()

        elif (opc == 2):
            ajuda()


os.system('cls')
menu()
print("\nJogo finalizado!")




