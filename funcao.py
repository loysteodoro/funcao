import random

def f(x):
    return x**3 - 6*x + 14

def gerar_individuo():
    return random.uniform(-10, 10)

def criar_populacao(tamanho):
    return [gerar_individuo() for _ in range(tamanho)]

def calcular_fitness(individuos):
    return [f(x) for x in individuos]

def selecionar_pais(populacao, fitness):
    pais = []
    for _ in range(2):
        competidores = random.sample(list(zip(populacao, fitness)), 3)
        pais.append(min(competidores, key=lambda x: x[1])[0])
    return pais

def crossover(pai1, pai2):
    return (pai1 + pai2) / 2

def mutacao(individuo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        return gerar_individuo()
    return individuo

def algoritmo_genetico(tamanho_populacao=10, geracoes=100, taxa_mutacao=0.01):
    populacao = criar_populacao(tamanho_populacao)

    for _ in range(geracoes):
        fitness = calcular_fitness(populacao)
        nova_populacao = []

        while len(nova_populacao) < tamanho_populacao:
            pais = selecionar_pais(populacao, fitness)
            filho = crossover(pais[0], pais[1])
            filho = mutacao(filho, taxa_mutacao)
            nova_populacao.append(filho)

        populacao = nova_populacao

    fitness = calcular_fitness(populacao)
    melhor_individuo = min(zip(populacao, fitness), key=lambda x: x[1])

    print(f'O valor de x que minimiza a função é: {melhor_individuo[0]}, com f(x) = {melhor_individuo[1]}.')

if __name__ == "__main__":
    algoritmo_genetico()
