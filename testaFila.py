from tads import Fila

fila = Fila()
fila.enqueue("abacaxi")
fila.enqueue('banana')
fila.enqueue('caju')
fila.enqueue('damasco')
fila.enqueue('embira')

print('Tamanho da fila: {}'.format(fila.getTamanho()))

while not fila.estaVazia():
    print('Chamando o próximo, de valor {}'.format(fila.dequeue()))
    print('Restam {} na fila'.format(fila.getTamanho()))
