

def karatsuba(n1: str, n2: str) -> int:
    
    x, y = n1, n2
    
    numero_de_algarismos = max(len(x), len(y))

    
    if numero_de_algarismos == 1:
        return int(x) * int(y)
    
    x, y = x.zfill(numero_de_algarismos), y.zfill(numero_de_algarismos)
    
    meio = numero_de_algarismos // 2
    
    
    A = x[:meio]  # inicio do numero
    B = x[meio:]  # fim do numero
    C = y[:meio]
    D = y[meio:]
    
    E = karatsuba(A, C)
    F = karatsuba(B, D)
    G = karatsuba(str(int(A) + int(B)), str(int(C) + int(D)))
    H = G - E - F
    
    print(numero_de_algarismos - meio)
    resultado = (10 ** (2 * (numero_de_algarismos - meio))) * E + (10 ** (numero_de_algarismos - meio)) * H + F
    
    
    return resultado


if __name__ == '__main__':
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    
    karatsuba_result = karatsuba(n1, n2)
    print(f'O resultado da multiplicação é: {karatsuba_result}')
    