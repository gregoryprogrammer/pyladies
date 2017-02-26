# user = {}
# user['name'] = 'Kamil'
# user['job'] = 'Programista'
# user['lang'] = 'Python 2.7'

# +------------------+
# | name: Kamil      |
# | job: Programista |
# | lang: Python 2.7 |
# +------------------+

def wizytowka(**kwargs):
    # 1. wygeneruj dane
    data = []
    max_row_len = 0
    for key, value in kwargs.items():
        row = '{}: {}'.format(key, value)
        data.append(row)

        row_len = len(row)
        if row_len > max_row_len:
            max_row_len = row_len

    # 2. print
    border = '+' + '-' * (max_row_len + 2) + '+'
    print(border)
    for row in data:
        spaces = max_row_len - len(row)
        print('|', row, ' ' * spaces + '|')
    print(border)

# wizytowka(name='Kamil', job='Programista', lang='Python 2.7')
# print()
# wizytowka(name='Sławek', job='Programista', lang='C')
# print()
# wizytowka(name='Tomek', job='Prezes', lang='C++')
# print()

def get_user():
    user = {}
    user = OrderedDict()
    user['name'] = input('Podaj imie:')
    user['job'] = input('Podaj job:')
    user['lang'] = input('Podaj lang:')
    return user

users = []
quit = False

while not quit:
    print('[1] Dodaj osobę')
    print('[q] Zakończ program')

    choice = input('Wybór:')

    if choice == '1':
        user = get_user()
        users.append(user)
    elif choice == 'q':
        quit = True
    else:
        print('Nie ma takiej opcji!')
    print()

for user in users:
    wizytowka(**user)




