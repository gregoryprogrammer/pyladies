#! env python3

import re

with open('index.html', 'rt') as f:
    data = f.read().split('\n')

dupa = []

x = 0
y = 0

for row in data:

    # if 'data-x' in row and 'data-y' in row:
    prefix = row.split('data-x')[0]

    data_x = re.search(r'.+data-x="(\d*)"', row)
    data_y = re.search(r'.+data-y="(\d*)"', row)

    if data_x and data_y:
        print(row)
        dxs = data_x.group(1)
        dys = data_y.group(1)
        dx = int(data_x.group(1))
        dy = int(data_y.group(1))
        print(dx, dy)
        print(data_x)

        ble = row[0:(data_x.span()[1] - len(dxs) - 2)] + '"{}" data-y="{}"' + row[data_y.span()[1]:]

        if dy != y:
            x = 0
            y = dy

        ble = ble.format(x, dy)

        print('OLD:', row)
        print('NEW:', ble)
        print(0)

        if not 'begin-example' in row:
            x += 1500

        row = ble


    dupa.append(row)

with open('index.html', 'wt') as f:
    f.write('\n'.join(dupa))
