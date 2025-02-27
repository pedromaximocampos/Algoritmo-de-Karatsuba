# Algoritmo-de-Karatsuba

### Descrição do projeto:

O algoritmo de Karatsuba é um método eficiente para multiplicação de números grandes, reduzindo a complexidade de O(n^2) para aproximadamente O(n^(log₂3)). Ele funciona dividindo os números em duas partes e aplicando a recursão para reduzir o número de multiplicações diretas

#### Explicação (linha a linha):

- Define a função karatsuba que recebe dois números como strings e retorna um int

```python

def karatsuba(n1: str, n2: str) -> int:

```

- x e y armazenam os números de entrada.
- numero_de_algarismos pega o maior comprimento entre os dois números para garantir que tenham o mesmo número de dígitos.

```python

 x, y = n1, n2
 numero_de_algarismos = max(len(x), len(y))

```

- Se os números tiverem apenas um dígito, a multiplicação pode ser feita diretamente e retornada (condição de parada).

```python

 if numero_de_algarismos == 1:
        return int(x) * int(y)
```

- Usa zfill para preencher com zeros à esquerda e garantir que ambos os números tenham o mesmo número de dígitos.

```python

  x, y = x.zfill(numero_de_algarismos),  y.zfill(numero_de_algarismos)
```

- Divide o número ao meio para separá-lo em duas partes. Aqui, // garante que a divisão seja inteira.

```python

    meio = numero_de_algarismos // 2
```

- O número x é dividido em duas partes: A (parte esquerda) e B (parte direita)

- O mesmo acontece com y, gerando C e D.

```python

    A = x[:meio]  # início do número
    B = x[meio:]  # fim do número
    C = y[:meio]
    D = y[meio:]

    H = G - E - F
```

- E = A \* C → Multiplica as partes mais significativas.
- F = karatsuba(B, D)
- G = (A + B) \* (C + D) → Multiplica as somas das partes.
- H = G - E - F → Encontra a parte intermediária eliminando as parcelas repetidas.

```python

    E = karatsuba(A, C)
    F = karatsuba(B, D)
    G = karatsuba(str(int(A) + int(B)), str(int(C) + int(D)))
    H = G - E - F
```

- E precisa ser deslocado para a esquerda duas vezes (multiplicado por 10^(2 \* (numero_de_algarismos - meio))).

- H precisa ser deslocado para a esquerda uma vez (multiplicado por 10^(numero_de_algarismos - meio)).

- F fica na posição original.

Somamos os três valores para obter o resultado final.

```python

   resultado = (10 ** (2 * (numero_de_algarismos -meio))) * E + (10 ** (numero_de_algarismos - meio)) * H + F

```

## Rodando o código:

Se você tem o Python instalado, basta abrir o terminal na pasta do projeto e rodar o comando abaixo no terminal:

```
python main.py
```

## Relatório Técnico:
