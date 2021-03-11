import matplotlib.pyplot as plt
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
    plt.plot(y, func_quadratica, 'co', label="10n^2")
    plt.plot(y, func_exponencial, 'go', label="2^n")
    plt.plot(y[menor_valor - 1], func_quadratica[menor_valor - 1] , 'rx', label="Menor valor que 10n^2 é mais eficiente")
    plt.legend(bbox_to_anchor=(0., 1.01, 1., .10), loc='center',
               ncol=3, borderaxespad=0)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo de execução")
    plt.show()


exercicio_um()
