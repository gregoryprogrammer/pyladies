keys = ['name', 'animal', 'age']

ala = ['Ala', 'cat', 23]
tomek = ['Tomek', 'dog', 32]
piotr = ['Piotr', 'dolphin', 63]

users = [ala, tomek, piotr]

a = [dict(zip(keys,user)) for user in users]

print(a)