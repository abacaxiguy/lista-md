# 1|P ou P|P

def eh_primo(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True


x = int(input("Digite um número para checar se ele é primo: "))
print(f'{x} é primo') if eh_primo(x) else print(f'{x} não é primo')
