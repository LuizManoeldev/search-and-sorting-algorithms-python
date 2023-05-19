from functions import carregar_arquivo, _busca_binaria, _busca_linear
from algoritmos import mergeSort, quickSort, insertionSort, bubbleSort
import time


if __name__ == '__main__':

  searchtest_list = carregar_arquivo()
  bubblesort_list = carregar_arquivo()
  insertionsort_list = carregar_arquivo()
  quicksort_list = carregar_arquivo()
  mergesort_list = carregar_arquivo()

  
  #Testes propostos pelo professor:

  # Para realizar o teste, descomente o algoritmo de busca a ser testado.
  # Funções auxiliares utilizadas, que recebem a lista e o numero de palavras a serem buscadas.
  ini = time.time()
  
  # Ordenação
  #bubbleSort(bubblesort_list)
  #insertionSort(insertionsort_list)
  #quickSort(quicksort_list)
  #mergeSort(mergesort_list)
  
  # Busca
  #_busca_linear(searchtest_list,1000)
  #_busca_binaria(mergesort_list, 1000)
  #_busca_linear(mergeSort_list, 1000)
  
  fim = time.time()
  tempo_execucao = round(fim-ini,2)
  
  print(f'Tempo de execução = {tempo_execucao}')
