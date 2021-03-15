import datetime
import random
from time import perf_counter_ns
from time import perf_counter
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")
import numpy as np

def gerar_vetor_ordenado(n):
    lista = random.sample(range(1, 999999), n)
    lista.sort()
    return lista

def gerar_vetor_inversamente_ordenado(n):
    lista = random.sample(range(1, 999999), n)
    lista.sort(reverse=True)
    return lista

def gerar_vetor_aleatorio(n):
    lista = random.sample(range(1, 999999), n)
    return lista

def gerar_vetor_repetido(n):
    lista = [random.randint(1, 999999)] * n
    return lista

def exercicio_um(numero_entradas):
    # Qual é o menor valor de entrada n (considere n > 0) tal que
    # um algoritmo cujo tempo de execução é 10n^2 é mais rápido
    # que um algoritmo cujo tempo de execução é 2^n?
    # Qual desses algoritmos você considera mais eficiente?

    func_quadratica = []
    func_exponencial = []
    for x in range(1, numero_entradas):
        quadratico = 10 * (x ** 2)
        exponencial = (2 ** x)
        func_quadratica.append(quadratico)
        func_exponencial.append(exponencial)

    menor_valor = func_quadratica.index([i for i, j in zip(func_quadratica, func_exponencial) if j > i][0]) + 1

    print("O menor valor para qual 10n^2 é mais rápido que 2^n é :", menor_valor)
    print("Assumindo a análise assintótica, o melhor algoritmo é o quadrático.")

    y = np.linspace(1, numero_entradas - 1, numero_entradas - 1)
    plt.figure(figsize=(8, 6))
    plt.title("Exercício 1", y=1.1)
    plt.plot(y, func_quadratica, 'co')
    plt.plot(y, func_quadratica, c='cyan', label="10n^2")
    plt.plot(y, func_exponencial, 'go')
    plt.plot(y, func_exponencial, c='green', label="2^n")
    plt.plot(y[menor_valor - 1], func_quadratica[menor_valor - 1], 'rx', label="Menor valor que 10n^2 é mais eficiente")
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=3, borderaxespad=0)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução")
    plt.show()


def exercicio_dois(valores_ate):
    # Implemente em uma linguagem de programação a sua escolha
    # o algoritmo abaixo que verifica se o valor de entrada é, ou
    # não, um número primo. Existe pior e melhor caso?

    def primo(n):
        j = 2
        while j < n and n % j != 0:
            j += 1

        print(n, "é primo.") if j == n else print(n, "não é primo.")

    x = np.linspace(1, valores_ate, valores_ate)
    tempos = []
    for i in x:
        start = perf_counter() * 1000
        primo(i)
        end = perf_counter() * 1000
        tempos.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 2", y=1.05)
    plt.plot(x, tempos)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()

def exercicio_tres(valores_ate):

    # LISTA_PRIMO
    # Implemente em uma linguagem de programação a sua escolha
    # o algoritmo abaixo que lista os números primos menores ou
    # igual ao valor de entrada. Existe pior e melhor caso?

    def lista_primo(n):
        A = []
        x = 1
        for i in range(2, n + 1):
            j = 2
            while j < i and i % j != 0:
                j += 1

            if j == i:
                A.append(i)
                x += 1

    x = np.linspace(1, valores_ate, valores_ate)
    tempos = []
    for k in x:
        start = perf_counter() * 1000
        lista_primo(int(k))
        end = perf_counter() * 1000
        tempos.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 3", y=1.05)
    plt.plot(x, tempos)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()


def exercicio_quatro(valores_ate):

    # Cada um dos algoritmos abaixo recebe um inteiro positivo e
    # devolve outro inteiro positivo. Os dois algoritmos devolvem o
    # mesmo número se receberem o mesmo valor de entrada n?
    # Qual dos dois algoritmos é mais eficiente?

    def soma_quadrados_a(n):
        x = 0
        for j in range(1, n+1):
            x += j * j
        return x

    def soma_quadrados_b(n):
        x = n * (n + 1) * ((2*n) + 1)
        x = int(x / 6)
        return x

    x = np.linspace(1, valores_ate, valores_ate)
    tempos_a = []
    tempos_b = []
    for k in x:
        start = perf_counter() * 1000
        soma_quadrados_a(int(k))
        end = perf_counter() * 1000
        tempos_a.append(end - start)

        start = perf_counter() * 1000
        soma_quadrados_b(int(k))
        end = perf_counter() * 1000
        tempos_b.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 4", y=1.09)
    plt.plot(x, tempos_a, label='Soma Quadrados A')
    plt.plot(x, tempos_b, label='Soma Quadrados B')
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=3, borderaxespad=0)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()


def exercicio_5_insercao(valores_ate):

    def insercao(V):
        for i in range(1, len(V)):
            key = V[i]
            j = i - 1
            while j >= 0 and key < V[j]:
                V[j + 1] = V[j]
                j -= 1
            V[j + 1] = key

    x = np.linspace(1, valores_ate, valores_ate)
    tempos_aleatorio = []
    tempos_ordenado = []
    tempos_inversamente_ordenado = []
    tempos_repetido = []
    for k in x:
        vetor_aleatorio = gerar_vetor_aleatorio(int(k))
        vetor_ordenado = gerar_vetor_ordenado(int(k))
        vetor_inversamente_ordenado = gerar_vetor_inversamente_ordenado(int(k))
        vetor_repetido = gerar_vetor_repetido(int(k))

        start = perf_counter() * 1000
        insercao(vetor_aleatorio)
        end = perf_counter() * 1000
        tempos_aleatorio.append(end - start)

        start = perf_counter() * 1000
        insercao(vetor_ordenado)
        end = perf_counter() * 1000
        tempos_ordenado.append(end - start)

        start = perf_counter() * 1000
        insercao(vetor_inversamente_ordenado)
        end = perf_counter() * 1000
        tempos_inversamente_ordenado.append(end - start)

        start = perf_counter() * 1000
        insercao(vetor_repetido)
        end = perf_counter() * 1000
        tempos_repetido.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 5 - Inserção", y=1.104)
    plt.plot(x, tempos_aleatorio, label='Entrada aleatória')
    plt.plot(x, tempos_ordenado, label='Entrada ordenada', color='yellow')
    plt.plot(x, tempos_inversamente_ordenado, label='Entrada inversamente ordenada', color='green')
    plt.plot(x, tempos_repetido, label='Entrada repetida')
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=2, borderaxespad=0)

    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()


def exercicio_5_selecao(valores_ate):

    def selecao(V):
        for i in range(len(V)):
            min_idx = i
            for j in range(i + 1, len(V)):
                if V[min_idx] > V[j]:
                    min_idx = j

            V[i], V[min_idx] = V[min_idx], V[i]

    x = np.linspace(1, valores_ate, valores_ate)
    tempos_aleatorio = []
    tempos_ordenado = []
    tempos_inversamente_ordenado = []
    tempos_repetido = []
    for k in x:
        vetor_aleatorio = gerar_vetor_aleatorio(int(k))
        vetor_ordenado = gerar_vetor_ordenado(int(k))
        vetor_inversamente_ordenado = gerar_vetor_inversamente_ordenado(int(k))
        vetor_repetido = gerar_vetor_repetido(int(k))

        start = perf_counter() * 1000
        selecao(vetor_aleatorio)
        end = perf_counter() * 1000
        tempos_aleatorio.append(end - start)

        start = perf_counter() * 1000
        selecao(vetor_ordenado)
        end = perf_counter() * 1000
        tempos_ordenado.append(end - start)

        start = perf_counter() * 1000
        selecao(vetor_inversamente_ordenado)
        end = perf_counter() * 1000
        tempos_inversamente_ordenado.append(end - start)

        start = perf_counter() * 1000
        selecao(vetor_repetido)
        end = perf_counter() * 1000
        tempos_repetido.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 5 - Seleção", y=1.104)
    plt.plot(x, tempos_aleatorio, label='Entrada aleatória')
    plt.plot(x, tempos_ordenado, label='Entrada ordenada', color='yellow')
    plt.plot(x, tempos_inversamente_ordenado, label='Entrada inversamente ordenada', color='green')
    plt.plot(x, tempos_repetido, label='Entrada repetida')
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=2, borderaxespad=0)

    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()

def exercicio_5_bubble(valores_ate):

    def bubble(V):
        n = len(V)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if V[j] > V[j + 1]:
                    V[j], V[j + 1] = V[j + 1], V[j]

    x = np.linspace(1, valores_ate, valores_ate)
    tempos_aleatorio = []
    tempos_ordenado = []
    tempos_inversamente_ordenado = []
    tempos_repetido = []
    for k in x:
        vetor_aleatorio = gerar_vetor_aleatorio(int(k))
        vetor_ordenado = gerar_vetor_ordenado(int(k))
        vetor_inversamente_ordenado = gerar_vetor_inversamente_ordenado(int(k))
        vetor_repetido = gerar_vetor_repetido(int(k))

        start = perf_counter() * 1000
        bubble(vetor_aleatorio)
        end = perf_counter() * 1000
        tempos_aleatorio.append(end - start)

        start = perf_counter() * 1000
        bubble(vetor_ordenado)
        end = perf_counter() * 1000
        tempos_ordenado.append(end - start)

        start = perf_counter() * 1000
        bubble(vetor_inversamente_ordenado)
        end = perf_counter() * 1000
        tempos_inversamente_ordenado.append(end - start)

        start = perf_counter() * 1000
        bubble(vetor_repetido)
        end = perf_counter() * 1000
        tempos_repetido.append(end - start)

    plt.figure(figsize=(8, 6))
    plt.title("Exercício 5 - Bubble", y=1.104)
    plt.plot(x, tempos_aleatorio, label='Entrada aleatória')
    plt.plot(x, tempos_ordenado, label='Entrada ordenada', color='yellow')
    plt.plot(x, tempos_inversamente_ordenado, label='Entrada inversamente ordenada', color='green')
    plt.plot(x, tempos_repetido, label='Entrada repetida')
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=2, borderaxespad=0)

    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução (ms)")
    plt.show()

exercicio_um(13)
exercicio_dois(200)
exercicio_tres(20)
exercicio_quatro(200)
exercicio_5_selecao(100)
exercicio_5_insercao(100)
exercicio_5_bubble(100)
