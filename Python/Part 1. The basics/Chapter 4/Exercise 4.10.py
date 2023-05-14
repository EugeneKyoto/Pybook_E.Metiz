# 4.10 Cегменты.
slices = ['Pybook', 'Computer', 'Time', 'Job', 'Cat', 'Home', 'Food']
print('The first three items in the list are:')
for i in slices[:3]:
    print(f'\t-{i}')

print('\nThree items from the middle of the list are:')
for i in slices[2:5]:
    print(f'\t-{i}')

print('\nThe last three items in the list are:')
for i in slices[-3:]:
    print(f'\t-{i}')