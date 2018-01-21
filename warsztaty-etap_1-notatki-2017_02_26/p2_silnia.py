# n! = n * (n-1)!
# 0! = 1

def silnia_r(n):
    if n == 0:
        return 1
    return n * silnia_r(n - 1)

def silnia_i(n):
    wynik = n
    while n > 1:
        n = n - 1
        wynik = wynik * n
    return wynik

print(silnia_i(3), 6)
print(silnia_i(5), 120)

print('-' * 10)

print(silnia_r(3), 6)
print(silnia_r(5), 120)

print('-' * 10)

# test
def func():
    func()

func()