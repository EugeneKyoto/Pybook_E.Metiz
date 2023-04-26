# 3.10 Все функции.
hardlist = ['Functional testing', 'Testing theory']
hardlist.insert(0, 'QA Zen') # Метод вставки по индексу + значение.
hardlist.append('Python') # Метод append - вставка элемента в конец списка.
hardlist.append('Ruby')
del hardlist[-1] #Удаление последнего элемента списка "ненужного".
hardlist.insert(2, 'Friendly')
hardlist.remove('Friendly') # Удаление  из списка по значению.
hardlist.append('Music')
popped_values = hardlist.pop(-1) # Удаление значения из списка с возвратом в переменную.
hardlist.sort()

print(hardlist, popped_values, sep='\n')