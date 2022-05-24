# inverso é o s unico
# q esteja entre 0 e m, q é o b

def combinacao_linear(a, b):
    if b == 0:
        s, t = 1, 0
        return s, t

    s, t = combinacao_linear(b, a % b)

    return t, s - (a//b) * t


a = int(input("Digite o a: "))
b = int(input("Digite o b: "))

cl = combinacao_linear(a, b)


def inverso(s, m):
    if s > 0 and s < m:
        return s

    s %= m
    return s


s = cl[0]

print(f'inverso: {inverso(s, b)}')
