from pickle import dump, load


def guardarEmBinario(dado, plv):
    with open('palavras.dat', 'ab') as arquivo:
        dump([dado, plv], arquivo)


def recuperarDoBinario(palavras):
    with open('palavras.dat', 'rb') as arquivo:
        while True:
            try:
                palavras.append(load(arquivo))

            except EOFError:
                break


def limparBinario():
    with open('palavras.dat', 'wb') as arquivo:
        arquivo.truncate(0)
        arquivo.seek(0)