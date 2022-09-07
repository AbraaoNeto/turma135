import pytest
import requests

    # variaves puplicas

url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


def teste_incluir_pet():
    # dados de entrada provem do pet.json


    # Resultado Esperados

    status_code_esperado = 200
    pet_id_esperado = 4859374
    pet_nome_esperado = "peludo"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_teg_esperado = "vacinado"

    #Execulta
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\Sabrina\\turma134\\Vendors\\Json\\pet.json')
    )

    #Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_teg_esperado
