def fatorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fatorial(x - 1)
