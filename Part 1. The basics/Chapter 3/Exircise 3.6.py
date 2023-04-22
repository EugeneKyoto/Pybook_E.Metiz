# 3.6 Больше гостей
guest_list = ['Pavel', 'Anton', 'Vlad', 'Zexkillo', 'Alex']

guest_list.insert(0, 'Vladimir') # Добавить нового гостя в начало списка.
guest_list.insert(3, 'Lex') # Добавить в середину списка.
guest_list.append('OG') # Добавить в конец списка.

for guest in guest_list:
    if guest == 'Vladimir' or guest == 'Lex' or guest == 'OG':
        print(f'Welcome {guest}! Nice to meet u!')
    else:
        print(f'Ты уже приглашён, {guest}!')

# Теория тестирования и sql едят время
# p.s. работа тоже, завтра запушу целую главу.. Надеюсь...