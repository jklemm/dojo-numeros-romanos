from unittest.case import TestCase
from explode_numeros_inteiros import ExplodeNumerosInteiros

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
