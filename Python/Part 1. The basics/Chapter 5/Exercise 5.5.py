# 5.5 Цвета 3.
alliens = ['red', 'green', 'yellow']
for allien in alliens:
    if allien.lower() == 'red':
        print('Boss killed(Red).\n+15 exp.\n')
    elif allien.lower() == 'yellow':
        print('Mini-boss killed(Yellow).\n+10 exp.\n')
    else:
        print('Enemy killed(Green).\n+5 exp.\n') 