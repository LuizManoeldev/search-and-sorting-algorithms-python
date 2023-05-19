#Código do Professor
NAO_ENCONTRADO = -1

class Resultado:

    def __init__(self, indice=NAO_ENCONTRADO, numero_operacoes=0):
        self.indice = indice
        self.numero_operacoes = numero_operacoes

    @property
    def existe(self):
        return self.indice != NAO_ENCONTRADO

    def incr(self):
        self.numero_operacoes += 1


def busca_linear(array: list, chave: int) -> Resultado:
    resultado = Resultado()
    for indice, elemento in enumerate(array):
        resultado.incr()
        if elemento == chave:
            resultado.indice = indice
            return resultado

    return resultado

def busca_linear_ordenada(array: list, chave: int) -> Resultado:
    resultado = Resultado()
    for indice, elemento in enumerate(array):
        resultado.incr()
        if elemento == chave:
            resultado.indice = indice
            return resultado
        elif chave < elemento:
            return resultado

    return resultado


def busca_binaria(array: list, chave: int) -> Resultado:
    inicio = 0
    fim = len(array) - 1
    resultado = Resultado()

    while inicio <= fim:
        resultado.incr()
        meio = (inicio + fim)// 2
        if chave < array[meio]:
            fim = meio - 1
        elif chave > array[meio]:
            inicio = meio + 1
        else:
            resultado.indice = meio
            return resultado

    return resultado



'''
if __name__ == "__main__":
    v1 = [ 100, 50, 32, 45, 12]
    v2 = [12, 32, 45, 50, 100]

    resposta = busca_linear(v1, 32)
    assert resposta.indice == 2
    assert resposta.existe is True
    resposta = busca_linear(v1, 200)
    assert resposta.existe is False
    resposta = busca_linear(v2, 32)
    assert resposta.existe is True
    assert resposta.indice == 1
    resposta = busca_linear(v2, 170)
    assert resposta.existe is False

    resposta = busca_linear_ordenada(v2, 45)
    assert resposta.existe is True
    assert resposta.indice == 2

    resposta = busca_linear_ordenada(v2, 5)
    assert resposta.existe is False
    assert resposta.numero_operacoes == 1

    resposta = busca_linear_ordenada(v2, 500)
    assert resposta.existe is False
    assert resposta.numero_operacoes == len(v2)


    v3 = list(range(1000))

    resposta = busca_linear_ordenada(v3, 477)
    assert resposta.existe is True
    assert resposta.numero_operacoes == 478

    resposta = busca_binaria(v3, 477)
    assert resposta.existe is True
    print(resposta.numero_operacoes)
'''