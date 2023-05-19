<<<<<<< HEAD
# 5.10 Проверка имён пользователей.
current_users = ['Eric', 'Eugene', 'Pavel', 'Anton', 'Alex', 'Vlad', 'Vitaliy', 'Yuriy']
new_users = ['Eugene', 'Pavel', 'John', 'Michael', 'Lui']

for user in current_users:
    if user in new_users:
        print(f'{user} - это имя уже используется!')
    else:
        print(f'{user.lower()} - это имя свободно!')

current_users2 = current_users.copy()
current_users2.append('John')
for i in current_users2:
    if i.lower() == 'john':
        print(f'\n{i.upper()} - already used.\n')
print(current_users2)
=======
# 5.10 не могу пока понять, отработал 14 часов...Отложу на завтра.
current_users = ['Eric', 'Eugene', 'Pavel', 'Anton', 'Alex', 'Vlad', 'Vitaliy', 'Yuriy']
new_users = []
>>>>>>> origin
