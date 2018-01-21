zdanie = input('Podaj co najmniej 3 wyrazy: ')

lista_slow = zdanie.split()

if len(lista_slow) < 3:
    print('Podałeś zbyt mało wyrazów! Do widzenia.')
    exit()

lista_slow.reverse()

nowe_zdanie = ' '.join(lista_slow)

print(nowe_zdanie)

