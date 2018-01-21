wyraz = input('Podaj wyraz, minimum 10 znaków: ')

if len(wyraz) < 10:
    print('Przykro mi, {} jest zbyt krótkiem wyrazem. Do widzenia.'.format(wyraz))
    exit()

wyraz = wyraz.lower()

a = wyraz.count('a')
o = wyraz.count('o')
u = wyraz.count('u')
e = wyraz.count('e')
i = wyraz.count('i')
y = wyraz.count('y')
au = wyraz.count('ą')
eu = wyraz.count('ę')
oo = wyraz.count('ó')

suma = a + o + u + e + i + y + au + eu + oo

print('Naliczyłem {} samogłosek w {}.'.format(suma, wyraz))
