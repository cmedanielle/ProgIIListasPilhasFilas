from tads import ListaEncadeadaSimples

lista = ListaEncadeadaSimples()
lista.addNoInicio('abacaxi')
lista.addNoInicio('banana')
lista.addNoInicio('caju')
lista.addNoInicio('damasco')
lista.addNoInicio('embira')

lista.imprimeLista()
print("Tamanho da lista: {}".format(lista.getTamanho()))

lista.removePrimeiro()
lista.imprimeLista()
print("Tamanho da lista: {}".format(lista.getTamanho()))

print('Índice do elemento Caju: {}'.format(lista.busca('caju')))
print('Índice do elemento Framboesa: {}'.format(lista.busca('framboesa')))

lista.addPorIndice('framboesa',2)
lista.imprimeLista()
print("Tamanho da lista: {}".format(lista.getTamanho()))

lista.removePorIndice(4)
lista.imprimeLista()
print("Tamanho da lista: {}".format(lista.getTamanho()))
