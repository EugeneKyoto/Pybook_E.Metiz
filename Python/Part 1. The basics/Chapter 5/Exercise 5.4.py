# 5.4 Цвета 2.
alliens = ['red', 'green', 'yellow']
for allien in alliens:
    if allien.lower() == 'red':
        print('Boss killed.\n+10 exp.\n')
    elif allien.lower() == 'yellow':
        print('Mini-boss killed.\n+7 exp.\n')
    else:
        print('Enemy killed.\n+5 exp.\n') 