from busca import busca_linear, busca_binaria
from random import shuffle

def carregar_arquivo():
  with open('dicionario.txt') as f:
    list = f.readlines()
  list = [x.rstrip('\n') for x in list]
  return list

chaves = carregar_arquivo()
shuffle(chaves)

def _busca_linear(lista, numero_de_palavras):
  for i in range(numero_de_palavras):
    chave = chaves[i]
    busca_linear(lista, chave)

def _busca_binaria(lista, numero_de_palavras):
  for i in range(numero_de_palavras):
    chave = chaves[i]
    busca_binaria(lista, chave)