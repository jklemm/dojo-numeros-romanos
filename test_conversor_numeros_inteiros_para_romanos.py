# coding=utf-8
from unittest.case import TestCase
from conversor_numeros_inteiros_para_romanos import ConversorDeNumerosInteirosParaRomanos


class ConverteParaNumerosRomanosTests(TestCase):

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

    def test_todos_os_milhares(self):
        self.assertEquals('M', self.conversor.converter(1000))
        self.assertEquals('MM', self.conversor.converter(2000))
        self.assertEquals('MMM', self.conversor.converter(3000))
        self.assertEquals('ĪV̄', self.conversor.converter(4000))
        self.assertEquals('V̄', self.conversor.converter(5000))
        self.assertEquals('V̄Ī', self.conversor.converter(6000))
        self.assertEquals('V̄ĪĪ', self.conversor.converter(7000))
        self.assertEquals('V̄ĪĪĪ', self.conversor.converter(8000))
        self.assertEquals('ĪX̄', self.conversor.converter(9000))

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
        self.assertEquals('MCCXXXIV', self.conversor.converter(1234))
        self.assertEquals('MMCCCXLV', self.conversor.converter(2345))
        self.assertEquals('MMMCDLVI', self.conversor.converter(3456))
        self.assertEquals('ĪV̄DLXVII', self.conversor.converter(4567))
        self.assertEquals('V̄DCLXXVIII', self.conversor.converter(5678))
        self.assertEquals('V̄ĪDCCLXXXIX', self.conversor.converter(6789))
        self.assertEquals('V̄ĪĪDCCCXC', self.conversor.converter(7890))
        self.assertEquals('V̄ĪĪĪCMI', self.conversor.converter(8901))
        self.assertEquals('ĪX̄XII', self.conversor.converter(9012))
        self.assertEquals('ĪX̄CMXCIX', self.conversor.converter(9999))
