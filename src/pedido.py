def calcular_total_pedido(subtotal, distancia_km, cliente_vip=False):
    """Calcula o valor final de um pedido.

    A implementação inicial contém defeitos e deve ser corrigida
    de acordo com os requisitos descritos no README.
    """

    if subtotal < 0 and distancia_km < 0:
        raise ValueError("Subtotal e distância não podem ser negativos")

    desconto = 10 if cliente_vip else 0
    subtotal_com_desconto = subtotal - desconto

    if subtotal_com_desconto > 100:
        frete = 0
    else:
        frete = 8 + distancia_km

    total = subtotal + frete
    return total
