class stack:
    _array_ = []                          #pilha
    _arraybackup_ = []                    #copia da pilha

    def input(a):                         #adiciona termos no topo da pilha
        stack._array_.append(a)
        stack._arraybackup_.append(a)

    def top():                            #retorna o valor do topo e desempilha
        if stack.isempty() == False:
            _aux = stack._array_[-1]
            stack._array_.pop()
            return _aux
        print("Erro: pilha vazia")

    def get():                            #retorna o valor do topo sem desempilhar
        if stack.isempty() == False:
            return stack._array_[-1]
        print("Erro: pilha vazia")

    def isempty():                        #retorna True se a pilha estiver vazia
        if stack.length() == 0:
            return True
        return False

    def length():                         #retorna o numero de itens empilhados
        return len(stack._array_)

    def ispalindrome():                   #retorna True se a palavra for um palindromo
        _aux = []

        for d in range(stack.length()):
            _aux.append(stack.top())

        if _aux == stack._arraybackup_:
            return True
        return False

if __name__ == '__main__':
    _word_ = input()                 #recebe a entrada do usuário

    for i in(_word_):                #empilha a palavra
        if i != " ":
            stack.input(i)

    if stack.ispalindrome():         #testa se a palavra é palíndroma e exibe o resultado 
        print("sim")
    else:
        print("nao")

