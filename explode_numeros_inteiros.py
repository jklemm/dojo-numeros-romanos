class ExplodeNumerosInteiros(object):

    def __init__(self):
        self.pares = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

    def explodir(self, valor):
        valor_texto = str(valor)
        par = unidade = 0
        for (indice, numero) in enumerate(reversed(valor_texto), start=1):
            self.pares[par][unidade] = numero
            unidade = unidade + 1 if indice % 3 != 0 else 0
            par += 1 if indice % 3 == 0 else 0
