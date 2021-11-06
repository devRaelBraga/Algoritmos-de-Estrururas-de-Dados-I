# importações

import pandas as pd  # para ler o arquivo csv
import matplotlib.pyplot as plt  # para plotar o gráfico


class Node:  # Criação da classe nó
    def __init__(self, data):
        self.data = data
        self.next = None


class Hash:  # criação da classe Hash
    def __init__(self, size):
        self.tabela = [None] * size
        self.tam = size
        self.colisoes = 0

    def fhash(self,
              dado):  # função hashing principal da Função C, determina uma área da tabela para uso conjunto de 2 letras, foi verificado quantas vezes
        tam = self.tam - 53338 - 1500  # aparece cada letra no início da palavra, junta-se uma letra que aparece muito e uma que aparece pouco
        tam = tam // 13  # e então, executa-se uma função hashing básica e adiciona o elemento na posição retornada

        if dado[0] == "c" or dado[0] == "x":
            som = 5337 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return ret

        elif dado[0] == "p" or dado[0] == "y":
            som = 5152 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 5337 + tam + ret

        elif dado[0] == "a" or dado[0] == "z":
            som = 5041 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 5337 + 5152 + tam * 2 + ret

        elif dado[0] == "m" or dado[0] == "w":
            som = 4363 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 5041 + 5152 + 5337 + tam * 3 + ret

        elif dado[0] == "s" or dado[0] == "k":
            som = 4392 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 4363 + 5041 + 5152 + 5337 + tam * 4 + ret

        elif dado[0] == "u" or dado[0] == "d":
            som = 4126 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 4392 + 4363 + 5041 + 5152 + 5337 + tam * 5 + ret

        elif dado[0] == "q" or dado[0] == "e":
            som = 3755 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 6 + ret

        elif dado[0] == "i" or dado[0] == "j":
            som = 3433 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 7 + ret

        elif dado[0] == "h" or dado[0] == "b":
            som = 3790 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 8 + ret

        elif dado[0] == "r" or dado[0] == "o":
            som = 3681 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return + 3790 + 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 9 + ret

        elif dado[0] == "n" or dado[0] == "f":
            som = 3479 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 3681 + 3790 + 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 10 + ret

        elif dado[0] == "t" or dado[0] == "v":
            som = 3457 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 3479 + 3681 + 3790 + 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 11 + ret

        elif dado[0] == "l" or dado[0] == "g":
            som = 3332 + tam
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % som)
            return 3457 + 3479 + 3681 + 3790 + 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 12 + ret

        else:
            sum = ""
            dado = str(dado)
            for c in range(0, len(dado)):
                sum += str(ord(dado[c]))
            ret = int(int(sum) % 1500)
            return 3332 + 3457 + 3479 + 3681 + 3790 + 3433 + 3755 + 4126 + 4392 + 4363 + 5041 + 5152 + 5337 + tam * 13 + ret

    def mostrar(self, indice):
        pointer = self.tabela[indice]
        if pointer:
            print(pointer.data, end="")
            while pointer.next:
                pointer = pointer.next
                print(" ", pointer.data, end="")

    def insert(self, dado):  # metodo de insert da função C
        no = Node(dado)
        hash = self.fhash(dado)

        try:
            if self.tabela[hash] == None:  # teste para ver se a posição está ocupada
                self.tabela[hash] = no

            else:
                hash = hash + self.fhash(
                    dado)  # se houve colisão, executa a função hash para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no

        except IndexError:
            hash = hash - self.tam - 1

            if self.tabela[hash] == None:  # teste para ver se a posição está ocupada
                self.tabela[hash] = no

            else:
                hash = hash + self.fhash(
                    dado)  # se houve colisão, executa a função hash para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no

    def f2hash(self, dado):  # função auxiliar para "hashing duplo"
        multi = 1
        dado = str(dado)
        for c in range(0, len(dado)):
            multi = ord(dado[c])
        ret = int(((multi ** 7) / len(dado)) % self.tam)
        return ret

    def f2hash2(self, dado):  # função auxiliar para "hashing duplo" e para casos de colisão
        sum = 0
        sum2 = 0
        for c in range(0, int(len(dado) / 2)):
            sum += ord(dado[c])
        for d in range(int(len(dado) / 2), len(dado)):
            sum2 += ord(dado[d])
        ret = int((sum * sum2))
        return ret

    def f2hash3(self, dado):  # função principal de uso "hashing duplo"
        has1 = self.f2hash(dado)
        ret = has1 + 3 * self.f2hash2(dado)
        ret = int((ret) * 147331 % self.tam)
        return ret

    def insert2(self, dado):  # metodo de insert da função B
        no = Node(dado)
        hash = self.f2hash3(dado)

        try:
            if self.tabela[hash] == None:  # vê se a posição está vazia
                self.tabela[hash] = no

            else:
                hash = hash + self.f2hash(
                    dado)  # se houve colisão, executa a função hash2 para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no

        except IndexError:  # tratamento de erro de indice, seguindo a lista a partir do inicio
            hash = hash - self.tam - 1

            if self.tabela[hash] == None:  # vê se a posição está vazia
                self.tabela[hash] = no

            else:
                hash = hash + self.f2hash(
                    dado)  # se houve colisão, executa a função hash2 para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no

    def f1hash(self,
               dado):  # Função de hashing principal, transforma as letras em strings, concatenando-as e transformando em inteiro novamente, multiplicando por um numero primo grande
        sum = ""
        dado = str(dado)
        for c in range(0, len(dado)):
            sum += str(ord(dado[c]))
        ret = int(int(sum) * 147331 % self.tam)
        return ret

    def f1hash2(self, dado):  # função secundária pro uso de "hashing duplo"
        sum = 0
        sum2 = 0
        for c in range(0, int(len(dado) / 2)):
            sum += ord(dado[c])
        for d in range(int(len(dado) / 2), len(dado)):
            sum2 += ord(dado[d])
        ret = int((sum * sum2))
        return ret

    def f1hash3(self, dado):  # função de "hashing duplo", para o caso de haver colisões
        has1 = self.f1hash(dado)
        ret = has1 + 147331 * self.f1hash2(dado)
        ret = int((ret) * 147331 % self.tam)
        return ret

    def insert1(self, dado):  # metodo de insert da Função A
        no = Node(dado)
        hash = self.f1hash(dado)

        try:
            if self.tabela[hash] == None:  # vê se a posição está vazia
                self.tabela[hash] = no

            else:
                hash = hash + self.f1hash3(
                    dado)  # se houve colisão, executa a função hash3 para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no

        except IndexError:  # Tratamento para erro de indice, seguindo a lista a partir do começo
            hash = hash - self.tam - 1

            if self.tabela[hash] == None:  # vê se a posição está vazia
                self.tabela[hash] = no

            else:
                hash = hash + self.f1hash3(
                    dado)  # se houve colisão, executa a função hash3 para determinar o tamanho do "pulo"
                if hash > self.tam:
                    hash = hash - self.tam - 1
                elif hash == self.tam:
                    hash = hash - self.tam
                pointer = self.tabela[hash]
                if pointer != None:
                    self.colisoes += 1
                if pointer != None:
                    while pointer.next:
                        pointer = pointer.next
                    pointer.next = no
                else:
                    self.tabela[hash] = no


# criação das tabelas Hashs, Função A com 5 tabelas, uma para cada tamanho. Etc.
a1 = Hash(333337)
a2 = Hash(78139)
a3 = Hash(74149)
a4 = Hash(65717)
a5 = Hash(62137)

b1 = Hash(333337)
b2 = Hash(78139)
b3 = Hash(74149)
b4 = Hash(65717)
b5 = Hash(62137)

c1 = Hash(333337)
c2 = Hash(78139)
c3 = Hash(74149)
c4 = Hash(65717)
c5 = Hash(62137)

path = 'lexicons-webmedia21.csv'
df = pd.read_csv(path)
df.head()

# inserindo os dados, uma tabela Hash para cada combinação de Função e Tamanho.
for i in range(0, 54382):
    a1.insert1(str(df.loc[i, 'term']))
    a2.insert1(str(df.loc[i, 'term']))
    a3.insert1(str(df.loc[i, 'term']))
    a4.insert1(str(df.loc[i, 'term']))
    a5.insert1(str(df.loc[i, 'term']))

    b1.insert2(str(df.loc[i, 'term']))
    b2.insert2(str(df.loc[i, 'term']))
    b3.insert2(str(df.loc[i, 'term']))
    b4.insert2(str(df.loc[i, 'term']))
    b5.insert2(str(df.loc[i, 'term']))

    c1.insert(str(df.loc[i, 'term']))
    c2.insert(str(df.loc[i, 'term']))
    c3.insert(str(df.loc[i, 'term']))
    c4.insert(str(df.loc[i, 'term']))
    c5.insert(str(df.loc[i, 'term']))

# Criação da Tabela
print("\033[1mTamanho\t\tFunção\t\tResultado\033[0m")
print(" 333337\t\t  A\t\t   ", a5.colisoes)
print("  78139\t\t  A\t\t  ", a4.colisoes)
print("  74149\t\t  A\t\t  ", a3.colisoes)
print("  65717\t\t  A\t\t  ", a2.colisoes)
print("  62137\t\t  A\t\t ", a1.colisoes)

print(" 333337\t\t  B\t\t  ", b5.colisoes)
print("  78139\t\t  B\t\t ", b4.colisoes)
print("  74149\t\t  B\t\t ", b3.colisoes)
print("  65717\t\t  B\t\t ", b2.colisoes)
print("  62137\t\t  B\t\t ", b1.colisoes)

print(" 333337\t\t  C\t\t  ", c5.colisoes)
print("  78139\t\t  C\t\t ", c4.colisoes)
print("  74149\t\t  C\t\t ", c3.colisoes)
print("  65717\t\t  C\t\t ", c2.colisoes)
print("  62137\t\t  C\t\t ", c1.colisoes)

print("\t   Tabela 1. Resultados\n")

# Criação do Gráfico usando MatplotLib
tamanhos = ["Tamanho 1", "Tamanho 2", "Tamanho 3", "Tamanho 4", "Tamanho 5"]
colisoes1 = [a5.colisoes, a4.colisoes, a3.colisoes, a2.colisoes, a1.colisoes]
colisoes2 = [b5.colisoes, b4.colisoes, b3.colisoes, b2.colisoes, b1.colisoes]
colisoes3 = [c5.colisoes, c4.colisoes, c3.colisoes, c4.colisoes, c1.colisoes]

plt.plot(tamanhos, colisoes1, 'b', marker='o')
plt.plot(tamanhos, colisoes2, 'r', marker='o')
plt.plot(tamanhos, colisoes3, 'g', marker='o')

plt.ylabel('Número de colisões')
plt.title("Colisões")
plt.legend(["Função A", "Função B", "Função C"], loc=3)
plt.show()
