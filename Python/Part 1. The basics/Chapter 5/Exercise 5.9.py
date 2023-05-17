# 5.9
users = ['Eugene', 'Sudo', 'Admin', 'Stan', 'Ekaterina']

for user in users:
    if user.lower() == 'admin':
        print(f'\nHello {user.title()}, would you like to see a status report?\n')
    else:
        print(f'Hello {user}, thank you for logging in again.')

users = []
if len(users) == 0:
    print('\nWe need to ind some users!')