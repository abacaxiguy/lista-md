# decompor um numero em seus fatores primos
# fatorar
# 10 | 2
# 5  | 5
# 1  | / -> 10, 2 * 5
primos = []


def eh_primo(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True


def fatores(x):
    for i in range(2, x+1):
        if eh_primo(i) and x % i == 0:
            primos.append(i)
            x = x // i
            if x == 1:
                return primos
            return fatores(x)


x = int(input("Digite um número para fatorar: "))
fatores(x)
print(f'Fatores de {x} são: {primos}')
