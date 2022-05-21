# mmc(10, 12) =
# 10, 12 | 2
# 5, 6   | 2
# 5, 3   | 3
# 5, 1   | 5
# 1, 1   | / 2 * 2 * 3 * 5 = 60


# mdc(10, 12) =
# 10, 12 | 2*
# 5, 6   | 2
# 5, 3   | 3
# 5, 1   | 5
# 1, 1   | / 2

from functools import reduce


def eh_primo(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True


def mmc(x, y, primos):
    maior = x if x > y else y
    for i in range(2, maior+1):
        if eh_primo(i) and (x % i == 0 or y % i == 0):

            primos.append(i)

            if x % i == 0 and y % i == 0:
                y //= i
                x //= i
            elif x % i == 0:
                x //= i
            else:
                y //= i

            if x == 1 and y == 1:
                return primos

            return mmc(x, y, primos)


def mdc(x, y, primos):
    maior = x if x > y else y
    for i in range(2, maior+1):
        if eh_primo(i) and (x % i == 0 or y % i == 0):

            if x % i == 0 and y % i == 0:
                primos.append(i)

            if x % i == 0 and y % i == 0:
                y //= i
                x //= i
            elif x % i == 0:
                x //= i
            else:
                y //= i

            if x == 1 and y == 1:
                return primos

            return mdc(x, y, primos)


x = int(input("Digite o primeiro número para o mdc e o mmc: "))
y = int(input("Digite o segundo número para o mdc e o mmc: "))

primos_mmc = []
mmc(x, y, primos_mmc)
mmc_final = reduce(lambda mmc, n: n * mmc, primos_mmc, 1)
print(f'O MMC de {x} e {y} é: {mmc_final}')

primos_mdc = []
mdc(x, y, primos_mdc)
mdc_final = reduce(lambda mdc, n: n * mdc, primos_mdc, 1)
print(f'O MDC de {x} e {y} é: {mdc_final}')
