import pytest

from src.pedido import calcular_total_pedido


def test_calculo_do_total_em_cenarios_principais():
    assert calcular_total_pedido(80.00, 10, False) == pytest.approx(103.00)
    assert calcular_total_pedido(100.00, 10, False) == pytest.approx(100.00)
    assert calcular_total_pedido(100.00, 10, True) == pytest.approx(113.00)
    assert calcular_total_pedido(80.33, 2.2, False) == pytest.approx(91.63)


def test_rejeita_valores_negativos():
    with pytest.raises(ValueError):
        calcular_total_pedido(-1.00, 5, False)

    with pytest.raises(ValueError):
        calcular_total_pedido(50.00, -1, False)
