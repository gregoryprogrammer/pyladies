eol = '\n\r'

a = ['{0} * {1} = {2}{3}'.format(i, j, i * j, '\r\n' if j == 9 else ', ') for i in range(10) for j in range(10)]


tabliczka = ''.join(a)
print(tabliczka)