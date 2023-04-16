# 3.5 Изменение спика гостей

guest_list = ['Pavel', 'Anton', 'Vlad', 'Zexkillo', 'Alex']

for guest in guest_list:
    if guest == 'Pavel' or guest == 'Anton' or guest == 'Zexkillo' or guest == 'Alex':
        print(f'Welcome to the club body, {guest}!\n')
    if guest == 'Vlad':
        print(f'\tHe does"t wonna go ->>> {guest}\n')