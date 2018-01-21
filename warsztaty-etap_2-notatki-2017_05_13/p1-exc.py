fruits = dict()
fruits['orange'] = 52
fruits['apple'] = 16

class BrakKlucza(Exception):
    komunikat = None

try:
    if 'kiwi' not in fruits.keys():
        wyjatek = BrakKlucza('nie ma kiwi')
        wyjatek.komunikat = 'zamów kiwi'
        raise wyjatek
    print('kiwi = ', fruits['kiwi'])
except BrakKlucza as err:
    print('Brak klucza:', err)
    print('Komunikat', err.komunikat)

