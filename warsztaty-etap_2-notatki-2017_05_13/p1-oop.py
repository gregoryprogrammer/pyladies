
class Planet:
    name = None

    def __init__(self, name='bez nazwy'):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        name1 = self.name
        if name1[-1] == 'a':
            name1 = name1[0:-1] + 'o'
        name2 = other.name.lower()
        name = '{}{}'.format(name1, name2)
        return Planet(name)

    def __sub__(self, other):
        return Planet('nie żartuj')

earth = Planet('Ziemia')
mars = Planet('Mars')
print('Nazwa planety 1:', earth)
print('Nazwa planety 2:', mars)
print('Suma planet 1 i 2:', earth + mars)
print('Różnica planet 1 i 2:', earth - mars)
