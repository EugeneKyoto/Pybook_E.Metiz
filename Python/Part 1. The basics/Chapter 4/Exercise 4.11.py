# 4.11 Моя пицца, твоя пицца.
pizzas = ['Пепперони', 'Маргарита', '4 сыра']
friend_pizza = pizzas[:]

pizzas.append('Студенческая')
friend_pizza.append('Гавайская')

print('My favorite pizzas are:')
for i in pizzas:
    print(f'\t-{i}')
print('\nMy friend’s favorite pizzas are:')
for i in friend_pizza:
    print(f'\t-{i}')