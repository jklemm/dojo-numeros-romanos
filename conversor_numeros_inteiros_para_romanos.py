from explode_numeros_inteiros import ExplodeNumerosInteiros


class ConversorDeNumerosInteirosParaRomanos(object):
    UM = 'I'
    CINCO = 'V'
    DEZ = 'X'
    CINQUENTA = 'L'
    CEM = 'C'
    QUINHENTOS = 'D'
    MIL = 'M'

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

        retorno = self._converte_milhar(milhar)
        retorno += self._converte_centena(centena)
        retorno += self._converte_dezena(dezena)
        retorno += self._converte_unidade(unidade)
        return retorno

    def _converte_unidade(self, unidade):
        if unidade == 0:
            return ''
        elif unidade in (1, 2, 3):
            return self.UM * unidade
        elif unidade in (4, 5):
            vezes = 5 - unidade
            return self.UM * vezes + self.CINCO
        elif unidade in (6, 7, 8):
            vezes = unidade - 5
            return self.CINCO + self.UM * vezes
        elif unidade == 9:
            return self.UM + self.DEZ

    def _converte_dezena(self, dezena):
        if dezena == 0:
            return ''
        elif dezena in (1, 2, 3):
            return self.DEZ * dezena
        elif dezena in (4, 5):
            vezes = 5 - dezena
            return self.DEZ * vezes + self.CINQUENTA
        elif dezena in (6, 7, 8):
            vezes = dezena - 5
            return self.CINQUENTA + self.DEZ * vezes
        elif dezena == 9:
            return self.DEZ + self.CEM

    def _converte_centena(self, centena):
        if centena == 0:
            return ''
        elif centena in (1, 2, 3):
            return self.CEM * centena
        elif centena in (4, 5):
            vezes = 5 - centena
            return self.CEM * vezes + self.QUINHENTOS
        elif centena in (6, 7, 8):
            vezes = centena - 5
            return self.QUINHENTOS + self.CEM * vezes
        elif centena == 9:
            return self.CEM + self.MIL

    def _converte_milhar(self, milhar):
        if milhar == 0:
            return ''
        elif milhar in (1, 2, 3):
            return self.MIL * milhar
        elif milhar in (4, 5):
            vezes = 5 - milhar
            return '_' + self.UM * vezes + self.CINCO
        elif milhar in (6, 7, 8):
            vezes = milhar - 5
            return '_' + self.CINCO + self.UM * vezes
        elif milhar == 9:
            return '_' + self.UM + self.DEZ
