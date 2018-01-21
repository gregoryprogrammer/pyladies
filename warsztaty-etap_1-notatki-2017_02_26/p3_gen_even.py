def even_numbers(N):
    return [i for i in range(N) if i % 2 == 0]

def even_numbers_gen(N):
    for i in range(N):
        if i % 2 == 0:
            yield i

tmp1 = even_numbers(10)
tmp2 = even_numbers_gen(10)

print('----------')

print(tmp1)
print(list(tmp2))