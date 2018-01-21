# -*- coding: utf8 -*-

# with open('pan-tadeusz.txt') as plik:
#     for line in plik:
#         print(repr(line))


# with open('pan-tadeusz.txt') as plik:
#     content = plik.read()
#     print(content)

# with open('plik.txt', 'w') as plik:
#     plik.write('Tomek ma psa Anatola')
#     plik.write('\n\r')
#     plik.write('Tomek ma psa Anatola')
#     plik.write('\n\r')
#     plik.write('Tomek ma psa Anatola')
#     plik.write('\n\r')

# tmp = ''

# with open('pan-tadeusz.txt') as plik:
#     content = plik.read()
#     # print(type(content))
#     content = content.split('\n')
#     # print(type(content))
#     content = sorted(content)
#     # print(type(content))
#     tmp = '\n'.join(content)

# with open('pan-sorted.txt', 'wt') as plik:
#     plik.write(tmp)


with open('pan-tadeusz.txt') as plik:
    content = plik.read().split()

    clean = []
    for word in content:
        tmp = word.replace(',', '').replace('.', '')
        tmp = tmp.replace('!', '').replace('?', '')
        tmp = tmp.lower()
        clean.append(tmp)

    count_words = {}
    for word in clean:
        if word not in count_words.keys():
            count_words[word] = 1
        else:
            count_words[word] += 1

    for key, value in count_words.items():
        if value > 100:
            print(key, '=', value)

    print('-----')
    print(count_words.get('mrówki'))
    print(count_words.get('piersi'))




    # zbior = set(clean)
    # print(len(zbior))
