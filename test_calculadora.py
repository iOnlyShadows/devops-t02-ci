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


def test_cupom_soma_ao_desconto_percentual():
    itens = [(100.0, 2)]

    # 10% + 15% = 25% sobre 200.0
    assert calcular_total(itens, desconto_percentual=10, cupom="PROMO15") == 150.0


def test_cupom_sem_desconto_percentual():
    itens = [(100.0, 1)]

    assert calcular_total(itens, cupom="PROMO10") == 90.0


def test_cupom_inexistente_nao_altera_o_total():
    itens = [(100.0, 1)]

    assert calcular_total(itens, cupom="NAO_EXISTE") == 100.0


def test_desconto_somado_nao_passa_de_cem_por_cento():
    itens = [(100.0, 1)]

    # 80% + 50% = 130%, limitado a 100%: o total zera em vez de ficar negativo
    assert calcular_total(itens, desconto_percentual=80, cupom="METADE") == 0.0


def test_obter_desconto_do_cupom_sem_cupom():
    assert obter_desconto_do_cupom(None) == 0
