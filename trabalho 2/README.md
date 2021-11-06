### 1 Problema

Uma lista ligada possui um ciclo se algum nó (valor)  ́e visitado mais do que uma vez enquanto se
percorre a lista. Dado um ponteiro para o head de uma lista ligada, escreva um programa em
Python para testar se a lista possui um ciclo. Se houver um ciclo, o programa deverá retornar 1.
Caso contrário, deverá retornar 0.

### 2 Exemplos
A lista L1 = 1 → 2 → 3 → null não tem ciclos. Portanto, o programa deverá retornar 0.
A lista L2 = 1 → 2 → 3 → 1 → null tem um ciclo, pois o nó 3 tem um valor anterior (1) da lista.
Portanto, o programa dever ́a retornar 1.

### 3 Descrição da função

O programa dever ́a ter, obrigatoriamente, uma fun ̧c ̃ao de nome testaCiclo (head) que receber ́a
o ponteiro para o primeiro elemento da lista e retornar o valor 1 (h ́a ciclo) ou 0 (n ̃ao h ́a ciclo).
N ̃ao  ́e permitido o uso de arrays e nem o tipo List de Python.

### 4 Entrada e Sa ́ıda de Dados
O arquivo de entrada estará no formato texto e terá uma sequência de valores numéricos. A saída
dever ́a ser 1 ou 0. O primeiro valor informa o número de elementos da lista. A Tabela 1 mostra
possíveis exemplos de entrada e saída de dados:

entrada   | saída
:---------: | :------:
3 | --
1 | --
2 | --
3 | 0
-- | --
4 | --
1 | --
2 | --
3 | --
1 | 1

Tabela 1: Exemplos.
