class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def estaVazia(self):
        return self.primeiro is None

    def getTamanho(self):
        return self.tamanho

    def enqueue(self, item):
        novoItem = No(item)
        if (self.estaVazia()):
            self.primeiro = novoItem
        else:
            self.ultimo.setProximo(novoItem)
        self.ultimo = novoItem
        self.tamanho += 1

    def dequeue(self):
        if not self.estaVazia():
            noAux = self.primeiro
            if self.primeiro is self.ultimo:
                self.ultimo = None
            self.primeiro = self.primeiro.getProximo()
            self.tamanho -= 1
            return noAux.getCarga()

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def estaVazia(self):
        return self.topo is None

    def getTamanho(self):
        return self.tamanho

    def peek(self):
        if not self.estaVazia():
            return self.topo.getCarga()

    def pop(self):
        if not self.estaVazia():
            noAux = self.topo
            self.topo = self.topo.getProximo()
            self.tamanho -= 1
            return noAux.getCarga()

    def push(self, item):
        novoItem = No(item, self.topo)
        self.topo = novoItem
        self.tamanho += 1

class ListaEncadeadaSimples:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def addNoInicio(self, carga):
        no = No(carga)
        no.setProximo(self.cabeca)
        self.cabeca = no
        self.tamanho += 1

    def addPorIndice(self, carga, posicao):
        if posicao == 0:
            self.addNoInicio(carga)
        elif posicao - 1 < self.tamanho:
            posicaoAtual = 1
            noAux = self.cabeca.getProximo()
            while (posicaoAtual < posicao - 1):
                noAux = noAux.getProximo()
                posicaoAtual += 1
            noAdicionado = No(carga, noAux.getProximo())
            noAux.setProximo(noAdicionado)
        self.tamanho += 1

    def imprimeLista(self):
        noAux = self.cabeca
        impressao = '[ '
        while (noAux != None):
            impressao += noAux.getCarga() + ' '
            noAux = noAux.getProximo()
        impressao += ']'
        print(impressao)

    def getCabeca(self):
        return self.cabeca

    def getTamanho(self):
        return self.tamanho

    def removePrimeiro(self):
        if (self.cabeca != None):
            self.cabeca = self.cabeca.getProximo()
            self.tamanho -= 1

    def removePorIndice(self, posicao):
        if posicao == 0:
            self.removePrimeiro()
        elif posicao - 1 < self.tamanho:
            posicaoAtual = 1
            noAux = self.cabeca.getProximo()
            while (posicaoAtual < posicao - 1):
                noAux = noAux.getProximo()
                posicaoAtual += 1
            noAux.setProximo(noAux.getProximo().getProximo())
        self.tamanho -= 1

    def busca(self, valor):
        noAux = self.cabeca
        posicao = 0
        while (noAux != None):
            if noAux.getCarga() == valor:
                break
            noAux = noAux.getProximo()
            posicao += 1
        if (noAux == None):
            return None
        return posicao

class No:
    def __init__(self, carga = None, proximo = None):
        self.carga = carga
        self.proximo = proximo

    def getCarga(self):
        return self.carga

    def setCarga(self, novaCarga):
        self.carga = novaCarga

    def getProximo(self):
        return self.proximo

    def setProximo(self, novoProximo):
        self.proximo = novoProximo