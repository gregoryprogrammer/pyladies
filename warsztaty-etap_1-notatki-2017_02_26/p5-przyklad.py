def bold(text):
    return '<b>{}</b>'.format(text)


def wizytowka_html(**kwargs):
    # 1. wygeneruj dane
    data = []
    for key, value in kwargs.items():
        row = '<td>{}</td> <td>{}</td>'.format(key, bold(value))
        data.append(row)

    html = ''
    # 2. print
    html += '<table border=1>'
    for row in data:
        html += '<tr>' + row + '</tr>'
    html += '</table>'
    html += '<br/>'
    return html

with open('baza.txt') as plik:
    content = plik.read()

    master_html = ''
    for row in content.split('\n'):
        name, job, lang = row.split(',')

        html = wizytowka_html(name=name, job=job, lang=lang)
        master_html += html

    with open('index.html', 'w') as plik_html:
        plik_html.write(master_html)