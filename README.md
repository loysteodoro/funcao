Este projeto implementa um algoritmo genético para encontrar o valor de ( x ) que minimiza a função ( f(x) = x^3 - 6x + 14 ) na faixa de [-10, 10].

Estrutura do Projeto
src/
funcao.py: Implementação do algoritmo genético.
utils.py: Funções auxiliares (não utilizadas neste exemplo, mas podem ser expandidas).
Configurações do Algoritmo
Tamanho da população : Configurável (padrão: 10).
Taxa de mutação : Configurável (padrão: 1%).
Pontos de crossover : 1 ou 2 (configuráveis).
Método de seleção : Torneio (ou pode ser inovador roleta vicada).
Elitismo : Configurável, com percentual de indivíduos a serem mantidos.
Critério de parada : Número máximo de gerações (configurável).
Como Executar
Clonar este repositório.
Navegue até a pasta do projeto.
Execute o script principal:
python src/funcao.py