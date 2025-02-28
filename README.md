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

### Complexidade ciclomática:

```

       (N1) Inicio
          │
          ▼
        (N2) numero_de_algarismos == 1?
        ├──────────► (N3) Retorna x * y  [Sim]
        │
        ▼
       (N4) karatsuba(A, C)
        │
        ▼
       (N5) karatsuba(B, D)
        │
        ▼
       (N6) karatsuba(A+B, C+D)
        │
        ▼
      (N7) Retorna resultado final


```

Formula complexidade ciclomática : 𝑀 = 𝐸 − 𝑁 + 2𝑃

M = Arestas - Nos + 2 \* Componentes(no caso 1)

M = 7 - 6 + 2

M = 3

## Complexidade assintótica

| Tipo de Complexidade      | Valor      |
| ------------------------- | ---------- |
| **Complexidade Temporal** | O(n^1.585) |
| **Complexidade Espacial** | O(n)       |
| **Melhor Caso**           | O(1)       |
| **Caso Médio**            | O(n^1.585) |
| **Pior Caso**             | O(n^1.585) |

## Melhor caso:

Número de algarismos == 1. O Algoritmo então não realiza a divisão dos números e apenas retorna o resultado da multiplicação dos dois números passados por parametro.

### **Pior Caso** - \( O(n^{1.585}) \)

No pior caso, o algoritmo realiza a divisão dos números de forma desbalanceada, levando a uma maior profundidade recursiva e um número elevado de multiplicações. Cada divisão gera subproblemas que exigem chamadas recursivas adicionais, com um crescimento não linear das operações, resultando em uma complexidade de \( O(n^{1.585}) \).

### **Caso Médio** - \( O(n^{1.585}) \)

No caso médio, o comportamento do algoritmo é similar ao pior caso, com as chamadas recursivas dividindo os números em subproblemas equilibrados. A complexidade continua sendo \( O(n^{1.585}) \), já que a quantidade de multiplicações e somas de subproblemas segue o mesmo padrão do pior caso, mas com uma distribuição menos desbalanceada.
