# coding=utf-8
from unittest.case import TestCase


class ExplodeNumerosInteiros(object):

    def __init__(self):
        self.pares = [['0', '0', '0'] for i in range(0, 5)]

    def explodir(self, valor):
        valor_texto = str(valor)
        par = unidade = 0
        for (indice, numero) in enumerate(reversed(valor_texto), start=1):
            #  print par, unidade, indice, numero
            self.pares[par][unidade] = numero
            unidade = unidade + 1 if indice % 3 != 0 else 0
            par += 1 if indice % 3 == 0 else 0


class ExplodeNumerosInteirosTests(TestCase):

    def setUp(self):
        self.explode_inteiros = ExplodeNumerosInteiros()

    def test_unidade(self):
        self.explode_inteiros.explodir(1)
        self.assertEquals('1', self.explode_inteiros.pares[0][0])

    def test_dezena(self):
        self.explode_inteiros.explodir(12)
        self.assertEquals('2', self.explode_inteiros.pares[0][0])
        self.assertEquals('1', self.explode_inteiros.pares[0][1])

    def test_centena(self):
        self.explode_inteiros.explodir(123)
        self.assertEquals('3', self.explode_inteiros.pares[0][0])
        self.assertEquals('2', self.explode_inteiros.pares[0][1])
        self.assertEquals('1', self.explode_inteiros.pares[0][2])

    def test_milhar(self):
        self.explode_inteiros.explodir(123456)
        self.assertEquals('6', self.explode_inteiros.pares[0][0])
        self.assertEquals('5', self.explode_inteiros.pares[0][1])
        self.assertEquals('4', self.explode_inteiros.pares[0][2])
        self.assertEquals('3', self.explode_inteiros.pares[1][0])
        self.assertEquals('2', self.explode_inteiros.pares[1][1])
        self.assertEquals('1', self.explode_inteiros.pares[1][2])

    def test_milhao(self):
        self.explode_inteiros.explodir(123456789)
        self.assertEquals('9', self.explode_inteiros.pares[0][0])
        self.assertEquals('8', self.explode_inteiros.pares[0][1])
        self.assertEquals('7', self.explode_inteiros.pares[0][2])
        self.assertEquals('6', self.explode_inteiros.pares[1][0])
        self.assertEquals('5', self.explode_inteiros.pares[1][1])
        self.assertEquals('4', self.explode_inteiros.pares[1][2])
        self.assertEquals('3', self.explode_inteiros.pares[2][0])
        self.assertEquals('2', self.explode_inteiros.pares[2][1])
        self.assertEquals('1', self.explode_inteiros.pares[2][2])

    def test_bilhao(self):
        self.explode_inteiros.explodir(123456789012)
        self.assertEquals('2', self.explode_inteiros.pares[0][0])
        self.assertEquals('1', self.explode_inteiros.pares[0][1])
        self.assertEquals('0', self.explode_inteiros.pares[0][2])
        self.assertEquals('9', self.explode_inteiros.pares[1][0])
        self.assertEquals('8', self.explode_inteiros.pares[1][1])
        self.assertEquals('7', self.explode_inteiros.pares[1][2])
        self.assertEquals('6', self.explode_inteiros.pares[2][0])
        self.assertEquals('5', self.explode_inteiros.pares[2][1])
        self.assertEquals('4', self.explode_inteiros.pares[2][2])
        self.assertEquals('3', self.explode_inteiros.pares[3][0])
        self.assertEquals('2', self.explode_inteiros.pares[3][1])
        self.assertEquals('1', self.explode_inteiros.pares[3][2])


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

        retorno = self._converte_centena(centena)
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


class NumerosRomanosTests(TestCase):

    def setUp(self):
        self.conversor = ConversorDeNumerosInteirosParaRomanos()

    def test_todas_as_unidades(self):
        self.assertEquals('I', self.conversor.converter(1))
        self.assertEquals('II', self.conversor.converter(2))
        self.assertEquals('III', self.conversor.converter(3))
        self.assertEquals('IV', self.conversor.converter(4))
        self.assertEquals('V', self.conversor.converter(5))
        self.assertEquals('VI', self.conversor.converter(6))
        self.assertEquals('VII', self.conversor.converter(7))
        self.assertEquals('VIII', self.conversor.converter(8))
        self.assertEquals('IX', self.conversor.converter(9))

    def test_todas_as_dezenas(self):
        self.assertEquals('X', self.conversor.converter(10))
        self.assertEquals('XX', self.conversor.converter(20))
        self.assertEquals('XXX', self.conversor.converter(30))
        self.assertEquals('XL', self.conversor.converter(40))
        self.assertEquals('L', self.conversor.converter(50))
        self.assertEquals('LX', self.conversor.converter(60))
        self.assertEquals('LXX', self.conversor.converter(70))
        self.assertEquals('LXXX', self.conversor.converter(80))
        self.assertEquals('XC', self.conversor.converter(90))

    def test_todas_as_centenas(self):
        self.assertEquals('C', self.conversor.converter(100))
        self.assertEquals('CC', self.conversor.converter(200))
        self.assertEquals('CCC', self.conversor.converter(300))
        self.assertEquals('CD', self.conversor.converter(400))
        self.assertEquals('D', self.conversor.converter(500))
        self.assertEquals('DC', self.conversor.converter(600))
        self.assertEquals('DCC', self.conversor.converter(700))
        self.assertEquals('DCCC', self.conversor.converter(800))
        self.assertEquals('CM', self.conversor.converter(900))

    def test_todos_misturados(self):
        self.assertEquals('III', self.conversor.converter(3))
        self.assertEquals('VIII', self.conversor.converter(8))
        self.assertEquals('XIII', self.conversor.converter(13))
        self.assertEquals('XIX', self.conversor.converter(19))
        self.assertEquals('XXIII', self.conversor.converter(23))
        self.assertEquals('XXVIII', self.conversor.converter(28))
        self.assertEquals('XXXI', self.conversor.converter(31))
        self.assertEquals('XLIX', self.conversor.converter(49))
        self.assertEquals('LIV', self.conversor.converter(54))
        self.assertEquals('LXVI', self.conversor.converter(66))
        self.assertEquals('LXXIII', self.conversor.converter(73))
        self.assertEquals('LXXXVIII', self.conversor.converter(88))
        self.assertEquals('XCIX', self.conversor.converter(99))
        self.assertEquals('CXXIII', self.conversor.converter(123))
        self.assertEquals('CCXXXIV', self.conversor.converter(234))
        self.assertEquals('CCCXLV', self.conversor.converter(345))
        self.assertEquals('CDLVI', self.conversor.converter(456))
        self.assertEquals('DLXVII', self.conversor.converter(567))
        self.assertEquals('DCLXXVIII', self.conversor.converter(678))
        self.assertEquals('DCCLXXXIX', self.conversor.converter(789))
        self.assertEquals('DCCCXC', self.conversor.converter(890))
        self.assertEquals('CMLXXXIX', self.conversor.converter(989))
