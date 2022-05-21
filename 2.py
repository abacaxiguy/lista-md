# 1|P ou P|P

import time


def eh_primo(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True


now = time.time()
i = 2


while True:
    now_plus_60 = time.time()

    if round(now_plus_60 - now) == 60:
        break

    print(i) if eh_primo(i) else ""

    i += 1
