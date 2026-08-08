import pytest

from calculadora import calcular_total, obter_desconto_do_cupom


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]

    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)


def test_cupom_devops10_funciona_com_minusculas():
    itens = [(200.0, 1)]

    assert calcular_total(itens, cupom="devops10") == 180.0


def test_cupom_soma_com_desconto_existente():
    itens = [(100.0, 1)]

    total = calcular_total(
        itens,
        desconto_percentual=5,
        cupom="DEVOPS10",
    )

    assert total == 85.0


def test_cupom_invalido_gera_erro():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], cupom="XPTO")


def test_cupom_boasvindas5():
    itens = [(200.0, 1)]

    assert calcular_total(itens, cupom="BOASVINDAS5") == 190.0


def test_cupom_ignora_espacos_em_volta():
    itens = [(200.0, 1)]

    assert calcular_total(itens, cupom="  devops10  ") == 180.0


def test_desconto_somado_nao_passa_de_cem_por_cento():
    itens = [(100.0, 1)]

    # 100% + 10% = 110%, limitado a 100%: o total zera em vez de ficar negativo
    assert calcular_total(itens, desconto_percentual=100, cupom="DEVOPS10") == 0.0


def test_sem_cupom_nao_concede_desconto():
    assert obter_desconto_do_cupom(None) == 0
