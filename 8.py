# ax ≡ b mod m
# achar o x, com x = abarra * b

def combinacao_linear(a, b):
    if b == 0:
        s, t = 1, 0
        return s, t

    s, t = combinacao_linear(b, a % b)

    return t, s - (a//b) * t


a = int(input("Digite o a: "))
b = int(input("Digite o b: "))
m = int(input("Digite o m: "))


cl = combinacao_linear(a, m)


def inverso(s, m):
    if s > 0 and s < m:
        return s

    s %= m
    return s


s = cl[0]

inverse = inverso(s, m)

congruencia = b * inverse if (b * inverse) <= m else (b * inverse) % m

print(f'\nax ≡ b mod(m)')
print(f'{a} * { {congruencia} } ≡ {b} mod({m})')
