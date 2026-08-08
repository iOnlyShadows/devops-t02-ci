CUPONS = {
    "PROMO10": 10,
    "PROMO15": 15,
    "METADE": 50,
}


def obter_desconto_do_cupom(cupom):
    """
    Devolve o percentual de desconto de um cupom.

    Cupom ausente ou desconhecido nao concede desconto.
    """
    if cupom is None:
        return 0

    return CUPONS.get(cupom, 0)


def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    desconto_total = desconto_percentual + obter_desconto_do_cupom(cupom)
    desconto_total = min(desconto_total, 100)
    total = subtotal * (1 - desconto_total / 100)

    return round(total, 2)
