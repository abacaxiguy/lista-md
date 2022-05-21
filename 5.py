# mdc (116, 68) = 4, mas como?

# euclides = recursao com a formula r = x - y * q
#                           sendo r = resto
#                           e q = quociente
# funcao para calcular quociente
# quociente = numero mais proximo para multiplicar y, q chegue proximo de x


def quociente(x, y):
    for i in range(1, x):
        if y * i > x:
            return i - 1


def euclides(x, y):
    q = quociente(x, y)
    resto = x - y * q
    if resto == 0:
        return y
    return euclides(y, resto)


x = int(input("Digite o primeiro número para o mdc com euclides: "))
y = int(input("Digite o segundo número para o mdc com euclides: "))
print(f'O MDC de {x} e {y} é: {euclides(x, y)}')
