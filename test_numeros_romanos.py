# coding=utf-8
from unittest.case import TestCase


def converte_em_numero_romano(valor):
    if valor == 1:
        return 'I'
    if valor == 2:
        return 'II'
    if valor == 3:
        return 'III'

class NumerosRomanosTests(TestCase):

    def test_escreve_um(self):
        resultado = converte_em_numero_romano(1)
        self.assertEquals(resultado, 'I')

    def test_escreve_dois(self):
        resultado = converte_em_numero_romano(2)
        self.assertEquals(resultado, 'II')

    def test_escreve_tres(self):
        resultado = converte_em_numero_romano(3)
        self.assertEquals(resultado, 'III')
