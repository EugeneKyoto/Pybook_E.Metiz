# 5.6 Периоды жизни.
age = int(input("Добрый день, для идентификации скажите сколько вам лет: "))
if 0 < age < 2:
    print('Младенец.')
elif 2 <= age < 4:
    print('Малыш.')
elif 4 <= age < 13:
    print('Ребёнок.')
elif 13 <= age < 20:
    print('Подросток.')
elif 20 <= age < 65:
    print('Взрослый.')
elif 101 > age >= 65:
    print('Пожилой человек.')
else:
    print('Что ты такое?')