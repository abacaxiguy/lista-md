# combinação linear
# mdc = s * x + t * y

# vamo la, vai dar

# resto = a - q * b
# a = b
# b = resto
# resto = b - q * b

# if resto = 0, -resto =

def combinacao_linear(a, b):
    if b == 0:
        s, t = 1, 0
        return s, t

    s, t = combinacao_linear(b, a % b)

    return t, s - (a//b) * t


a = int(input("Digite o a: "))
b = int(input("Digite o b: "))

cl = combinacao_linear(a, b)

print(f"s (ou x) = {cl[0]}\nt (ou y) = {cl[1]}")
