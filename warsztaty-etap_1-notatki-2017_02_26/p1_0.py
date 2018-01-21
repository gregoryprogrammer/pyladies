user = {}
user['name'] = 'Tomek'
user['animal'] = 'pies'
user['age'] = 32

print(user)
print(user['animal'])

# del user['age']
age = user.get('age')

if age:
    print('Tomek ma lat', age)

print('---------')


for key, value in user.items():
    print(key, '→', value)

for i in range(10):
    print(user)