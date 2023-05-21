# 5.12 Стиль оформления команд if. (empty file в GitHub?)
# команды if нужно оформлять согласно PEP8 (на примере 5.11):
for i in range(1, 10):
    if i == 1:
        print(f'{i}st!')
    if 1 < i <= 3:
        print(f'{i}rd')
    if 4 <= i <= 10:
        print(f'{i}th')
print('Not empty')