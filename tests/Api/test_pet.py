import json

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

    # Execulta
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\Sabrina\\turma134\\Vendors\\Json\\pet.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_teg_esperado


def teste_consultar_pet():

    pet_id = '4859374'

    status_code_esperado = 200
    pet_id_esperado = 4859374
    pet_nome_esperado = "peludo"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_teg_esperado = "vacinado"

    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_teg_esperado


def teste_alterar_pet():
#configura
    status_code_esperado = 200
    pet_id_esperado = 4859374
    pet_nome_esperado = "peludo"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_teg_esperado = "vacinado"
    pet_status_esperado = 'pending'
#Execulta
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\Sabrina\\turma134\\Vendors\\Json\\pet1.json')
    )
#Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_teg_esperado
    assert corpo_do_resultado_obtido['status']== pet_status_esperado
