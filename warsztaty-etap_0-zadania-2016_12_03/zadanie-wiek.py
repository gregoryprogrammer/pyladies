imie = input('Podaj imie: ')
nazwisko = input('Podaj nazwisko: ')
rok = input('Podaj rok urodzenia: ')

# wczytan rok jest stringiem, a potrzebujemy int
rok = int(rok)

# obliczamy wiek
wiek = 2016 - rok

if wiek % 3 == 0:
    print('Cześć {}! Za 20 lat będziesz miał {} lat'.format(imie, wiek + 20))
else:
    print('{}. {}.'.format(imie[0], nazwisko[0]))
