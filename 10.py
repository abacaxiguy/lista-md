from copy import copy
from functools import reduce


congruencias = []
mzinhos = []
M = 1
coprimos = True
xo = 0

n = int(input("Quantas congruencias?: "))
# n = 3


def eh_primo(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True


def combinacao_linear(a, b):
    if b == 0:
        s, t = 1, 0
        return s, t

    s, t = combinacao_linear(b, a % b)

    return t, s - (a//b) * t


def inverso(s, m):
    if s > 0 and s < m:
        return s

    s %= m
    return s


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


for cong in range(1, n+1):
    b = int(input(f'Digite o b{cong}: '))
    m = int(input(f'Digite o m{cong}: '))

    M *= m

    congruencias.append({"b": b, "m": m})
    mzinhos.append(m)


for i, mzin in enumerate(mzinhos):
    mods_sem_mod = copy(mzinhos)
    mods_sem_mod.pop(i)

    primos_mdc = []
    for mod in mods_sem_mod:
        mdc(mzin, mod, primos_mdc)
        mdc_final = reduce(lambda mdc, n: n * mdc, primos_mdc, 1)

        if mdc_final != 1:
            coprimos = False
            break

    if not coprimos:
        break


if coprimos:
    for cong in congruencias:
        m = cong["m"]
        b = cong["b"]
        a = M/cong["m"]

        cl = combinacao_linear(a, m)

        s = cl[0]

        inverse = inverso(s, m)

        if inverse > m:
            inverse %= m

        elif inverse < 0:
            inverse += m

        xo += a * b * inverse

    if xo < 0:
        xo += M

    elif xo > M:
        xo %= M

    print(f'Xo = {xo}')

else:
    print("Os mods não são coprimos")
