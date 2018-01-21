def revword(word):
    title = word.istitle()
    if title:
        return word[::-1].title()
    else:
        return word[::-1]


def revwords_1(text):
    words = text.split()
    new_words = []
    for word in words:
        tmp = revword(word)
        new_words.append(tmp)
    return ' '.join(new_words)

def revwords_2(text):
    return ' '.join([revword(word) for word in text.split()])

def revwords_3(text):
    return ' '.join(
                    [
                        word[::-1].title() if word.istitle() else word[::-1]
                        for word in text.split()
                    ]
                    )


print(revwords_3('Tomek ma psa Anatola'))
# Kemot am asp Alotana

print(revwords_3('Kemot am asp Alotana'))
# Tomek ma psa Anatola