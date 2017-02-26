# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibi(n):
    a = 0
    b = 1

    while n > 0:
        a, b = b, a + b
        n = n - 1

    return a

for i in range(40):
    # print('fib({}) = {}'.format(i, fib(i)))
    print('fib({}) = {}'.format(i, fibi(i)))


