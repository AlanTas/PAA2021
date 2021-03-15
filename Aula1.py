import datetime
from time import perf_counter_ns
from time import perf_counter
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")
import numpy as np


def exercicio_um():
    # Qual é o menor valor de entrada n (considere n > 0) tal que
    # um algoritmo cujo tempo de execução é 10n^2 é mais rápido
    # que um algoritmo cujo tempo de execução é 2^n?
    # Qual desses algoritmos você considera mais eficiente?

    func_quadratica = []
    func_exponencial = []
    numero_entradas = 13
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


def exercicio_dois():
    # Implemente em uma linguagem de programação a sua escolha
    # o algoritmo abaixo que verifica se o valor de entrada é, ou
    # não, um número primo. Existe pior e melhor caso?

    def primo(n):
        j = 2
        while j < n and n % j != 0:
            j += 1

        print(n, "é primo.") if j == n else print(n, "não é primo.")

    valores_ate = 200
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

def exercicio_tres():

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

    valores_ate = 20
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


def exercicio_quatro():

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

    valores_ate = 200
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


def exercicio_5(n):

    def insercao(V):
        for i in range(1, len(V)):
            key = V[i]
            j = i - 1
            while j >= 0 and key < V[j]:
                V[j + 1] = V[j]
                j -= 1
            V[j + 1] = key




# exercicio_um()
# exercicio_dois()
# exercicio_tres()
exercicio_quatro()
