# Especificação do exercício

Faça um script que receba um valor entre `0.00` e `10.00` e calcule o número de moedas necessárias para trocar esse valor em reais levando em consideração que sempre são selecionadas as moedas de mais alto valor.
A saída deve ser no seguinte formato:

```markdown
São necessárias:
moedas de R$ 1.00: [m1]
moedas de R$ 0.50: [m2]
moedas de R$ 0.25: [m3]
moedas de R$ 0.10: [m4]
moedas de R$ 0.05: [m5]
moedas de R$ 0.01: [m6]
```

Os números `[m1]` até `[m6]` devem ser substituídos pela quantidade de moedas em questão.
Caso o valor seja zero, a linha deve ser suprimida na saída.
Deve ser utilizada uma chamada da função `print` para cada linha da saída.

## Exemplos

Entrada 1: `9.51`

Saída 1:

```markdown
São necessárias:
moedas de R$ 1.00: 9
moedas de R$ 0.50: 1
moedas de R$ 0.01: 1
```

Entrada 2: `5.00`

Saída 2:

```markdown
São necessárias:
moedas de R$ 1.00: 5
```

Entrada 3: `9.99`

Saída 3:

```markdown
São necessárias:
moedas de R$ 1.00: 9
moedas de R$ 0.50: 1
moedas de R$ 0.25: 1
moedas de R$ 0.10: 2
moedas de R$ 0.01: 4
```

Entrada 4: `0.09`

Saída 4:

```markdown
São necessárias:
moedas de R$ 0.05: 1
moedas de R$ 0.01: 4
```

Entrada 5: `0.37`

Saída 3:

```markdown
São necessárias:
moedas de R$ 0.25: 1
moedas de R$ 0.10: 1
moedas de R$ 0.01: 2
```
