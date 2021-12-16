from time import perf_counter
from itertools import count
from random import shuffle, randint


def defineQtdTestes():
    nTestes = int(input('Digite quantas vezes deseja testar os algoritmos: '))
    return nTestes


def calculaTempo(tempoInicial, tempoFinal):
    return round(tempoFinal - tempoInicial, 5)


def bubbleSort(listaAleatoria):
    for posFinal in range(len(listaAleatoria), 0, -1):
        desordenado = False
        for posAtual in range(posFinal-1):
            if listaAleatoria[posAtual] > listaAleatoria[posAtual + 1]:
                listaAleatoria[posAtual], listaAleatoria[posAtual + 1] = listaAleatoria[posAtual + 1], listaAleatoria[posAtual]
                desordenado = True
        if not desordenado:
            break
    return listaAleatoria


def insertionSort(listaAleatoria):
    c = count(1)
    contador = next(c)
    while contador < len(listaAleatoria):
        numeroDaVez = listaAleatoria[contador]
        posNumeroAnterior = contador - 1
        while posNumeroAnterior >= 0 and listaAleatoria[posNumeroAnterior] > numeroDaVez:
            listaAleatoria[posNumeroAnterior + 1] = listaAleatoria[posNumeroAnterior]
            posNumeroAnterior -= 1
        listaAleatoria[posNumeroAnterior + 1] = numeroDaVez
        contador = next(c)
    return listaAleatoria


def selectionSort(listaAleatoria):
    for posTrocado in range(len(listaAleatoria) - 1):
        posMenor = posTrocado
        for posLista in range(posTrocado, len(listaAleatoria)):
            if listaAleatoria[posMenor] > listaAleatoria[posLista]:
                posMenor = posLista
        if listaAleatoria[posTrocado] > listaAleatoria[posMenor]:
            listaAleatoria[posTrocado], listaAleatoria[posMenor] = listaAleatoria[posMenor], listaAleatoria[posTrocado]
    return listaAleatoria


def execucaoAlgoritmos(listaAleatoria, funcAlgoritmo):
    inicio = perf_counter()
    funcAlgoritmo(listaAleatoria)
    fim = perf_counter()
    return calculaTempo(inicio, fim)


def printEspecial(posicao, contadorEspecial, nomeAlgoritmo, listaResultado):

    print(f'Resultado do {posicao + 1}º teste do {nomeAlgoritmo}: Número de elementos'
          f' testados: {listaResultado[posicao*2]}, tempo gasto na tarefa:'
          f' {listaResultado[posicao + contadorEspecial]} segundos.')


def comparaçãoAlgoritmos(numeroDeTestes):
    resultadoBubble = []
    resultadoInsertion = []
    resultadoSelection = []
    c = count()
    contadorEspecial = next(c)

    for posTeste in range(numeroDeTestes):
        contadorEspecial = next(c)
        nElementos = randint(10000, 50000)
        listaGerada = [randint(0, nElementos) for elementos in range(nElementos)]
        shuffle(listaGerada)
        resultadoBubble.append(nElementos)
        resultadoBubble.append(execucaoAlgoritmos(listaGerada, bubbleSort))
        resultadoInsertion.append(nElementos)
        resultadoInsertion.append(execucaoAlgoritmos(listaGerada, insertionSort))
        resultadoSelection.append(nElementos)
        resultadoSelection.append(execucaoAlgoritmos(listaGerada, selectionSort))
        print('\n------------------------------------------------------------------------'
              '------------------------------------------------------------------------\n')
        printEspecial(posTeste, contadorEspecial, 'Bubble Sort', resultadoBubble)
        printEspecial(posTeste, contadorEspecial, 'Insertion Sort', resultadoInsertion)
        printEspecial(posTeste, contadorEspecial, 'Selection Sort', resultadoSelection)


def main():
    comparaçãoAlgoritmos(defineQtdTestes())


main()
