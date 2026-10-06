# Tarefa de Familiarização — Correção de Defeitos em Cálculo de Pedido

## Objetivo

O arquivo `src/pedido.py` contém uma função responsável por calcular o valor final de um pedido. A implementação atual possui defeitos.

Sua tarefa é corrigir o código existente para que ele atenda a todos os requisitos abaixo e seja aprovado pelos testes automatizados.

Tempo máximo: 25 minutos.

## Função a ser corrigida

```python
calcular_total_pedido(subtotal, distancia_km, cliente_vip=False)
```

A função deve retornar um `float` com o valor final do pedido.

## Requisitos

1. Se `subtotal` for negativo, a função deve lançar `ValueError`.
2. Se `distancia_km` for negativa, a função deve lançar `ValueError`.
3. Clientes VIP recebem **10% de desconto sobre o subtotal** antes do cálculo do frete.
4. Se o subtotal após o desconto VIP for **maior ou igual a R$ 100,00**, o frete deve ser gratuito.
5. Quando houver cobrança de frete, o valor deve ser **R$ 8,00 + R$ 1,50 por quilômetro**.
6. O total final deve ser calculado usando o subtotal já descontado, somado ao frete, e retornado com **duas casas decimais**.

## Critérios de conclusão

A tarefa será considerada concluída quando:

1. A assinatura da função `calcular_total_pedido` for mantida.
2. Valores negativos para `subtotal` e `distancia_km` forem rejeitados com `ValueError`.
3. O desconto de cliente VIP for calculado corretamente como 10% do subtotal.
4. A regra de frete gratuito para valores a partir de R$ 100,00 após o desconto estiver correta.
5. O frete pago for calculado usando a fórmula `8 + 1.5 * distancia_km`.
6. O valor final considerar desconto e frete e for retornado com duas casas decimais.
7. Todos os testes automatizados forem aprovados.

## Exemplos de entrada e saída

```python
calcular_total_pedido(80.00, 10, False)
# Retorno esperado: 103.00
```

Explicação: frete = 8 + (1,5 × 10) = 23; total = 80 + 23 = 103.

```python
calcular_total_pedido(120.00, 10, False)
# Retorno esperado: 120.00
```

Explicação: subtotal >= 100, então o frete é gratuito.

```python
calcular_total_pedido(100.00, 10, True)
# Retorno esperado: 113.00
```

Explicação: cliente VIP recebe 10% de desconto, resultando em subtotal de 90. Como 90 < 100, o frete é 23. Total = 90 + 23 = 113.

```python
calcular_total_pedido(-10.00, 5, False)
# Deve lançar ValueError
```

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest -q
```

A implementação inicial contém defeitos, portanto é esperado que os testes falhem antes das correções.
