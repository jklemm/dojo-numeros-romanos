from explode_numeros_inteiros import ExplodeNumerosInteiros


class ConversorDeNumerosInteirosParaRomanos(object):
    UM = 'I'
    CINCO = 'V'
    DEZ = 'X'
    CINQUENTA = 'L'
    CEM = 'C'
    QUINHENTOS = 'D'
    MIL = 'M'
    UM_MIL = 'Ī'
    CINCO_MIL = 'V̄'
    DEZ_MIL = 'X̄'

    def __init__(self):
        self.explode = ExplodeNumerosInteiros()
        self.valor = 0

    def converter(self, valor):
        self.valor = valor
        self.explode.explodir(self.valor)

        unidade = int(self.explode.pares[0][0])
        dezena = int(self.explode.pares[0][1])
        centena = int(self.explode.pares[0][2])
        milhar = int(self.explode.pares[1][0])

        retorno = self._converte_milhares(milhar, self.MIL)
        retorno += self._converte_tres_numeros(centena, self.CEM, self.QUINHENTOS, self.MIL)
        retorno += self._converte_tres_numeros(dezena, self.DEZ, self.CINQUENTA, self.CEM)
        retorno += self._converte_tres_numeros(unidade, self.UM, self.CINCO, self.DEZ)
        return retorno

    def _converte_tres_numeros(self, valor, menor, meio, maior):
        if valor == 0:
            return ''
        elif valor in (1, 2, 3):
            return menor * valor
        elif valor in (4, 5):
            vezes = 5 - valor
            return menor * vezes + meio
        elif valor in (6, 7, 8):
            vezes = valor - 5
            return meio + menor * vezes
        elif valor == 9:
            return menor + maior

    def _converte_milhares(self, valor, menor):
        if valor == 0:
            return ''
        elif valor in (1, 2, 3):
            return menor * valor
        else:
            return self._converte_tres_numeros(valor, self.UM_MIL, self.CINCO_MIL, self.DEZ_MIL)
