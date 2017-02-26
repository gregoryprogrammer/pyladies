def func(*args):
    print(type(args))
    suma = 0
    for i in args:
        suma = suma + i
    return suma

def give_me_four(a, b, c, d):
    pass

s = func(1, 2, 3, 4)

print(s)

args = [1, 2, 3, 4]
give_me_four(*args)

def show(**kwargs):
    name = kwargs.get('name')
    job = kwargs.get('job')
    print('Człowiek nazywa się {} i jest {}'.format(name, job))

user = {}
user['name'] = 'Kamil'
user['job'] = 'Programista'

show(name='Kamil', job='Programista')