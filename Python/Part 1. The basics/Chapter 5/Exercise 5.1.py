# 5.1 Проверка условий.
car = 'Vortex'
print(car == 'Vortex') # Условие истинно: True.

print(car == 'BMW') # Условие ложно: False.

cars = ['Bmw', 'Audi', 'Vaz', 'Vortex', 'Man', 'Mazda']

for cara in cars:
    if cara == 'Bmw':
        print(f'{cara.upper()} is a good car!')
    if cara == 'Audi':
        print(f'{cara} is a greatest car!')
    if cara == 'Vaz':
        print(f'{cara.upper()} so bad car...')
    else:
        print(f'{cara.upper()} is a normal car.')