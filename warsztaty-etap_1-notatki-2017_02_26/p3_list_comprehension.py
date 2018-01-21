a = [i for i in range(10)]
b = [i for i in range(10) if i % 2 == 0]
c = [i for i in range(100) if i % 2 == 0 and i % 7 == 0]

print(a)
print(b)
print(c)

print('-' * 10)

d = [i * i for i in range(10)]
e = ['{0}*{0} = {1}'.format(i, i * i) for i in range(10)]


def K(c):
    return c + 273.15

f = {(i, K(i)) for i in range(0, 100, 10)}


print(d)
print(e)
print(f)


# źle: zbior = {}
# bo to jest słownik
zbior = set()
