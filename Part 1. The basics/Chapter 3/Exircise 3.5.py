# 3.5 Изменение спика гостей

guest_list = ['Pavel', 'Anton', 'Vlad', 'Zexkillo', 'Alex']

for guest in guest_list:
    if guest == 'Pavel' or guest == 'Anton' or guest == 'Zexkillo' or guest == 'Alex':
        print(f'Welcome to the club body, {guest}!\n')
    if guest == 'Vlad':
        print(f'\tHe does not wonna go ->>> {guest}\n')

# Условие №1: заменить имя гостя, который не может прийти.
guest_list[2] = 'Nikolay'
print(f'Список приглашённых {guest_list}')
print()

# Условие №2 Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список
for guest in guest_list:
    print(f'Nice to meet you, {guest}!\n')