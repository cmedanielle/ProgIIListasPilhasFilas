from tads import Pilha

pilha = Pilha()
pilha.push("abacaxi")
pilha.push('banana')
pilha.push('caju')
pilha.push('damasco')
pilha.push('embira')

print('Topo da pilha: {}'.format(pilha.peek()))

while not pilha.estaVazia():
    print('Removendo o topo de valor {}'.format(pilha.pop()))
    print('Topo da pilha: {}'.format(pilha.peek()))
