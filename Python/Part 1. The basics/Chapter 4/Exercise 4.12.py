# 4.12 Больше циклов.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(*[i for i in my_foods], sep='\n')
print(*[i for i in friend_foods], sep='\n')
