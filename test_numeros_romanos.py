# coding=utf-8
from unittest.case import TestCase


def parser_numerico(valor):
    valor_texto = str(valor)
    comprimento = len(valor_texto)

    centena = valor_texto[-3:]
    milhar = valor_texto[-6:-3]
    milhao = valor_texto[-9:-6]
    bilhao = valor_texto[-12:-9]


def converte_em_numero_romano(valor):
    if valor <= 3:
        return 'I' * valor
    elif 4 <= valor <= 5:
        return 'I' * (5 - valor) + 'V'
    elif 6 <= valor <= 8:
        return 'V' + 'I' * (valor - 5)
    elif valor == 9:
        return 'IX'



class NumerosRomanosTests(TestCase):

    def test_escreve_um(self):
        self.assertEquals(converte_em_numero_romano(1), 'I')

    def test_escreve_dois(self):
        self.assertEquals(converte_em_numero_romano(2), 'II')

    def test_escreve_tres(self):
        self.assertEquals(converte_em_numero_romano(3), 'III')

    def test_escreve_quatro(self):
        self.assertEquals(converte_em_numero_romano(4), 'IV')

    def test_escreve_cinco(self):
        self.assertEquals(converte_em_numero_romano(5), 'V')

    def test_escreve_seis(self):
        self.assertEquals(converte_em_numero_romano(6), 'VI')

    def test_escreve_sete(self):
        self.assertEquals(converte_em_numero_romano(7), 'VII')

    def test_escreve_oito(self):
        self.assertEquals(converte_em_numero_romano(8), 'VIII')

    def test_escreve_nove(self):
        self.assertEquals(converte_em_numero_romano(9), 'IX')

    def test_escreve_dez(self):
        self.assertEquals(converte_em_numero_romano(10), 'X')

    def test_escreve_treze(self):
        self.assertEquals(converte_em_numero_romano(17), 'XIII')

    def test_escreve_dezessete(self):
        self.assertEquals(converte_em_numero_romano(17), 'XVII')
