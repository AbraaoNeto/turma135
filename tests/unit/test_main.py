import csv

import pytest
from main import somar, subtrair, multiplicar, dividir

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Fail imprevista: {fail}')




def test_somar():
    numero_a = 10
    numero_b = 20

    resultado_esperado = 30

    resultado_obtido = somar (numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


def test_subtrair():
    numero_a = 10
    numero_b = 2

    resultado_esperado = 8

    resultado_obtido = subtrair(numero_a -numero_b)

    assert resultado_obtido == resultado_esperado




def test_multiplicar():
    numero_a = 10
    numero_b = 20

    resultado_esperado = 200

    resultado_obtido = multiplicar(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


def test_dividir_positivo():
    numero_a = 100
    numero_b = 20

    resultado_esperado = 5

    resultado_obtido = dividir(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


def test_dividir_negativo():

    numero_a = 27
    numero_b = 0

    resultado_eperado = 'Nao dividiras por zero'

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado',ler_csv('C:\\Users\Sabrina\\turma134\\Vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):

    numero_a = 10
    numero_b = 20

    resultado_esperado = 30

    resultado_obtido = somar(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado
