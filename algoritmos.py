from typing import List

def mergeSort(array:List[int]):
    #print(array)
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Chamada recursiva para cada metade do array
        mergeSort(right)
        mergeSort(left)

        # Aqui é iniciado o processo de merge dos vetores

        # iteradores para percurso das duas metades
        i = 0 # iterador para a metade esquerda
        j = 0 # iterador para a metade direita
        
        # iterador para o array principal
        k = 0
        
        # Comparando os elementos da metade da esquerda e da direita
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # O valor da metade esquerda é ordenado
              array[k] = left[i]
              # Avança o iterador da metade esquerda
              i += 1
            else:
                # o valor da metade direita é ordenado
                array[k] = right[j]
                # Avança o iterador da metade direita
                j += 1
            # Avança para o próximo slot do array principal
            k += 1

        # Os valores remanescentes, da metade esquerda, são copiados
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Os valores remanescentes, da metade direita, são copiados
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

######################################################################################################################################################


def quickSort(array):
    quickSortRun(array,0,len(array)-1)


# Função que realiza todo o processo de posicionamento do pivô e 
# particionamento das unidades do array. Retorna o índice correspondente
# ao posicionamento do pivô no array ordenado
#
# array[] --> Array a ser ordenado
# low  --> índice do primeiro elemento do array
# high  --> índice do último elemento do array
def partition(array,low,high):
    pivot = array[low] # pivot
   
    # indice que sobe de forma crescente 
    a = low + 1
    # indice que desce de forma decrescente 
    b = high

    while(True):
        # Deslocando o indice para a direita
        while( a <= high  and array[a] <= pivot ):
            a+=1

        # Deslocando o indice do final para a esquerda
        while( array[b] > pivot):
            b-=1

        # Se o indice "a" for menor que "b", realizamos a troca
        if ( a < b ):
            array[a],array[b] = array[b],array[a]
            a+=1
            b-=1
			
        # se a cruzar com b, sai do laço
        if( a > b):
            break
    # Ja foi encontrado o lugar do pivo. Agora vamos troca-lo com o elemento
    # que se encontra no indice 
    array[low] = array[b]
    array[b] = pivot

    return ( b )   

# função recursiva que aciona o particionamento e chamadas recursivas das
# subdivisões do array
def quickSortRun(array,low,high): 
    if low < high:  
        # pi é o índice de particionamento 
        pi = partition(array,low,high) 
  
        # Separadamente, os elementos antes e depois e antes da
        # partição são ordenados
        quickSortRun(array, low, pi-1) 
        quickSortRun(array, pi+1, high)


######################################################################################################################################################

def insertionSort(array):
    # percorre o array
    # O laço começa do índice 1, pois o índice 0 é o início
    # do subconjunto ordenado
    for i in range(1, len(array)):
        # chave do subarray desordenado        
        key = array[i]
            
        # Move os elementos de array[0.. i-1] que são maiores
        # do que a chave, para uma posicao à frente de sua
        # posição atual

        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key


######################################################################################################################################################


def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if (array[j] > array[j+1] ):
                array[j],array[j+1] = array[j+1],array[j] # Efetua a troca