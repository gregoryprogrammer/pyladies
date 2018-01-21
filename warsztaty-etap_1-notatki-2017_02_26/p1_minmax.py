def minmax(*args):
    print(repr(args))

    # 'naprawmy' args
    if len(args) == 1:
        args = args[0]

    print(repr(args))

    if len(args) == 0:
        return None

    mini = args[0]
    maks = args[0]

    for i in args:
        if i < mini:
            mini = i
        if i > maks:
            maks = i

    return mini, maks

a = minmax(1, 2, 6, 88, 2, -9, 45)
print(a)

print('---')

b = minmax([1, 2, 6, 88, 2, -9, 45])
print(b)

print('---')

c = minmax()
print(c)

print('---')

d = [1, 2, 6, 88, 2, -9, 45]

print((sorted(d)[0], sorted(d)[-1]))

