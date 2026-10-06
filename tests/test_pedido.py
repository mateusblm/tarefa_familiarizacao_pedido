import pytest

from src.pedido import calcular_total_pedido


def test_calcula_frete_pago_corretamente():
    assert calcular_total_pedido(80.00, 10, False) == pytest.approx(103.00)


def test_aplica_frete_gratis_no_limite_de_cem_reais():
    assert calcular_total_pedido(100.00, 10, False) == pytest.approx(100.00)


def test_aplica_desconto_vip_antes_do_calculo_do_frete():
    assert calcular_total_pedido(100.00, 10, True) == pytest.approx(113.00)


def test_rejeita_subtotal_ou_distancia_negativos():
    with pytest.raises(ValueError):
        calcular_total_pedido(-1.00, 5, False)

    with pytest.raises(ValueError):
        calcular_total_pedido(50.00, -1, False)
