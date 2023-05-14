# 5.2 Больше условий.
cars = ['Bmw', 'Audi', 'Vaz', 'Vortex', 'Man', 'Mazda', 'Honda', 'Kia', 'Toyota']

# Проверка равенства и неравенства строк + lower().
for car in cars:
    if car.lower() == 'bmw':
        print('TRUE')
    if car.lower() != 'bmw':
        print('FALSE')

# Числовые проверки равенства + вспомнил цикл while + логический оператор.
age = 18
if age >= 18:
    print('Доступ разрешён.\n')
if age < 18:
    print('Доступ запрещён.\n')

age1 = int(input('Сколько вам лет: '))
while True:
    if age1 >= 18 and 65 >= age1:
        print('Годен. Следующий!')
        age1 = int(input('Сколько вам лет: '))
    else:
        print('Не годен. Последний, повезло.\n')
        break

# Проверка вхождения элемента в список.
pizzas = ['Пепперони', 'Маргарита', '4 сыра']
if 'Гавайская' not in pizzas:
    print('\nСрочно добавьте в меню Гавайскую пиццу!')
if 'Маргарита' in pizzas:
    print('Марграрита есть? Отлично! Прекрасная пицца!')