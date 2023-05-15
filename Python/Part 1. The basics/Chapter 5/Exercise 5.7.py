# 5.7 Любимый фрукт.
mff = ['Mango', 'Watermellon', 'Apple', 'Orange', 'Bananas', 'Potato']
for m in mff:
    if m.lower() == 'mango':
        print(f'{m.title()} - самый вкусный фрукт!')
    if m.lower() == 'watermellon':
        print(f'{m.title()} - хорошо кушать летом, а вообще это ягода, а не фрукт :)')
    if m.lower() == 'apple':
        print(f'{m.title()} - полезно!')
    if m.lower() == 'orange':
        print(f'{m.title()} - можно купить в любой сезон.')
    if m.lower() == 'bananas':
        print(f'{m.title()} - banana man xD')
else:
    print(f'{m} - это даже не фрукт!!!')