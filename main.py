import sys

from conversor_numeros_inteiros_para_romanos import ConversorDeNumerosInteirosParaRomanos


def main():
    numero = int(sys.argv[1])
    roman_number = ConversorDeNumerosInteirosParaRomanos().converter(numero)
    print('The equivalent roman number is: {}'.format(roman_number))

if __name__ == "__main__":
	main()
