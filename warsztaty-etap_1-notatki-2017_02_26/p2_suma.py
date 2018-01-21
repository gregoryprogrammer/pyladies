def suma(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + suma(numbers[1:])

print(suma([1, 2, 3, 4, 5]), '== 15')
print(suma([1, 0, 3, 4, 5]), '== 13')
print(suma([1, 1, 3, 4, -5]), '== 4')

def my_len(text):
    if text == '':
        return 0
    return 1 + my_len(text[1:])

print(my_len('Ala'), 3)
print(my_len('Ala ma kota'), len('Ala ma kota'))
print(my_len('Tomek i pies'), len('Tomek i pies'))

#suma([1, 4, 6, 2, 3])
#     = 1 +   suma([4, 6, 2, 3])
#     = 1 + ( 4 + suma([6, 2, 3]) )
#     = 1 + ( 4 + (6 + suma([2, 3]) ) )
#     = 1 + ( 4 + (6 + (2 + suma([3]) ) ) )
#     = 1 + ( 4 + (6 + (2 + (3 + suma([]) ) ) ) ) )
#     = ....