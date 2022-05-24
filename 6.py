# combinação linear
# mdc = s * x + t * y

# vamo la, vai dar

# resto = a - q * b
# a = b
# b = resto
# resto = b - q * b

# if resto = 0, -resto =

def combinacao_linear(a, m):
    if m == 0:
        s, t = 1, 0
        return s, t

    s, t = combinacao_linear(m, a % m)

    return t, s - (a//m) * t


a = int(input("Digite o a: "))
m = int(input("Digite o m: "))

cl = combinacao_linear(a, m)

print(f"s (ou x) = {cl[0]}\nt (ou y) = {cl[1]}")
