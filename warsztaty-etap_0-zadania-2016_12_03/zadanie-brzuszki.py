def brzuszki_z_ifem(liczba):
    liczba = str(liczba)
    suma = 0
    for znak in liczba:
        if znak in ['0', '6', '9', '0']:
            suma = suma + 1
        elif znak == '8':
            suma = suma + 2
    return suma

def brzuszki_bez_ifa(liczba):
    liczba = str(liczba)
    brzuchy = {'0':1, '6':1, '8':2, '9':1}
    suma = 0
    for znak in liczba:
        # metoda get dziala prawie tak samo jak indeksowanie slownika, czyli
        # brzuchy['6'] == brzuchy.get('6')
        # ale jest pewna roznica,
        # bo gdy w slownik nie ma klucza spod ktorego wyciagamy wartosc,
        # to mozemy podac domyslna wartosc ktora zostanie zwrocona zamiast.
        # na przyklad brzuchy.get('1', 0) zwroci 0, bo w slowniku brzuchy
        # nie ma klucza '1'
        suma = suma + brzuchy.get(znak, 0)
    return suma

# ta funkcja nie dziala tak jak trzeba,
# pomysl nie jest zly, ale jest pewien przypadek,
# o ktorym programista nie pomyslal,
# jesli masz ochote, to przeanalizuj,
# sprawdz jakie wyniki dają testy
def brzuszki_bez_stringa_i_bez_ifa(liczba):
    suma = 0
    brzuchy = {0:1, 6:1, 8:2, 9:1}
    # jesli nie wiesz jak dziala instrukcja while,
    # to sprawdz na przyklad tu: http://www.python-course.eu/python3_loops.php
    while liczba:
        suma = suma + brzuchy.get(liczba % 10, 0)
        liczba = liczba // 10
    return suma


print('Test 1.', brzuszki_z_ifem(12345) == 0)
print('Test 2.', brzuszki_z_ifem(0) == 1)
print('Test 3.', brzuszki_z_ifem(888) == 6)
print('Test 4.', brzuszki_z_ifem(86) == 3)
print('Test 5.', brzuszki_z_ifem(-99) == 2)
print('Test 5.', brzuszki_z_ifem(1234567890) == 5)

print('Test 1.', brzuszki_bez_ifa(12345) == 0)
print('Test 2.', brzuszki_bez_ifa(0) == 1)
print('Test 3.', brzuszki_bez_ifa(888) == 6)
print('Test 4.', brzuszki_bez_ifa(86) == 3)
print('Test 5.', brzuszki_bez_ifa(-99) == 2)
print('Test 5.', brzuszki_bez_ifa(1234567890) == 5)

print('Test 1.', brzuszki_bez_stringa_i_bez_ifa(12345) == 0)
print('Test 2.', brzuszki_bez_stringa_i_bez_ifa(0) == 1)
print('Test 3.', brzuszki_bez_stringa_i_bez_ifa(888) == 6)
print('Test 4.', brzuszki_bez_stringa_i_bez_ifa(86) == 3)
print('Test 5.', brzuszki_bez_stringa_i_bez_ifa(-99) == 2)
print('Test 5.', brzuszki_bez_stringa_i_bez_ifa(1234567890) == 5)
