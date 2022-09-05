import pytest

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Nao dividiras por zero'
## Obs: o try except é um segunda opção de erro ou que não pode ser execultada.

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

    resultado_obtido = dividir(numero_a,  numero_b)
    assert resultado_obtido == resultado_eperado

##abra
