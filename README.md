# funcao# Algoritmo Genético para Minimização de Função

Este projeto implementa um algoritmo genético para encontrar o valor de \( x \) que minimiza a função \( f(x) = x^3 - 6x + 14 \) na faixa de [-10, 10].

## Estrutura do Projeto

- `src/`
  - `funcao.py`: Implementação do algoritmo genético.
  - `utils.py`: Funções auxiliares (não utilizado neste exemplo, mas pode ser expandido).

## Configurações do Algoritmo

- **Tamanho da população**: Configurável (padrão: 10).
- **Taxa de mutação**: Configurável (padrão: 1%).
- **Pontos de crossover**: 1 ou 2 (configurável).
- **Método de seleção**: Torneio (ou pode ser implementada roleta viciada).
- **Elitismo**: Configurável, com percentual de indivíduos a serem mantidos.
- **Critério de parada**: Número máximo de gerações (configurável).

## Como Executar

1. Clone este repositório.
2. Navegue até a pasta do projeto.
3. Execute o script principal:
   ```bash
   python src/funcao.py

