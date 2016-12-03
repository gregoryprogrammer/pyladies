#! env python3

import re
# <a href="#part1">1</a>

with open('index.html') as f:
    data = f.read().split('\n')

for row in data:
    divid = re.search(r'^<div id="([\w|-]*)"', row)
    if divid:
        i = divid.group(1)

        href = '<a href="#{0}">{0}</a>'.format(i)

        print(href)