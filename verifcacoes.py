# Verifica do site Dicio.com.br
def buscarPalavra(lista, chave):
    inicio = 0
    fim = len(lista) -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] > chave:
            fim = meio - 1

        elif lista[meio] < chave:
            inicio = meio + 1
            
        else:
            return True

    return False


def verificarExistencia(termo):
    lista_palavras = list()
    with open('palavras5letras.txt', 'r', encoding='utf-8') as arquivo:
        for palavra in arquivo:
            lista_palavras.append(palavra[:-1])

    if buscarPalavra(lista_palavras, termo):
        return True

    return False


